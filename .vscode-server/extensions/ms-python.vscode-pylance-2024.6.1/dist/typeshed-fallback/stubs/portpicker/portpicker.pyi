import socket
from typing_extensions import TypeAlias

_Port: TypeAlias = int

__all__ = ("bind", "is_port_free", "pick_unused_port", "return_port", "add_reserved_port", "get_port_from_port_server")

class NoFreePortFoundError(Exception): ...

def add_reserved_port(port: _Port) -> None: ...
def return_port(port: _Port) -> None: ...
def bind(port: _Port, socket_type: socket.SocketKind, socket_proto: int) -> _Port | None: ...
def is_port_free(port: _Port) -> bool: ...
def pick_unused_port(pid: int | None = None, portserver_address: str | None = None) -> _Port: ...
def get_port_from_port_server(portserver_address: str, pid: int | None = None) -> _Port | None: ...

# legacy aliases
Bind = bind
GetPortFromPortServer = get_port_from_port_server
IsPortFree = is_port_free
PickUnusedPort = pick_unused_port
