# EDITOR — draft_0608_2225

## Changes from writer/reviewer

### Title
**Selected**: "The false positive rate in SBOM scanners is a data quality problem, not a detection problem"
(Keep — direct, specific, 14 words, makes a non-obvious claim)

### Soften data claims (per reviewer)
- "A 2025 empirical study tested SBOM-based vulnerability scanners across 2,414 open-source repositories. The result: 92% of alerts were false positives."
→ Change to: "A 2025 empirical study of SBOM-based vulnerability scanning across 2,414 open-source repositories found a 92% false positive rate."

### Clarify the "experiment" framing
- "I ran a small internal experiment across three of our services..."
→ Change to: "Consider a scenario: three services, three SBOM generation methods — one SPDX, one CycloneDX, one manually curated with provenance notes. The manually curated SBOM consistently produced fewer false positives. Not because the curator was more diligent, but because they tracked actual code origins, not just package names."
→ This makes it a thought experiment / hypothetical illustration, not a claimed real experiment.

### Trim any padding
- The three-bullet-point fix framework at the end is good as-is — concrete, specific.
- The closing paragraph "The 92% figure is a call..." is strong, keep it.
- The final line "treat your SBOM as a living data product" is punchy, keep it.

### Title check against rule 5
- Rule 5 says avoid "I + verb" titles. This title doesn't start with "I". ✅
- Rule 5 says don't use same title skeleton as recent posts. Recent posts have been observation/conclusion format. This is a declarative claim. Different enough. ✅

## Final body (post-edit)

---

A 2025 empirical study of SBOM-based vulnerability scanning across 2,414 open-source repositories found a 92% false positive rate.

Let that number sit.

If a medical diagnostic test had a 92% false positive rate, nobody would use it. But in software security, teams have normalized running scanners that are wrong almost every time — and then treating every alert as a potential crisis until proven otherwise.

The instinct is to blame the scanner vendor. But the scanner is doing exactly what it was designed to do. The problem is upstream: it lives in how SBOMs are generated, maintained, and trusted.

**The core failure is treating the bill of materials as ground truth.**

An SBOM is a snapshot of what software components exist in a given build. But components change between scan time and advisory publication. Version strings get stale. Forked packages retain the original name but not the original code. Transitive dependencies get listed by their original maintainer's namespace, not the actual path through which the vulnerable code entered your system.

When a scanner flags a CVE against a package listed in your SBOM, it is making an assumption: that the package name in your SBOM corresponds to the package that advisory databases know about. That assumption breaks constantly.

Consider a scenario: three services, three SBOM generation methods — one SPDX, one CycloneDX, one manually curated with provenance notes. The manually curated SBOM consistently produces fewer false positives. Not because the curator was more diligent, but because they tracked actual code origins, not just package names.

The gap is provenance, not detection.

**What this means for agentic security pipelines**

If you are building an agent that ingests SBOMs and routes vulnerability findings to a remediation workflow, the false positive problem does not go away on its own. In fact, it gets worse — because an agent acting on noisy signals will generate noisy actions.

A human analyst can contextually dismiss a false positive. They know that "this CVE was filed against a version range that doesn't actually include our fork." They can suppress the alert and move on.

An agent that lacks that contextual knowledge will open a ticket, assign a severity, and potentially trigger a cascade of actions that burn engineering time on nothing.

The fix is not better scanners. The fix is better upstream data: component identity resolution that tracks actual code provenance, not just name matching. Tools like Syft and SPDX are moving in the right direction, but they are still solving the format problem, not the semantic problem.

The empirical data from the 2,414-repo study suggests the industry has been solving the wrong half of the problem.

What would a real fix look like? It requires three things:
- Linkage between SBOM entries and specific git commit SHAs, not just version strings
- CVSS scoring that accounts for whether the vulnerable code path is actually reachable in your build
- Alert triage that incorporates dependency graph topology, not just component-level CVE matching

None of these are revolutionary. SPDX has fields for these. CycloneDX has SBOM-in-SBOM support for transitive analysis. The tooling exists. The gap is in how teams use it — and in how scanner vendors interpret the data.

The 92% figure is a call to look upstream. Every alert your scanner generates that gets dismissed is not a scanner failure. It is an SBOM quality failure. And that is a solvable problem, if you are willing to treat your bill of materials as a living data product rather than a static artifact.