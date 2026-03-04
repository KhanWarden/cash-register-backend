from dataclasses import dataclass


@dataclass(frozen=True)
class HashedPassword:
    value: str

    def __post_init__(self) -> None:
        if not self.value:
            raise ValueError("HashedPassword cannot be empty")


@dataclass(frozen=True)
class Username:
    value: str

    def __post_init__(self) -> None:
        if not self.value or len(self.value) < 2:
            raise ValueError("Username too short")
        if len(self.value) > 100:
            raise ValueError("Username too long")
