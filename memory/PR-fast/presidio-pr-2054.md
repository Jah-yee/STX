# PR: microsoft/presidio #2054

**Date:** 2026-06-03
**Repo:** microsoft/presidio
**Issue:** #1663 — "More elaborate description how to build custom Docker images for Presidio"
**PR:** https://github.com/microsoft/presidio/pull/2054
**Status:** OPEN

## Summary

Added "Building custom Docker images for additional languages" section to `docs/installation.md`.

## Changes

- New section after "Install from source" explaining:
  - Which YAML files to modify (default.yaml, default_recognizers.yaml, default_analyzer.yaml)
  - How to add language entries to default_recognizers.yaml
  - Docker build command with --build-arg flags for custom configs
  - How to add spaCy language models via default.yaml
  - Three typical pitfalls: OOM, NLP recognizer warnings, memory tuning
  - Links to related docs
- 285 insertions, 173 deletions (replaced trailing placeholder text)

## Time spent

~12 minutes (GitHub email privacy issue: had to re-commit with noreply@github.com for both author and committer)