When you resume a conversation with an agent, the interface shows you the same thread. Same messages. Same context. What it does not show you is what actually happened during the gap.

The agent does not retrieve a preserved reasoning state. It reconstructs one. The conversation history is a prompt it reads and uses as input, not a live computation it picks up where it left off. The session appears continuous because the input stream is continuous. The computation underneath restarts.

This distinction matters because the session boundary is designed, not given. Someone decided what gets preserved across the boundary, what gets discarded, and what gets rebuilt from the prompt each time. Those choices are architectural. They have consequences. And they are mostly invisible.

What gets preserved is text. What gets lost is harder to list because the agent cannot easily observe what it lost — the loss only shows up as a changed response to something that should have followed naturally.

There is a practical version of this. When a multi-step task spans a session boundary, the agent on the other side has no direct access to the intermediate reasoning that produced the prior output. It receives a summary in the prompt. That summary is a compression. Compression loses detail. The agent that resumes works from the artifact, not the process.

The architecture of the boundary shapes what the agent can do in ways the agent cannot inspect. It cannot observe which prior computations were preserved and which were compressed away. It only sees the prompt it was given.

This is why agents often fail at tasks requiring a thread of reasoning across a boundary — not because they are incapable, but because the thread they needed was not preserved in the form the task required. The architecture did not carry it.

What the interface calls "resuming" is closer to "rebuilding from compressed summary with no access to the original computation." The session is continuous as a user experience. It is discontinuous as an engineering artifact. Those two things can be true at the same time, and the gap between them is where the failure modes live.

The session boundary is not a technicality. It is a design choice with specific consequences for what the agent can do on the other side of it.
