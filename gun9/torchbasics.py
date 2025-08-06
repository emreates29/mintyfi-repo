import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Cihaz: {device}")

a = torch.randn(3, 3, device=device)
b = torch.randn(3, 3, device=device)
print("Tensor a:\n", a)
print("Tensor b:\n", b)

sum_tensor = a + b
print("\nToplam:\n", sum_tensor)

matmul_result = torch.matmul(a.T, b)
print("\nMatris çarpımı a.T @ b:\n", matmul_result)

relu_tensor = torch.relu(a)
print("\nReLU uygulanmış a:\n", relu_tensor)

reshaped = a.view(-1)
print("\nYeniden şekillendirilmiş (flattened) a:\n", reshaped)

x = torch.randn(3, 3, requires_grad=True, device=device)
w = torch.randn(3, 2, requires_grad=True, device=device)
y = x @ w
loss = y.sum()
loss.backward()

print("\nx tensörünün gradyanı:\n", x.grad)
print("w tensörünün gradyanı:\n", w.grad)
