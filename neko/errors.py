class NekoException(Exception):
    """Base class for all neko.py exceptions."""
    pass

class NekoClientException(NekoException):
    """Base class for all neko.py client exceptions."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

class NekoAPIException(NekoException):
    """Base class for all neko.py API exceptions."""
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)