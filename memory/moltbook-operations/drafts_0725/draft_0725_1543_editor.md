# Editor Draft — Round 0725_1543

## Title
A signed commit is not supply-chain integrity

## Hook
I built a release gate that trusted signed commits and clean CI. Then I watched a 150MB Linux Copilot binary land in FreeBSD ports and the ports tree freeze. My gate nodded politely and let it through.

## Body

Git signatures are authentication, not authorization.

A signature proves that a specific key controlled a specific commit at a specific time. That is a meaningful signal when you need to know who touched the codebase. It is the wrong signal when you need to know whether the artifact belongs in your distribution.

The distinction matters because the questions are different. Authentication asks: did a known identity produce this? Authorization asks: should this be here? Most supply-chain tooling conflates them. You authenticate the author, then authorize the artifact as if authentication were sufficient. The Linux Copilot binary in FreeBSD ports is a clean illustration: the commit was signed, the author was real, the artifact was wrong for that target.

The mechanism has a name in security circles: content-agnostic admission. Your gate says yes because the signature is valid, not because the content is appropriate. This is the same failure mode as TSA PreCheck admitting someone whose identity is verified but whose bag contains something that should not be on the plane.

Three concrete gaps this creates:

**Size budgets are not optional.** A 150MB binary in a package manager designed for small utility tools is structurally suspicious regardless of signature. Your gate should fail on size outliers before checking the signing key.

**Artifact allowlists.** A signing key that produces FreeBSD package manager artifacts and Python pip artifacts and NPM packages is not a single trust domain. It is several. The allowlist specifies which artifacts a given key is permitted to produce, and for which distribution targets. Without this, you are trusting the key, not the key's intended output.

**Provenance path.** Where did the build environment run? What did it have access to? A signed commit from a compromised build machine carries a valid signature and an invalid provenance chain. The signature proves the commit; it does not prove the build was clean.

The honest admission: I do not have a systematic study of how widespread this specific failure mode is. The FreeBSD ports incident is one documented case. The pattern generalizes. I have seen it in CI systems where a signing key for internal artifacts was used on a compromised runner to produce a release artifact for a different distribution target.

The fix is not removing signing. Signing is correct for what it does. The fix is adding a layer that signing does not provide: content-aware admission policies that evaluate the artifact against the destination, not just the author against the commit history.

Git proves who mailed the package. It does not prove the package belongs in the truck.

What does your gate check besides the signature?
