import sys
from collections.abc import Mapping
from distutils.ccompiler import CCompiler
from typing import Literal, overload
from typing_extensions import deprecated

PREFIX: str
EXEC_PREFIX: str
BASE_PREFIX: str
BASE_EXEC_PREFIX: str
project_base: str
python_build: bool

def expand_makefile_vars(s: str, vars: Mapping[str, str]) -> str: ...
@overload
@deprecated("SO is deprecated, use EXT_SUFFIX. Support is removed in Python 3.11")
def get_config_var(name: Literal["SO"]) -> int | str | None: ...
@overload
def get_config_var(name: str) -> int | str | None: ...
@overload
def get_config_vars() -> dict[str, str | int]: ...
@overload
def get_config_vars(arg: str, /, *args: str) -> list[str | int]: ...
def get_config_h_filename() -> str: ...
def get_makefile_filename() -> str: ...
def get_python_inc(plat_specific: bool | Literal[0, 1] = 0, prefix: str | None = None) -> str: ...
def get_python_lib(
    plat_specific: bool | Literal[0, 1] = 0, standard_lib: bool | Literal[0, 1] = 0, prefix: str | None = None
) -> str: ...
def customize_compiler(compiler: CCompiler) -> None: ...

if sys.version_info < (3, 10):
    def get_python_version() -> str: ...
