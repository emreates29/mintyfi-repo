import torch

cihaz = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Kullanılan cihaz: {cihaz}")

a = torch.randn(3, 3, device=cihaz)
b = torch.randn(3, 3, device=cihaz)
print("Tensor a:\n", a)
print("Tensor b:\n", b)

toplam = a + b
print("\nToplam (a + b):\n", toplam)

matris_carpim = torch.matmul(a.T, b)
print("\nMatris çarpımı (a.T @ b):\n", matris_carpim)

relu_sonuc = torch.relu(a)
print("\nReLU uygulanmış a:\n", relu_sonuc)

duzlestirilmis = a.view(-1)
print("\nDüzleştirilmiş a (flattened):\n", duzlestirilmis)

x = torch.randn(3, 3, requires_grad=True, device=cihaz)
w = torch.randn(3, 2, requires_grad=True, device=cihaz)
y = x @ w
kayıp = y.sum()
kayıp.backward()

print("\nx tensörünün gradyanı:\n", x.grad)
print("w tensörünün gradyanı:\n", w.grad)
