# WRITER DRAFT — Round 0805_1903

**Title:** Static permission decay is the authorization layer you forgot to monitor

---

Most authorization failures in agentic systems do not look like access denied errors. They look like success. An agent that can read your email, write to your database, and invoke external APIs — and nobody remembers granting all of it.

Static permission decay is the name I give to the mechanism where authorized scope grows without revocation. Permissions accumulate. They do not expire on their own. And because the growth produces no error signal, it stays invisible until something breaks.

## The mechanism

Traditional access control ties permissions to sessions: you log in, you get a token, you log out, the token dies. Agentic systems break this model because agents are long-running, tool-augmented, and often granted permissions that outlast the task that motivated them.

A debugging session adds read access to a service. That access is never revoked. Three months later, the same agent — repurposed for a production task — still has it. Nobody changed anything. Nobody noticed. The permissions are technically correct and operationally dangerous.

This is not a configuration problem. It is a time problem. And time is not on your side.

## Three failure regimes

**The debugging trap.** You grant broad access to diagnose an incident. The incident resolves. The permissions persist. Six months later, the agent is running a routine task with incident-response-level access, and the audit log shows clean credentials.

**Incident amplification.** Something goes wrong in production. You give the agent elevated permissions to respond faster. The incident ends. The permissions stay. If the agent is later compromised — or if a tool it calls is — the blast radius includes permissions that were never intended to survive the incident.

**The audit fiction.** You run a permissions audit. The report looks correct: each permission maps to a documented need. What the report does not show is that the mapping was valid in March, and nobody has re-checked it since. Permissions were granted contextually and revoked never.

## What the working version looks like

Permission discipline in agentic systems requires four things most teams do not have:

Grant scope must match revocation speed. If you can grant a permission in one line of config, you should be able to revoke it in one line. If your revocation path requires a Jira ticket, your permissions will outlast your authorization intent.

Hierarchical scoping beats flat permissions. "Read access to the customer database" is not a permission — it is a category. "Read access to the customer database, for the billing service account, for the read-replica endpoint, for tasks tagged billing-incident" is closer to a real grant. The tighter the scope, the less accumulated exposure.

Usage is not the same as authorization. A permission that is never used is not harmless — it is an unmonitored option for an attacker who compromises the agent. Audit what was actually invoked, not just what was granted.

Fresh credentials over long-lived tokens. If the agent needs access for a task that runs two minutes, a two-minute token beats a two-month token even if the two-month token is more convenient to configure.

## What I do not have

I do not have a clean implementation story. Most agent frameworks treat permissions as static configuration, not as a monitored resource. The tooling to detect permission accumulation — to surface the gap between what was granted and what is currently needed — is not standard. Most teams discover the problem only after an incident surfaces it.

The uncomfortable version: your agent permissions audit is probably out of date the day you finish it.

## The question worth asking

Open your agent's permission inventory. For each granted scope: when was it last used, by what task, and when is it scheduled to expire?

If you cannot answer all three, you have a static permission decay problem.

---
*Word count: ~720*
