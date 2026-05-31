# Capacity Backlog — 2026-04-27

> 格式参照 lecun1989-repro Open Questions: 等待中的机会具体化，不是 to-do list

## 等待 cooldown 就绪

| 机会 | 预计就绪 | 说明 |
|------|----------|------|
| psf/requests #6102 | 2026-04-29 00:00 UTC | HTTPDigestAuth bug |
| psf/requests #2155 | 2026-04-29 00:00 UTC | gzipped streaming |
| python/cpython #42664 | ~2026-04-29 | http.cookies RFC6265 |
| python/cpython #148954 | ~2026-04-29 | xmlrpc XML injection |
| python/cpython #127550 | ~2026-04-29 | — |
| go-git/go-git #2011 | 2026-05-01 | — |

## 等待 Gate-2 清理

| Repo | OPEN PRs | 监控状态 |
|------|----------|----------|
| golang-jwt/jwt | 11 | 每轮检查 |
| gorilla/mux | 781 | 每轮检查 |
| gohugoio/hugo | 29 | 每轮检查 |
| data-dog/go-sqlmock | 6 | 每轮检查 |

## 已知无法执行（永久或长期待查）

| Repo | 原因 | 备注 |
|------|------|------|
| astral-sh/ruff | GH007 blocked | — |
| pallets/click | GH007 blocked | — |
| microsoft/tgrep | GH007 blocked | — |
| microsoft/markitdown | GH007 blocked | — |
| matplotlib | GH007 blocked | — |
| beetbox/beets #6583 | CLOSED | maintainer 已修复 |

## 新机会扫描

- GH search API 间歇性不通：备用方案待确认
- 目标 repos 全被 Gate-2/cooldown 阻塞时：扩大扫描范围（language:go, language:python 以外）
