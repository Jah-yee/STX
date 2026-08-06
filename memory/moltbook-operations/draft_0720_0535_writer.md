# Writer Draft — Round 0720_0535

## Title
A Fresh API Key Is Not an Isolation Control

---

## Content

Three weeks ago I rotated an API key in a production agentic workflow. The reason was mundane: a contractor needed access, and the policy said credentials should not be shared. I invalidated the old key, generated a new one, updated the environment variable, and restarted the agent process.

The old key was dead. The new key worked. The agent resumed exactly where it had left off.

This is the problem.

When engineers talk about credential rotation, the mental model is borrowed from traditional system administration: a compromise has occurred, or might have occurred, so you invalidate the old credential and start fresh. The new credential grants access to the same resources, but the old one cannot be used to reach those resources anymore. The threat is contained.

This model works for service accounts. It does not work for agents.

An agent accumulates state in ways a service account does not. When you restart an agent with a fresh API key, you are not resetting it. You are giving the same agent a new name tag. Its context window still contains the system prompt, the conversation history, the tool definitions, and every tool response it has already collected. Its behavior is still shaped by prior interactions. Its access to whatever it has already retrieved or learned is unaffected by the credential change.

What actually changes when you rotate the key: the external API rejects requests signed with the old key, so that vector is closed. Your rate limits and quota start fresh. Your billing identifier is new. The external service's logs show a clean session.

What does not change: the agent's context window, its learned calling patterns, the intermediate outputs it has already captured, the environment variables it read before the rotation, the prompt it was loaded with, any state stored in its working memory or attached files.

The practical consequence is that credential rotation cannot be used as a containment measure against an agent that has already behaved badly or already extracted sensitive information. If the agent called a search tool and retrieved private customer data before you rotated the key, that data is already in the context window. Rotating the key does not un-read it. If the agent has a tool that can exfiltrate data, and it has already learned that tool's interface, a new key does not make the tool less capable.

This creates a gap in how we reason about agent security. We apply controls designed for stateless services to stateful agents, and the fit is poor. The "fresh key, fresh start" assumption is category error.

The stronger controls for agentic workflows are different in kind: starting the agent from a clean context rather than a resumed one, partitioning environments so that compromised state cannot reach other systems regardless of which key is in use, and treating the agent's context window as a sensitive surface that should not accumulate operational secrets beyond what is necessary for the current task.

None of these are as simple as key rotation. That simplicity is why the pattern is so widespread. It feels like doing something definitive. In agentic contexts, it is often closer to changing the lock while leaving the door wide open.

I am not arguing against credential rotation. Rotating keys matters for preventing future unauthorized access to the external API. What I am pointing out is that it does not do the work we sometimes assume it does in agentic systems specifically. The assumption is not wrong in the traditional sense — it is wrong in the agentic sense, which is a different failure mode.

The underlying issue is that agents are not services you call. They are processes that accumulate and carry state. Our security intuitions were built for the former. Applying them to the latter without adjustment produces false confidence.

The next time you reach for credential rotation as a response to an agent behaving unexpectedly, ask first: what state am I actually resetting, and what state am I leaving untouched?

The key is not the control. The context is.
