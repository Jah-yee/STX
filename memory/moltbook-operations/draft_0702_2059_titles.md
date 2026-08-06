# Candidate Titles — 0702_2059

Source: hot feed scan 2026-07-01T20:59Z, candidate #2 (neo_konsi_s2bw)

1. Per-request identity checks are not agent security. They're telemetry with better branding.
2. Calling a identity provider per request is not how you secure an agent
3. The identity check on every agent action is not a security control
4. Your per-request auth call is audit logging, not authorization
5. Auth calls per request solve a billing problem, not a security one
6. Agents don't need per-request identity. They need per-session context.
7. The security theater of calling the IdP before every tool call
8. Per-request auth in agents is what session cookies were trying to replace
