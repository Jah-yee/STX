# Editor — 0720_0813

## Changes (surgical)

1. **Opening**: "A rotated key inherits the same world" → keep, it's strong. The second sentence is doing too much work — trim "What they don't always realize is that rotation resets the credential — the who in authentication — but leaves the authorization state fully intact." Keep the credential vs permission distinction but make it land faster.

2. **The permission examples**: "read all buckets in that S3 prefix" / "fire webhooks to that internal endpoint" — good, concrete enough. Keep.

3. **The distinction sentence**: "**credential state** (what you prove with) and **permission state** (what you're allowed to do) are separate data structures." — bold the terms, this is the core. Keep verbatim.

4. **Two failure modes section**: Good. The "over-trust" and "under-trust" labels help. Keep.

5. **Final question**: "what permissions does this principal still have, and do we still want them there?" — sharp. Keep.

6. **Closing line**: "The two don't automatically track each other." — fine but could be punchier. "They don't co-evolve unless something forces them to." → keep original, it's cleaner.

## Final version

---

A rotated key inherits the same world.

Rotation resets the credential — what you prove with. It doesn't touch the authorization state — what you're allowed to do. The permissions, role bindings, and downstream trust decisions were set by the old key and survive the rotation unchanged.

That means a fresh key with the same access scope has the same blast radius as the one it replaced. If the old key could read all buckets in that S3 prefix, the new key can too. If it could fire webhooks to that internal endpoint, the new one can as well.

The distinction that matters: **credential state** (what you prove with) and **permission state** (what you're allowed to do) are separate data structures. Rotation touches the first. Authorization logic touches the second.

There are two failure modes from this.

**Over-trust in rotation.** "We rotated the key" is treated as equivalent to "the access is revoked." It isn't, unless your authorization layer is explicitly keyed to the credential — which most aren't. The permission stands until something removes it.

**Under-trust in new keys.** A fresh key feels clean because it has zero history. But if the IAM role it's attached to has broad permissions, the new key is immediately a wide-open door. A key's age tells you nothing about the permissions it carries.

After any credential rotation, the right question is not "is this key new?" It's "what permissions does this principal still have, and do we still want them there?"

The two don't automatically track each other.
