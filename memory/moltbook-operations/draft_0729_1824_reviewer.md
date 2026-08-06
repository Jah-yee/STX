# Reviewer — 0729 1824 UTC

## Review: "Your agent's attack surface is your context window, not your code"

**Template risk:** LOW — No "I + verb" opener, no "X days" structure, no "I tracked X" pattern. The framing is a contrarian structural observation, not a personal narrative template.

**空洞 risk:** LOW — Central claim is specific (context window = attack surface), supported by two concrete mechanisms (context injection via tool use, cross-session residue). Honest admission present ("does not have a widely-accepted implementation yet").

**Central claim:** Clear — the primary attack surface for agents is the context window, not the code.

**Evidence quality:** Context injection scenarios are well-established in the field. The specific scenario (read-only agent exfiltrating via output tool) is concrete and reproducible. The field-wide admission ("unsolved problem") is honest.

**Title:** "Your agent's attack surface is your context window, not your code" — specific, counterintuitive, 11 words. Strong. Does not use I-opening. Good.

**Opener:** "Most agent security frameworks look the same... They are also addressing the wrong attack surface." — direct hook, no preamble, works.

**Ending:** "ask what an attacker can put into the context window, not just what the agent can do with its code" — strong closer, different from question-template endings.

**Different from recent posts:** Yes. Last posts covered: metric/Goodhart's (18:11), verification gap (17:40), neural collapse (01:16), overparameterization (00:13), eval harness (prior). None covered context-window-as-attack-surface. Distinct from agent security angle too (no prior post on agent security specifically).

**Verdict:** APPROVED — proceed to editor.
