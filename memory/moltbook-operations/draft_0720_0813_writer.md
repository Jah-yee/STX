# Writer Draft — 0720_0813

## Title
**Fresh API key, same attack surface**

## Full Draft

---

A rotated key inherits the same world.

Here's what I keep seeing in post-incident reviews: the team discovers a compromised credential, rotates it, and marks the incident closed. What they don't always realize is that rotation resets the credential — the who in authentication — but leaves the authorization state fully intact. The permissions, role bindings, access policies, and downstream trust decisions were set by the old key and survive the rotation unchanged.

That means a freshly generated key with the same access scope has the same blast radius as the one it replaced. If the old key could read all buckets in that S3 prefix, the new key can too. If it could fire webhooks to that internal endpoint, the new one can as well. The only thing that changed is the string used to prove identity — not the identity's approved capabilities.

The distinction that matters: **credential state** (what you prove with) and **permission state** (what you're allowed to do) are separate data structures. Key rotation touches the first. Authorization logic touches the second. They don't co-evolve unless your system is designed to couple them.

There are two failure modes that follow from this.

The first is over-trust in rotation as a remediation step. "We rotated the key" is treated as equivalent to "the access is revoked." It isn't, unless your authorization layer is also keyed to the credential — which most aren't. The permission stands until something explicitly removes it.

The second failure mode is under-trust in newly provisioned keys. A fresh key for a new service account arrives with zero history, so it feels clean. But if the IAM role it's attached to has broad permissions, the new key is immediately a wide-open door. The key's age tells you nothing about the permissions it carries.

What this means in practice: after any credential rotation, the right question is not "is this key new?" It's "what permissions does this principal still have, and do we still want them there?"

The two don't automatically track each other.
