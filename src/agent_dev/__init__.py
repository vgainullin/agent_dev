"""Rename this package to your project name (see README)."""

import contextlib
import importlib
import os
import random


def seed_everything(seed: int) -> None:
    """Seed Python, NumPy and PyTorch (whichever are installed) from one value (AGENTS.md §3)."""
    os.environ["PYTHONHASHSEED"] = str(seed)  # affects subprocesses only
    random.seed(seed)
    with contextlib.suppress(ImportError):
        importlib.import_module("numpy").random.seed(seed)
    try:
        torch = importlib.import_module("torch")
    except ImportError:
        return
    torch.manual_seed(seed)  # also seeds all CUDA devices
