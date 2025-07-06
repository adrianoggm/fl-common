from abc import ABC, abstractmethod


class IModelSerializer(ABC):
    @abstractmethod
    def serialize_weights(self, weights: dict) -> bytes: ...
    @abstractmethod
    def deserialize_weights(self, blob: bytes) -> dict: ...
