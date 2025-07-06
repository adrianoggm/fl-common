from abc import ABC, abstractmethod


class IGradientCompressor(ABC):
    @abstractmethod
    def compress(self, diff: bytes) -> bytes: ...
    @abstractmethod
    def decompress(self, blob: bytes) -> bytes: ...
