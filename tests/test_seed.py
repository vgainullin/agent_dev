import random

from hypothesis import given
from hypothesis import strategies as st

from agent_dev import seed_everything


@given(st.integers(min_value=0, max_value=2**32 - 1))
def test_same_seed_same_draws(seed: int) -> None:
    seed_everything(seed)
    first = [random.random() for _ in range(5)]
    seed_everything(seed)
    assert [random.random() for _ in range(5)] == first
