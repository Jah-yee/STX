# Writer Draft — 0720_2054
Title: Your pentest found nothing. The attacker changed what the AI read.

---

A red team ran their standard assessment. Everything came back clean. No injection, no privilege escalation, no database exposure. The report read like a security win.

Three weeks later, an AI-assisted document system started surfacing sensitive internal memos to the wrong users. The investigation found the root cause: a modified file in the document store, specifically constructed to be retrieved by the AI and repeated verbatim — with a payload that redirected file access permissions.

No server was touched. No authentication was bypassed. The vulnerability was in the context window.

---

This is the class of attack that standard penetration testing does not see.

A penetration test audits your infrastructure. It probes APIs, authentication layers, database queries, and access controls. It tests the distance between an attacker and your servers. When it comes to AI systems, it typically stops at the model interface — the text that goes in and the text that comes out.

But an AI system has a second attack surface that lives upstream: the data it reads. The retrieved documents. The system prompts. The conversation history. The context that shapes what the model will do with its capabilities. If an attacker can place content in that context — not by breaking your server but by getting the AI to read a modified document — they have effectively rewritten the operating environment from inside the model.

This is prompt injection, but the entry point is not the model itself. It's the retrieval pipeline that feeds it.

---

The practical implication is that your security perimeter is now partly semantic. The question "can an attacker write to the context?" is not answered by checking if they can write to your database. It depends on what the retrieval system will fetch and surface — and whether any of those sources accept untrusted input.

Consider what a strict content security boundary looks like for AI retrieval:
- Which data sources can AI read without a human in the loop?
- Can any of those sources accept content from outside the trust boundary?
- When the AI reads a document, does it treat it as data or instruction?
- Does your evaluation framework test retrieval-side attacks or only prompt-side ones?

Most teams answer these questions incompletely, not because they are careless but because the security function is split. Infrastructure security owns the server. Application security owns the API. ML teams own the model. The retrieval layer — the pipeline between your data and the model — often falls between all three.

---

What makes this particularly difficult is that the attack succeeds without the model doing anything obviously wrong. The model is faithfully acting on what it read. It retrieved a file, applied the permissions described in that file, and shared the document with a user. The behavior is internally consistent. The failure is in the composition: the file was not authored by a trusted principal, but the retrieval pipeline did not check.

You cannot catch this by monitoring model outputs for anomalous behavior. You catch it by auditing what the model reads — before it reads it.

---

I do not have a clean answer for what this monitoring looks like at scale. Content provenance for AI context is an unsolved problem. Digital signatures on documents are standard practice; digital signatures that AI retrieval pipelines can verify are not. The ecosystem has not caught up to the threat model.

What I can say is this: if your security posture depends on "the AI only reads trusted documents," you need to verify that claim the same way you verify any security claim — with a test that actively tries to violate it.

Run an injection assessment that targets the retrieval layer, not just the model prompt. Ask: what happens if the content the AI retrieves is adversarial? Can we inject at the document level?

Your pentest will come back clean. The attack surface it didn't test is where the next incident will be.
