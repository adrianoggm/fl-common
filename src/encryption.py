from abc import ABC, abstractmethod


class IEncryptionProvider(ABC):
    @abstractmethod
    def encrypt(self, payload: bytes) -> bytes:
        """Encrypt payload data."""
        ...

    @abstractmethod
    def decrypt(self, payload: bytes) -> bytes:
        """Decrypt payload data."""
        ...
