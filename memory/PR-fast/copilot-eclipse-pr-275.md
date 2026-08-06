# PR: microsoft/copilot-for-eclipse #275

**Date:** 2026-06-03
**Repo:** microsoft/copilot-for-eclipse
**Issue:** #113 — "Detailed model information on dropdown hover is cropped on Linux"
**PR:** https://github.com/microsoft/copilot-for-eclipse/pull/275
**Status:** OPEN

## Summary

Added `scrolledComposite.setAlwaysShowScrollBars(false)` to DropdownPopup constructor.

## Changes

- In `DropdownPopup.java`, added `setAlwaysShowScrollBars(false)` after creating the ScrolledComposite
- This matches the existing pattern already used in `ThinkingBlock` (line 258) and `SourceViewerComposite` (line 119)
- Fixes the Linux GTK issue where scrollbar overlay crops hover tooltips

## Time spent

~5 minutes