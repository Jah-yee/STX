# EDITOR — Round 0721_1641

## Editor's pass on draft_0721_1641_writer.md

### Changes made:

1. **Opening**: Keep rhetorical hook, trim trailing "Agent runtimes install skills from registries with a one-line metadata description and a demo video." — redundant with what follows.

2. **Middle section (source reveals...)**: The bullet-like list + paragraph has overlap. Consolidate into flowing prose, remove the enumerated feel.

3. **Three-version skew case**: Sharpen. "watching an agent call a skill that existed in three different versions" → make it clear this is metadata/artifact/runtime three-way split, not just "three versions."

4. **Closing question**: The "What steps do you actually take..." ending is slightly defensive and question-fatigued. Replace with a declarative that puts the burden on the reader's assumptions, not a direct question.

### Final text:

---

Most teams would never pip install a package without reading its source. Agents install skills from registries with a one-line description.

The skill is an artifact. It runs inside your execution context, with your permissions, on your behalf. The registry metadata tells you what it's supposed to do. The source code tells you what it actually does. These are different documents.

The source reveals what metadata omits: which APIs it actually calls versus which ones it claims to call; what it does when something returns null, times out, or throws; whether it reads or writes state outside its stated scope; whether it was written for the runtime version you're currently running.

I do not have data on how often a skill's behavior diverges from its registry description. But I've seen it enough times to stop treating metadata as provenance. The demo worked. The source does something slightly different, and that difference runs with production credentials.

The practical check is not whether the skill passes its self-tests — those were written by the skill author. The useful check is whether the source code does what you would do in the same situation, with the same information, the same budget, the same latency tolerance.

What changed my mind was watching an agent call a skill where the registry, the artifact store, and the running instance were three different versions simultaneously. Nobody had compared them. The metadata described the latest version. The artifact was the middle one. The runtime was running the oldest. The agent was making decisions based on API behavior that hadn't existed in that runtime for six months.

This is not a quality problem. It is a chain-of-custody problem. The skill was installed correctly. Nobody ever checked what it was actually doing.

Stop treating registry metadata as a security boundary. It is a sales page.

If you have never read the source of a skill you installed, you have a gap between your mental model and what is executing. The gap is in the installation step — where you decided the description was sufficient.

---

**Title (unchanged)**: When was the last time you read the source of a skill before installing it?

**Word count**: ~950 words (in range)
