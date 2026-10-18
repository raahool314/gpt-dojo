# Curriculum (DRAFT - the architect expands this on /plan)

| #  | Module | Core idea |
|----|--------|-----------|
| 00 | Setup & workflow | env check, pytest, the tutoring loop |
| 01 | Tensors & broadcasting | shapes, views, indexing, einsum basics |
| 02 | Autograd by hand | build a scalar autograd engine, compare to torch |
| 03 | PyTorch autograd & nn.Module | backward, optimizers, training loop |
| 04 | Bigram language model | counting vs learned, NLL loss, sampling |
| 05 | MLP language model | embeddings, context windows, init, batching |
| 06 | Training dynamics | LR, activations/gradient stats, BatchNorm/LayerNorm |
| 07 | Tokenization | byte-level BPE from scratch, compare to tiktoken |
| 08 | Self-attention | Q/K/V, scaling, causal masking |
| 09 | Transformer block | multi-head, residuals, pre-norm, MLP |
| 10 | Train a small GPT | data pipeline, eval loss, sampling (temperature, top-k/p) |
| 11 | Scaling practicalities | mixed precision, grad accumulation, checkpoints, KV cache |
| 12 | Fine-tuning | instruction SFT, optional LoRA from scratch |
| 13 | Capstone | your own GPT, trained and fine-tuned, with a write-up |

## Change log
