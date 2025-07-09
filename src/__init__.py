"""
fl-common: Shared interfaces and utilities for Federated Learning system.

This package provides the core abstractions and protobuf definitions
that all FL components (clients, server, aggregation service) use.
"""

from .serializers import IModelSerializer
from .encryption import IEncryptionProvider
from .compression import IGradientCompressor

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "adrianoggm@correo.ugr.es"

__all__ = [
    "IModelSerializer",
    "IEncryptionProvider", 
    "IGradientCompressor",
]