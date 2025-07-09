"""Tests for MQTT configuration."""
import os
from src import mqtt_config


class TestMQTTConfig:
    """Test MQTT configuration constants and defaults."""
    
    def test_topic_constants_exist(self):
        """Test that all required MQTT topic constants are defined."""
        assert hasattr(mqtt_config, 'MODEL_DISTRIBUTE_TOPIC')
        assert hasattr(mqtt_config, 'MODEL_UPDATES_TOPIC')
        assert hasattr(mqtt_config, 'MODEL_AGGREGATED_TOPIC')
        
        # Check they are strings
        assert isinstance(mqtt_config.MODEL_DISTRIBUTE_TOPIC, str)
        assert isinstance(mqtt_config.MODEL_UPDATES_TOPIC, str)
        assert isinstance(mqtt_config.MODEL_AGGREGATED_TOPIC, str)
    
    def test_qos_constants_exist(self):
        """Test that QoS level constants are defined."""
        assert hasattr(mqtt_config, 'QOS_AT_MOST_ONCE')
        assert hasattr(mqtt_config, 'QOS_AT_LEAST_ONCE')
        assert hasattr(mqtt_config, 'QOS_EXACTLY_ONCE')
        
        # Check they are integers with correct values
        assert mqtt_config.QOS_AT_MOST_ONCE == 0
        assert mqtt_config.QOS_AT_LEAST_ONCE == 1
        assert mqtt_config.QOS_EXACTLY_ONCE == 2
    
    def test_broker_configuration_exists(self):
        """Test that broker configuration variables exist."""
        assert hasattr(mqtt_config, 'BROKER_URL')
        assert hasattr(mqtt_config, 'BROKER_PORT')
        assert hasattr(mqtt_config, 'USE_TLS')
        
        # Check types
        assert isinstance(mqtt_config.BROKER_URL, str)
        assert isinstance(mqtt_config.BROKER_PORT, int)
        assert isinstance(mqtt_config.USE_TLS, bool)
    
    def test_default_values(self):
        """Test that default values are reasonable."""
        # Clear environment variables for this test
        original_url = os.environ.get('MQTT_BROKER_URL')
        original_port = os.environ.get('MQTT_BROKER_PORT')
        
        if 'MQTT_BROKER_URL' in os.environ:
            del os.environ['MQTT_BROKER_URL']
        if 'MQTT_BROKER_PORT' in os.environ:
            del os.environ['MQTT_BROKER_PORT']
        
        try:
            # Reload the module to get defaults
            import importlib
            importlib.reload(mqtt_config)
            
            assert mqtt_config.BROKER_URL == "localhost"
            assert mqtt_config.BROKER_PORT == 8883
            assert mqtt_config.USE_TLS is True
            
        finally:
            # Restore environment variables
            if original_url is not None:
                os.environ['MQTT_BROKER_URL'] = original_url
            if original_port is not None:
                os.environ['MQTT_BROKER_PORT'] = original_port
            
            # Reload again to restore original state
            importlib.reload(mqtt_config)
