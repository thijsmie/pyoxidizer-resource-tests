# PyOxidizer package resource tests

There are multiple mechanisms to read in-package python resources. In PyOxidizer some of those work, and then only for some setups. Here is an index what currently (2022-10-14) works:

```
Resource in main directory of module
pkgutil.get_data FAILURE
pkg_resources.resource_string SUCCESS
importlib.resources.open_text SUCCESS
importlib.resources.files FAILURE
importlib.resources.read_text SUCCESS
importlib.resources.read_binary SUCCESS
importlib.resources.contents SUCCESS
Resource in subdirectory of module
pkgutil.get_data FAILURE
pkg_resources.resource_string SUCCESS
importlib.resources.open_text CANT_USE
importlib.resources.files FAILURE
importlib.resources.read_text CANT_USE
importlib.resources.read_binary CANT_USE
importlib.resources.contents SUCCESS
```

These results were obtained by simply typing `pyoxidizer run` in the top level directory. The `CANT_USE` is here because some of the importlib.resources functions do not accept path separators in the resource names, making it impossible to access things in subdirectories. With `importlib.resources.files` not working at all your only option is `pkg_resources.resource_*` functions which work reliably in my tests.
