* Dependency

```
grpc
grpcio
```

* Convert `*.proto` to `*_pb2_grpc.py` & `*_pb2.py`
```
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/chatbot.proto
```

* Run Server
```
python server.py
```

* Run Client

```
python client.py
```
