"""Tests for gradient compressors interface."""
import pytest
from abc import ABC

from src.compression import IGradientCompressor


class TestIGradientCompressor:
    """Test the IGradientCompressor interface structure."""
    
    def test_interface_is_abstract(self):
        """Test that IGradientCompressor is an abstract base class."""
        assert issubclass(IGradientCompressor, ABC)
        
        # Should not be able to instantiate directly
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            IGradientCompressor()
    
    def test_interface_has_required_methods(self):
        """Test that the interface defines the required abstract methods."""
        # Check that the abstract methods exist
        assert hasattr(IGradientCompressor, 'compress')
        assert hasattr(IGradientCompressor, 'decompress')
        
        # Check that they are abstract
        assert getattr(IGradientCompressor.compress, '__isabstractmethod__', False)
        assert getattr(IGradientCompressor.decompress, '__isabstractmethod__', False)
    
    def test_method_signatures(self):
        """Test that methods have correct signatures."""
        import inspect
        
        # Check compress signature
        compress_sig = inspect.signature(IGradientCompressor.compress)
        compress_params = list(compress_sig.parameters.keys())
        assert 'self' in compress_params
        assert 'diff' in compress_params
        
        # Check decompress signature
        decompress_sig = inspect.signature(IGradientCompressor.decompress)
        decompress_params = list(decompress_sig.parameters.keys())
        assert 'self' in decompress_params
        assert 'blob' in decompress_params
