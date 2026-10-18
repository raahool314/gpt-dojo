"""Run: uv run python scripts/check_env.py"""
import platform
import sys

print(f"Python {sys.version.split()[0]} on {platform.system()} {platform.machine()}")
try:
    import torch
except ImportError:
    sys.exit("PyTorch not installed - see README / setup steps.")

print(f"PyTorch {torch.__version__}")
if torch.cuda.is_available():
    device = "cuda"
    print(f"CUDA GPU: {torch.cuda.get_device_name(0)}")
elif getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
    device = "mps"
    print("Apple Silicon GPU (MPS) available")
else:
    device = "cpu"
    print("No GPU found - CPU is fine for modules 00-09.")

torch.manual_seed(0)
x = torch.randn(3, 4, device=device, requires_grad=True)
(x ** 2).sum().backward()
assert torch.allclose(x.grad, 2 * x.detach()), "autograd check failed"
print(f"Autograd check passed on {device}. You're ready.")
