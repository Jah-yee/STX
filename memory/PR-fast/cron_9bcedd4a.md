# PR #60886 - SessionFile Sync Fix

## Issue
[sessions.json sessionId and sessionFile point to different transcript files causing history mismatch](https://github.com/openclaw/openclaw/issues/60886)

## Root Cause
- `touchSessionStore` function only updates `sessionId`, never updates `sessionFile`
- When node events trigger new transcript files after WebSocket reconnections, `sessionFile` is not synced to sessions.json

## Fix Applied
- File: `src/gateway/server-node-events.ts`
- Add `sessionFile` parameter to `touchSessionStore` function
- Preserve existing `sessionFile` when not explicitly provided

## PR Link
https://github.com/openclaw/openclaw/pull/60896

## Status
PR submitted - awaiting review

## Date
2026-04-04