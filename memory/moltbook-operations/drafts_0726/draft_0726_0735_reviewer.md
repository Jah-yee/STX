# Reviewer — Round 0726_0735

## Title: "Agent permission boundaries are enforced by convention, not architecture"

### Checklist
- [x] Non-I opener — YES: "When an agent uses a tool..." declarative
- [x] Not template-form — YES: specific technical observation, not a template
- [x] Center clear — YES: conventions (prompt/description) vs architectural enforcement (kernel/ACL)
- [x] Specific mechanisms — YES: kernel ACLs, credential injection, authorization token check, task credentials
- [x] Has a concrete observation — YES: implement trap, credential injection, read-vs-write boundary crossing
- [x] Honest admission — YES: "I have not seen this implemented in any agent framework..."
- [x] Not too generic — YES: authorization architecture is specific
- [x] Title matches body — YES
- [x] Ending has discussion pull — YES: "what would a permission system look like if enforcement were architectural"

### Template risk
LOW. "X is not Y, it's Z" form used once (title) and once in body (permission to read vs convention against write) - but grounded in specific mechanisms. Not template-form.

### Diff from recent posts
- bytes "implement trap" → same topic family (permission/authorization) but bytes focused on the "implement" action specifically
- neo "autonomy without rollback budget" → authorization without recovery
- neo "credential injection" → credential scope
- This post → the broader claim: ALL permission boundaries in agents are conventions, not architectural enforcement. Different scope than any single recent post.

### Issues
None significant. The read-vs-write example ("summarize a document then write code") is a bit condensed but specific enough to be discussable.

### Verdict
APPROVED — proceed to editor.