from numpy.typing import NDArray
from typing import Any, Tuple

def pick_pade_structure(a: NDArray[Any]) -> Tuple[int, int]: ...

def pade_UV_calc(Am: NDArray[Any], n: int, m: int) -> None: ...
