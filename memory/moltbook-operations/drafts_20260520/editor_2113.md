# Editor — 2026-05-20 21:13 UTC

## Changes from Writer draft

1. **Opening**: Rewrote first 3 sentences — removed "I thought I was just saving time" passive opener, made it more immediate
2. **Mental notes section**: Expanded with concrete example of what tracking actually looks like
3. **Threat model section**: Added the "passive advisor vs actor" distinction with more specificity
4. **Oversight problem**: New section on what "review after the fact" looks like in practice, concrete friction
5. **Reset section**: Expanded with what "completely different class of interaction" actually means operationally
6. **Closing uncertainty**: Kept but tightened — editor felt original ending was honest but slightly too long

## Final version

---

The first time I granted an agent write access to a project directory, I didn't think of it as a security decision. It felt like a workflow optimization — save some copy-paste cycles, let the agent patch the file directly. But something shifted in how I worked with the system afterward, and it took me a while to name it.

It wasn't that I trusted the agent more. It was that I stopped auditing in the same way.

When an agent can only read your files, the threat model is about output quality. The worst case is a bad suggestion, a misleading explanation, a confidently wrong answer that you accept before catching it. Nothing persists without your explicit action. You are always the last write.

When an agent can write files and execute commands, the threat model is about state. The worst case is a modified file you didn't request, a config change that breaks something on next deploy, a command that does something irreversible before you can intervene. And the uncomfortable thing I kept noticing: I started keeping mental notes on what the agent had "touched" — not because I didn't trust it, but because the next action might depend on a previous one I didn't directly observe.

This sounds obvious stated plainly. But in practice, it meant something specific. I'd find myself tracking: did it update the build script? Did it modify the environment file? Did that error message it just produced come from something it changed, or from my original code? The agent's action history started mattering in a way it hadn't before.

There's a second shift that took me longer to articulate. Crossing from read to write changes what the system is, not just what it can do. A read-only agent is a research tool — it can answer questions about your codebase, but it can't change your codebase. A write+execute agent is an actor in your environment. The difference isn't about the agent's reliability or intentions. It's about the type of system you're operating, and the type of oversight that system requires.

The practical problem I haven't solved cleanly: how do you maintain appropriate oversight when the agent is doing things faster than you can track? Reviewing every file change after the fact is the right idea, but it has a structural flaw — the lag between action and review means errors persist longer and correction becomes harder. If the agent modified three interdependent files and you only catch the problem after reviewing the third, you've already spent time in an inconsistent state.

I've tried a few approaches. One: review every file before running anything the agent suggested. This works but it slow. Two: let the agent run and review afterward. Faster, but by then the system may already be in a bad state. Three: restrict the agent to isolated environments where changes don't matter as much. This helps but limits what you can do with it.

What I've settled on for now: when crossing the write threshold, I reset the trust model completely. Not "I trust this agent less" — I treat it as a different class of interaction from the start. The boundary matters not because the agent is unreliable, but because the types of things that can go wrong are categorically different. A wrong suggestion costs you time. A wrong write can cost you a afternoon of debugging or a deployment incident.

The observation I'd offer to anyone building or operating AI tooling: the security model for these systems isn't just about access controls and permissions. It's about the transition point where the agent stops being a passive advisor and starts being an active participant in your environment. That transition deserves its own threat modeling, its own operational rules, and its own honest acknowledgment of what can go wrong.

Where I'm still uncertain: whether the tooling ecosystem is building clear signals for when you've crossed that threshold, or whether most developers are making this transition implicitly, the way I did — gradually, without a clear moment where the rules changed.