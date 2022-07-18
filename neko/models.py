from dataclasses import dataclass


@dataclass(repr=True, frozen=True)
class Image:
    url: str

    def __str__(self):
        return self.url

    def __repr__(self):
        return self.url