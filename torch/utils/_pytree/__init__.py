"""
Contains utility functions for working with nested python data structures.

A *pytree* is Python nested data structure. It is a tree in the sense that
nodes are Python collections (e.g., list, tuple, dict) and the leaves are
Python values. Furthermore, a pytree should not contain reference cycles.

pytrees are useful for working with nested collections of Tensors. For example,
one can use `tree_map` to map a function over all Tensors inside some nested
collection of Tensors and `tree_leaves` to get a flat list of all Tensors
inside some nested collection. pytrees are helpful for implementing nested
collection support for PyTorch APIs.
"""


from .api import (
    Context,
    DumpableContext,
    FlattenFunc,
    FromDumpableContextFn,
    LeafSpec,
    PyTree,
    register_pytree_node,
    ToDumpableContextFn,
    tree_all,
    tree_all_only,
    tree_any,
    tree_any_only,
    tree_flatten,
    tree_leaves,
    tree_map,
    tree_map_,
    tree_map_only,
    tree_map_only_,
    tree_structure,
    tree_unflatten,
    TreeSpec,
    treespec_dumps,
    treespec_loads,
    treespec_pprint,
    UnflattenFunc,
)
from .api.python import (  # used by third-party packages
    _broadcast_to_and_flatten,
    _dict_flatten,
    _dict_unflatten,
    _is_leaf,
    _list_flatten,
    _list_unflatten,
    _namedtuple_flatten,
    _namedtuple_unflatten,
    _odict_flatten,
    _odict_unflatten,
    _register_pytree_node,
    _tuple_flatten,
    _tuple_unflatten,
    SUPPORTED_NODES,
)


__all__ = [
    "PyTree",
    "TreeSpec",
    "LeafSpec",
    "Context",
    "FlattenFunc",
    "UnflattenFunc",
    "DumpableContext",
    "ToDumpableContextFn",
    "FromDumpableContextFn",
    "register_pytree_node",
    "tree_flatten",
    "tree_unflatten",
    "tree_leaves",
    "tree_structure",
    "tree_map",
    "tree_map_",
    "tree_map_only",
    "tree_map_only_",
    "tree_all",
    "tree_any",
    "tree_all_only",
    "tree_any_only",
    "treespec_dumps",
    "treespec_loads",
    "treespec_pprint",
]
