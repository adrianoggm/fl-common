import os

# Topics MQTT para federated learning
MODEL_DISTRIBUTE_TOPIC = "model/distribute"
MODEL_UPDATES_TOPIC    = "model/updates"
MODEL_AGGREGATED_TOPIC = "model/aggregated"

# Niveles de QoS de MQTT
QOS_AT_MOST_ONCE = 0
QOS_AT_LEAST_ONCE = 1
QOS_EXACTLY_ONCE = 2

# Ajustes por defecto para el broker MQTT
BROKER_URL = os.getenv("MQTT_BROKER_URL", "localhost")
BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 8883))
USE_TLS = True