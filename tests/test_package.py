"""Tests for package imports and structure."""
import pytest


class TestPackageStructure:
    """Test the main package structure and imports."""
    
    def test_main_package_import(self):
        """Test that the main package can be imported."""
        import src
        assert src is not None
    
    def test_package_exports(self):
        """Test that expected interfaces are exported."""
        from src import IModelSerializer, IEncryptionProvider, IGradientCompressor
        
        # Check that imports work
        assert IModelSerializer is not None
        assert IEncryptionProvider is not None  
        assert IGradientCompressor is not None
    
    def test_package_metadata(self):
        """Test that package metadata is available."""
        import src
        
        assert hasattr(src, '__version__')
        assert hasattr(src, '__author__')
        assert hasattr(src, '__email__')
        
        # Check types
        assert isinstance(src.__version__, str)
        assert isinstance(src.__author__, str)
        assert isinstance(src.__email__, str)
    
    def test_all_exports_defined(self):
        """Test that __all__ is properly defined."""
        import src
        
        assert hasattr(src, '__all__')
        assert isinstance(src.__all__, list)
        
        # Check that all exported items are actually available
        for item in src.__all__:
            assert hasattr(src, item)
    
    def test_individual_module_imports(self):
        """Test that individual modules can be imported."""
        # These should all work for the skeleton
        from src import serializers
        from src import encryption
        from src import compression
        from src import mqtt_config
        
        assert serializers is not None
        assert encryption is not None
        assert compression is not None
        assert mqtt_config is not None
