"""Tests for model serializers interface."""
import pytest
from abc import ABC

from src.serializers import IModelSerializer


class TestIModelSerializer:
    """Test the IModelSerializer interface structure."""
    
    def test_interface_is_abstract(self):
        """Test that IModelSerializer is an abstract base class."""
        assert issubclass(IModelSerializer, ABC)
        
        # Should not be able to instantiate directly
        with pytest.raises(TypeError, match="Can't instantiate abstract class"):
            IModelSerializer()
    
    def test_interface_has_required_methods(self):
        """Test that the interface defines the required abstract methods."""
        # Check that the abstract methods exist
        assert hasattr(IModelSerializer, 'serialize_weights')
        assert hasattr(IModelSerializer, 'deserialize_weights')
        
        # Check that they are abstract
        assert getattr(IModelSerializer.serialize_weights, '__isabstractmethod__', False)
        assert getattr(IModelSerializer.deserialize_weights, '__isabstractmethod__', False)
    
    def test_method_signatures(self):
        """Test that methods have correct signatures."""
        import inspect
        
        # Check serialize_weights signature
        serialize_sig = inspect.signature(IModelSerializer.serialize_weights)
        serialize_params = list(serialize_sig.parameters.keys())
        assert 'self' in serialize_params
        assert 'weights' in serialize_params
        
        # Check deserialize_weights signature  
        deserialize_sig = inspect.signature(IModelSerializer.deserialize_weights)
        deserialize_params = list(deserialize_sig.parameters.keys())
        assert 'self' in deserialize_params
        assert 'blob' in deserialize_params
