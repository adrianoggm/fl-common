from abc import ABC, abstractmethod


class IGradientCompressor(ABC):
    @abstractmethod
    def compress(self, diff: bytes) -> bytes:
        """Compress gradient data."""
        ...

    @abstractmethod
    def decompress(self, blob: bytes) -> bytes:
        """Decompress gradient data."""
        ...
