# Fix for pandas meson.build with Meson 1.11.0

## Problem

Meson 1.11.0 changed the `dependencies` keyword argument for `python.extension_module()` 
from `array[str]` to `array[Dependency | InternalDependency]`.

Error:
```
../pandas/_libs/tslibs/meson.build:32:7: ERROR: python.extension_module keyword argument 'dependencies' was of type array[str] but should have been array[Dependency | InternalDependency]
```

## Solution

In `pandas/_libs/tslibs/meson.build` line 32, change:

```meson
# OLD - strings (WRONG in Meson 1.11.0+)
py.extension_module('tzcode',
    sources,
    dependencies: ['libc'],  # strings - FAILS
)
```

To:

```meson
# NEW - Dependency objects (CORRECT)
py.extension_module('tzcode',
    sources,
    dependencies: [dependency('libc')],  # Dependency object - WORKS
)
```

## Key Changes

1. Convert each string dependency name to `dependency('name')` 
2. For internal dependencies, use `declare_dependency(link_with: lib_target)`
3. Python dependency is automatically handled: `py.dependency()`

## Example fix pattern

```meson
# Find all occurrences like:
#   dependencies: ['dep1', 'dep2']
# Change to:
#   dependencies: [dependency('dep1'), dependency('dep2')]

# For internal libs:
my_lib = static_library(...)
# Replace internal string with:
#   dependencies: [declare_dependency(link_with: my_lib)]
```