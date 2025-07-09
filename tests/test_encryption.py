"""Tests for encryption providers interface."""
import pytest
from abc import ABC

from src.encryption import IEncryptionProvider


class TestIEncryptionProvider:
    """Test the IEncryptionProvider interface structure."""
    
    def test_interface_is_abstract(self):
        """Test that IEncryptionProvider is an abstract base class."""
        assert issubclass(IEncryptionProvider, ABC)
        
        # Should not be able to instantiate directly
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            IEncryptionProvider()
    
    def test_interface_has_required_methods(self):
        """Test that the interface defines the required abstract methods."""
        # Check that the abstract methods exist
        assert hasattr(IEncryptionProvider, 'encrypt')
        assert hasattr(IEncryptionProvider, 'decrypt')
        
        # Check that they are abstract
        assert getattr(IEncryptionProvider.encrypt, '__isabstractmethod__', False)
        assert getattr(IEncryptionProvider.decrypt, '__isabstractmethod__', False)
    
    def test_method_signatures(self):
        """Test that methods have correct signatures."""
        import inspect
        
        # Check encrypt signature
        encrypt_sig = inspect.signature(IEncryptionProvider.encrypt)
        encrypt_params = list(encrypt_sig.parameters.keys())
        assert 'self' in encrypt_params
        assert 'payload' in encrypt_params
        
        # Check decrypt signature
        decrypt_sig = inspect.signature(IEncryptionProvider.decrypt)
        decrypt_params = list(decrypt_sig.parameters.keys())
        assert 'self' in decrypt_params
        assert 'payload' in decrypt_params
