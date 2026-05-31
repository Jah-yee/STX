# PR: gh-issues prompt injection fix

**Date:** 2026-04-05
**Issue:** Template injection via issue body in gh-issues skill

**Fix:** Wrap issue body and review comment body in CDATA markers to prevent XML/HTML injection

**PR:** https://github.com/openclaw/openclaw/pull/61040

**Status:** Open