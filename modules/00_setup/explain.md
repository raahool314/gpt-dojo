# Module 00 evidence — environment check

## Current environment-check output (2026-10-19)

```
Python 3.12.12 on Windows AMD64
PyTorch 2.6.0+cu124
CUDA GPU: NVIDIA GeForce MX330
Autograd check passed on cuda. You're ready.
```

## Environment fix record (2026-10-19)

**Problem:** `scripts/check_env.py` reported `No GPU found` even though the NVIDIA
GeForce MX330 was present and working (`nvidia-smi` shows driver 581.83, CUDA 13.0
runtime capable).

**Root cause:** the installed PyTorch was the **CPU-only build** (`2.14.1+cpu`,
`torch.backends.cuda.is_built() == False`). The GPU is not the problem; the wheel was.

**Fix:** point `uv` at the PyTorch CUDA 12.4 index and re-sync:

- `pyproject.toml` now has `[[tool.uv.index]]` named `pytorch-cu124`
  (https://download.pytorch.org/whl/cu124) and a `[tool.uv.sources]` entry
  forcing `torch` to resolve from that index.
- Version floor was corrected from a typo (`torch>=2.14.1`, which does not exist
  on any index) to `torch>=2.1.0`; the CUDA 12.4 index tops out at `2.6.0+cu124`.

**Reproduce:**
```bash
uv sync
uv run python scripts/check_env.py
```
Expected output starts with `PyTorch 2.6.0+cu124` and reports `CUDA GPU: NVIDIA GeForce MX330`.

## Notes for later modules

- The MX330 has 2 GB VRAM. That is fine for the tiny CPU-first GPT in this
  curriculum; `check_env.py`'s autograd check now runs on `cuda`.
- The default is still CPU-first; CUDA is available when a specific module
  benefits, but no curriculum gate requires it.

## Environment check output - evidence
```
(.venv) PS C:\Users\poona\projects\understanding-llms> uv run python .\scripts\check_env.py
Python 3.12.12 on Windows AMD64
PyTorch 2.6.0+cu124
CUDA GPU: NVIDIA GeForce MX330
Autograd check passed on cuda. You're ready.
```