# fl-common

**Shared interfaces, protobuf definitions, and utilities for our Federated Learning system.**  
This package defines the core messages, RPC services, and abstract base classes that all other FL components (clients, server, aggregation service, etc.) will import and implement.

---

## 📁 Repository Structure

```
fl-common/
├── proto/
│   ├── model.proto         # Messages for model weights & updates
│   └── service.proto       # gRPC service definitions (GetModel, SendUpdate)
│
├── src/
│   └── fl_common/
│       ├── __init__.py         # Package entry point
│       ├── serializers.py      # IModelSerializer: serialize/deserialize weight dictionaries
│       ├── encryption.py       # IEncryptionProvider: encrypt/decrypt byte payloads
│       └── compression.py      # IGradientCompressor: compress/decompress update diffs
│
├── tests/
│   └── test_serializers.py     # Unit tests for serializer implementations (example)
│
├── pyproject.toml          # Poetry build & dependency settings
└── README.md               # This documentation
```

---

## 1. `proto/`

- **`model.proto`**  
    Defines two core messages used throughout the system:
    - `ModelWeights` (raw checkpoint + version)
    - `ModelUpdate` (delta + sample count for FedAvg weighting)

- **`service.proto`**  
    *(Optional / future)* gRPC service definitions to fetch the global model and send updates.

> **Usage:**  
> After cloning, run:
> ```bash
> protoc --python_out=src/ --grpc_python_out=src/ proto/*.proto
> ```
> to generate the Python bindings.

---

## 2. `src/fl_common/`

Holds the abstract interfaces and shared logic:

- **`serializers.py`**  
    ```python
    class IModelSerializer(ABC):
            def serialize_weights(self, weights: dict) -> bytes: ...
            def deserialize_weights(self, blob: bytes) -> dict: ...
    ```
    *Implement this to convert your ML model’s weight dicts ↔ byte blobs (e.g. via pickle, Torch, ONNX).*

- **`encryption.py`**  
    ```python
    class IEncryptionProvider(ABC):
            def encrypt(self, payload: bytes) -> bytes: ...
            def decrypt(self, payload: bytes) -> bytes: ...
    ```
    *Plug in homomorphic encryption, secure aggregation, or simple AES here.*

- **`compression.py`**  
    ```python
    class IGradientCompressor(ABC):
            def compress(self, diff: bytes) -> bytes: ...
            def decompress(self, blob: bytes) -> bytes: ...
    ```
    *Supports sparsification, quantization, or sketching of model updates.*

---

## 3. `tests/`

- **`test_serializers.py`**  
    Example unit tests to validate any `IModelSerializer` implementation.  
    *Extend this folder with tests for your encryption & compression providers.*

---

## 4. `pyproject.toml`

- Managed by Poetry
- Defines package metadata, dependencies (protobuf), and build settings.

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
poetry install
```

### 2. Generate Protobuf bindings

```bash
protoc --proto_path=proto --python_out=src --grpc_python_out=src proto/*.proto
```

### 3. Run tests

```bash
poetry run pytest
```

---

## 📦 Publish

Once stable, tag a release and push to PyPI or your private package index:

```bash
poetry publish --build
```

---

> This **fl-common** package is the foundation for all Federated Learning components.  
> **Next up:** building `fl-ml-models` which will import these interfaces and provide out-of-the-box model trainers!