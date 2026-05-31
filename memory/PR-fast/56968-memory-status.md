# PR #56968 - Fix: status shows 'unavailable' for third-party memory plugins

## Status: ✅ MERGED

**Date:** 2026-04-04
**PR Link:** https://github.com/openclaw/openclaw/pull/60906

## Issue Summary

When using a third-party memory plugin (e.g., `memory-lancedb-pro`), the `openclaw status` command incorrectly displays "unavailable" despite the plugin being fully functional.

## Root Cause

- `resolveSharedMemoryStatusSnapshot()` called built-in config checks which only read `agents.defaults.memorySearch`
- Third-party plugin users have this disabled (using plugin instead)
- Returns `null` → displays "unavailable"

## Fix Summary

For third-party memory plugins (not `memory-core`), skip built-in config checks and directly query the plugin's memory search manager.

## Files Changed

- `src/commands/status.scan.shared.ts` +17 lines