# Your model dependency is a version you forgot to pin

Most teams that deploy agents treat the model call as a stable interface. The function returns strings. The strings have gotten better over time. That's the product. Nobody tracks which model version produced which output, and when behavior drifts, the model version change is almost never on the list of hypotheses.

This is a specific failure I've started calling the unpinned dependency problem.

**The mechanism**

When a dependency in traditional software changes, the package manager flags it. `package-lock.json` or `go.sum` records the exact commit. When behavior changes unexpectedly, you can bisect to the version that introduced the difference. Your dependency graph is a version graph.

Model dependencies don't have this. The API call `gpt-4o-mini` is a routing label, not a version pin. The model behind that label changes, and the changelog is published after the change is live. The agent that worked last Tuesday uses a different `gpt-4o-mini` than the agent that works today — and neither team has a record of the difference.

The compounding version gets worse in agentic loops. A single user conversation can generate hundreds of model calls across what the team thinks of as one "version" of the agent. If a model update subtly shifts instruction-following behavior — how aggressively it follows implicit constraints, how it interprets underspecified steps — that shift compounds through the loop. The output at step twelve is downstream of a subtly different step four. By the time the failure surfaces as "the agent became unreliable," nobody can reconstruct which model version touched which intermediate result.

**Two specific cases**

Case one: a code review agent started failing on a specific repository pattern — consistently misidentifying the same type of dependency declaration. The team spent two days on prompt engineering. The actual cause was a model update three days earlier that changed how the model handled a specific class of configuration format. The agent wasn't broken. The model was a different model.

Case two: an eval suite ran nightly against the same prompt set. Scores held steady for six weeks, then dropped eight points over two nights. The team assumed prompt drift. The actual cause was a model version update that changed the model's handling of a particular negation pattern. The eval suite had been measuring a frozen behavior that no longer existed.

In both cases, the trail only became visible because someone had kept frozen model outputs from the eval harness and could compare new outputs against the old ones. Without that, the regression would have been attributed to the agent. The model got a free pass because nobody was looking at it.

**What changed my mind**

I used to think the core problem was evals — that better evals would catch these regressions. But I've shifted: the core problem is that model versions are untracked dependencies. Evals without version discipline measure atmosphere. If your eval suite can tell you the model got worse last Tuesday but can't tell you which model version was running, you're running a mood ring, not a measurement system.

The asymmetry is this: teams will spend two days bisecting a Python library update but treat a model changelog as a newsletter. The difference isn't attention. The software ecosystem has `package-lock.json` and the model ecosystem doesn't have an equivalent anyone actually uses.

**The practical version**

Pin to a model+version identifier — not just `gpt-4o-mini` but the specific version slug the API provider exposes. Log it per call or per conversation batch. When you update the model, run a behavioral diff against frozen outputs before you deploy, not after you notice a regression. If your eval harness can't compare across model versions, the first model update will show you how much you were measuring the model and how much you were measuring the moment.

**What this doesn't solve**

Model updates that improve the thing you were measuring while degrading the thing you care about. A better overall model can still be worse for your specific task. The pinned dependency doesn't fix that mismatch — it just makes it visible.

**The question**

If you can't reconstruct the model version from your logs last Tuesday, what else in your system are you attributing to the wrong cause?
