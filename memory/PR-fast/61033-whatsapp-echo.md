# PR #61033 - WhatsApp Self-Message Loop Fix

**Date:** 2026-04-04
**Status:** OPEN ✅
**PR Link:** https://github.com/openclaw/openclaw/pull/61045

## Issue
WhatsApp self-message causes infinite reply loop when sending to oneself. The message gets echoed back as inbound.

## Solution
Skip messages where sender phone equals recipient phone (from === to).

## Changes
```diff
- logVerbose(`📱 Same-phone mode detected (from === to: ${msg.from})`);
+ logVerbose(`📱 Skipping self-message (from === to: ${msg.from}) to prevent infinite loop`);
+ return;
```

## Files Modified
- `extensions/whatsapp/src/auto-reply/monitor/on-message.ts`: +2, -1