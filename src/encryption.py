from abc import ABC, abstractmethod

class IEncryptionProvider(ABC):
    @abstractmethod
    def encrypt(self, payload: bytes) -> bytes: ...
    @abstractmethod
    def decrypt(self, payload: bytes) -> bytes: ...
