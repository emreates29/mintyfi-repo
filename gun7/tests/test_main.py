import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
import pytest
from main import app

@pytest.fixture(scope="module")
def client():
    """Test client oluşturur ve modül süresince kullanılır."""
    with TestClient(app) as c:
        yield c  

def test_predict_valid_input(client):
    """
    Geçerli metin ile /predict endpointinin 200 döndürüp
    doğru formatta label ve probability içerdiğini test eder.
    """
    response = client.post("/predict", json={"text": "Bugün saat 5’te toplantı var"})
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert "probability" in data
    assert isinstance(data["label"], str)
    assert isinstance(data["probability"], float)
    assert 0.0 <= data["probability"] <= 1.0

def test_predict_empty_input(client):
    """
    Boş istek gövdesi gönderildiğinde FastAPI'nin 422 hata kodu döndürdüğünü test eder.
    """
    response = client.post("/predict", json={})
    assert response.status_code == 422

def test_predict_spam_text(client):
    """
    Spam içerikli metinle yapılan isteğin 200 döndürüp,
    label ve probability tiplerinin doğru olduğunu test eder.
    """
    response = client.post("/predict", json={"text": "Kazandınız! Hemen tıklayın."})
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result["label"], str)
    assert isinstance(result["probability"], float)
