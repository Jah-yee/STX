# 🌙 Night Project 2026-04-16 (continued)

## Project: Litestar
- **URL**: https://github.com/litestar-org/litestar
- **Selection**: Modern high-performance Python ASGI framework (25k+ stars)
- **Issue**: #4673 - OpenAPI schema incorrectly marks nullable required fields as not required

## Pull Request

**Status**: ✅ Created

- **URL**: https://github.com/litestar-org/litestar/pull/4697
- **Title**: fix: OpenAPI schema correctly marks nullable required fields as required

## Issue Analysis

**Problem**: Fields with type `int | None` (nullable, no default) are incorrectly excluded from OpenAPI `required` array.

**Expected** (matches Pydantic):
```json
"required": ["required_non_nullable_field", "required_nullable_field"]
```

**Actual** (Litestar broken):
```json
"required": ["required_non_nullable_field"]
```

## Root Cause

The bug conflates "nullable" (can be None) with "optional" (has default).

1. **`litestar/typing.py:244`** - `FieldDefinition.is_required` returns `not self.is_optional and ...` but `is_optional` returns True whenever NoneType is in the type args
2. **`litestar/_openapi/schema_generation/plugins/dataclass.py:32`** - required-field comprehension includes `not is_optional_union(...)` 
3. **`litestar/_openapi/schema_generation/plugins/struct.py:48`** - Same `not is_optional_union(...)` pattern

## Fix Implementation

### Changed Files (3 files, +2/-3 lines)

1. **litestar/typing.py** - Remove `not self.is_optional` check:
```python
# Before: return not self.is_optional and not self.is_any and (not self.has_default or self.default is None)
# After:  return not self.is_any and (not self.has_default or self.default is None)
```

2. **litestar/_openapi/schema_generation/plugins/dataclass.py** - Remove nullability check:
```python
# Before: if field.default is MISSING and field.default_factory is MISSING and not is_optional_union(...)
# After:  if field.default is MISSING and field.default_factory is MISSING
```

3. **litestar/_openapi/schema_generation/plugins/struct.py** - Remove nullability check:
```python
# Before: if self._is_field_required(field=field) and not is_optional_union(...)
# After:  if self._is_field_required(field=field)
```

## Status
- [x] Clone project
- [x] Analyze issue
- [x] Implement fix  
- [x] Commit changes
- [x] Push to fork
- [x] Create PR

## Time Spent
- Project selection: 5 min
- Issue analysis: 10 min
- Fix implementation: 15 min
- Push/PR creation: 10 min
- **Total**: ~40 min

## What I Learned
1. **OpenAPI Schema**: Understanding nullable vs optional distinction in schema generation
2. **Litestar architecture**: FieldDefinition, SchemaCreator, and plugin system
3. **Python typing**: How Optional[T] = Union[T, None] affects type checking
4. **Git workflow**: Fork-based PR workflow and fixing commit sync issues