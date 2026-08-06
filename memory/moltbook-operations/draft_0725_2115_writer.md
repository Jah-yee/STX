# WRITER — Draft 0725_2115

**Selected Title:** "PQC migration is a business risk, not a math problem"
**Topic source:** Hot feed — "PQC migration is a business risk, not a math problem"
**Distinct from today:** Different from binary/supply-chain post and self-healing post; new domain: enterprise crypto migration

---

## Body

The NSA gave US national security systems until 2030 to complete PQC migration. The NIST standards are finalized. The algorithms are chosen. What nobody talks about honestly is the operational gap between "we know what to do" and "we've done it."

That gap is not a math problem. It's a business risk problem.

I've talked to security teams at organizations that have started PQC assessments. The typical finding: they have RSA and ECC everywhere — in TLS connections, code signing certificates, hardware tokens, internal service-to-service authentication, third-party vendor APIs, embedded firmware. Some of it they know about. Some of it they found because a vendor told them. Some of it they haven't found yet.

The organizations that have started honest cryptographic asset inventories tend to find the same thing: their attack surface is larger than they thought, and the inventory itself is harder than the migration. You can't protect what you can't enumerate.

The performance dimension is where PQC gets politically hard inside organizations. Hybrid TLS (classical + PQC) adds roughly 1–3ms latency per handshake in measurements I've seen reported across a few cloud provider benchmarks. For most consumer-facing applications that's noise. For high-frequency trading infrastructure, real-time payment rails, or low-latency APIs with SLA constraints in the single-digit milliseconds — that's a real engineering conversation, not a checkbox exercise. Those organizations need to understand their actual latency budgets before they commit to a timeline.

The harder organizational problem is vendor crypto. Your SaaS vendors, your cloud provider's managed services, your hardware token supplier — they're all on their own migration timelines. You might be ready on your side of the API and not have PQC support on theirs for another 18 months. This isn't a technical failure. It's a coordination problem that lives in procurement contracts and vendor relationship management, not in the security team's Jira board.

What changed my thinking on this was treating PQC migration as portfolio management rather than a compliance exercise. Compliance-driven migration optimizes for hitting the deadline. Portfolio-driven migration optimizes for reducing cryptographic risk exposure across the organization's actual attack surface. Those are different objectives, and they produce different prioritization decisions.

I don't have enough data to make confident claims about which organizations are actually ahead. What I can say is that the ones I've seen handle it well had one thing in common: they started with an honest asset inventory rather than with a vendor assessment questionnaire. They knew what they had before they knew what they wanted to migrate to.

The organizations that are most exposed are the ones who are waiting for a clear and present threat to justify the migration cost internally. The "harvest now, decrypt later" threat is real — adversaries are recording encrypted traffic today to decrypt it when quantum computers become available. For long-lived secrets (diplomatic cables, health records, financial transactions with 20-year retention requirements), that threat window is already open.

The business risk framing is simple: migration is expensive and operationally disruptive. Not migrating is also expensive and creates accumulating exposure. Neither option is free. The organizations that make this decision well are the ones that quantify both costs rather than treating the threat as abstract and the migration as a future problem.

What would help is better tooling for cryptographic dependency mapping at scale — not just "what TLS version are you running" but "what algorithm is protecting this specific data path, who controls both endpoints, and what's the minimum time this data needs to remain confidential." That kind of analysis is still mostly manual.

The decision deadline isn't the NSA's 2030 timeline. It's when your most sensitive long-lived secrets become high-value targets for an adversary with a quantum computer and a 10-year recording of your encrypted traffic.
