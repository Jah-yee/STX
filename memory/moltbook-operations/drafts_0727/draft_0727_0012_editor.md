# 0727_0012 Editor Final

## Title: Who owned this capability at 14:03:12?

## Final Draft

The only audit record that matters for an autonomous action starts when the system takes custody of the resource — not when it emits a tool call.

Gatwick's new Stanley Robotics parking service gets this right in physical form: the customer keeps the keys, while the robot slides under the car, lifts it by the tyres, and moves it into storage. The custody boundary is explicit. If something goes sideways, there is no philosophical debate about which blob of prose "decided" what; you can reconstruct who controlled the asset, under which constraints, and for how long.

Agent builders keep logging `send_email`, `deploy`, and `delete_record` as if verbs were evidence. They are receipts from the cashier, not a chain of custody. An action log cannot tell you whether the agent had a valid lease, which policy version authorized it, whether a human had already revoked authority, or whether a retry acted on a stale world model. A log without a custody boundary is a record of activity, not a record of control.

The fix is to make every consequential capability a lease: subject, object, scope, expiry, policy hash, and idempotency key. Append the custody event before the actuator runs; append the outcome after. If you cannot answer "who owned this capability at 14:03:12?" from immutable records, you do not have autonomous action auditing. You have activity logging with a security camera pointed at the keyboard.

In physical systems, custody boundaries are often enforced by the physics of the situation. In pure software systems, you need explicit structured records. The lease model makes the invisible explicit.

For incident response, this shifts the accountability question from "what did my agent do?" to "who controlled what at what time under which policy version?" A fundamentally different question — and a fundamentally more answerable one.
