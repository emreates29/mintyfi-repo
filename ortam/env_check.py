import torch
import numpy as np
import pandas as pd
import platform

print("Python sürümü:", platform.python_version())
print("NumPy sürümü:", np.__version__)
print("Pandas sürümü:", pd.__version__)
print("PyTorch sürümü:", torch.__version__)
print("CUDA kullanılabilir mi:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("CUDA versiyonu:", torch.version.cuda)
    print("GPU adı:", torch.cuda.get_device_name(0))