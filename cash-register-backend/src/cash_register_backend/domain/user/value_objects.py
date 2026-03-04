from dataclasses import dataclass


@dataclass(frozen=True)
class HashedPassword:
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise ValueError("HashedPassword cannot be empty")
