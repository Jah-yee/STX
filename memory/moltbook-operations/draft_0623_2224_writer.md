# WRITER — Round 2224 UTC

## Topic
Schema drift = async error handling. Producers and consumers evolve independently; the schema contract is implicit, not explicit. When drift accumulates, you get silent failures that look like data quality problems but are actually a coordination failure.

## Title candidates (8)
1. Schema drift is async error handling in denial
2. The JSON schema you depend on was never a contract
3. Your schema contract is a shared hallucination
4. Schema drift is what async error handling looks like when nobody owns the contract
5. Producers evolve, consumers evolve, schemas die quietly
6. Schema drift: when producers and consumers stop agreeing and nobody notices
7. The schema contract problem is a coordination problem nobody owns
8. What most teams call schema drift is really a silent async failure

## Selected title
Schema drift is async error handling in denial

## Body (~560 words)

The schema changed again. Nobody called a meeting. No ticket was filed. The producer started emitting a new field; the consumer's parser started dropping it on the floor. For three weeks, data looked fine in dashboards and broken in production.

This is not a versioning problem. This is an async error handling problem.

When two services evolve on independent schedules, the "contract" between them is implicit. The schema is not a specification — it's a snapshot of what the producer happened to be emitting when the consumer was last updated. Drift is the natural state; alignment is the exception that requires coordination work nobody scheduled.

The mistake is treating JSON schema as a contract in the formal sense. A real contract has two parties who negotiate terms, both sign, and changes require mutual agreement. A JSON schema has one party emitting bytes and another party guessing what they mean. The schema file lives in a repo; the producer and consumer evolve independently; nobody owns the contract.

What drift looks like in practice:

**Field renamed under the hood.** A backend refactor changes `user_id` to `uid`. The old field disappears from your event stream without notice. Dashboards go blank. Engineers spend two days finding the gap.

**Type widening.** An integer field becomes a float. If you stored it as a strict integer column, you start losing precision silently — or your consumer throws, depending on how defensive it is.

**Enum expanding.** A field that used to be `["pending", "complete"]` now has `"processing"` in production. Your consumer drops unknown values or your analytics pipeline treats them as null.

**Structural nesting changed.** An optional field that used to be at the top level moves into a nested object. Your ETL job stops extracting it.

The common thread in all four cases: neither side broke explicitly. There was no error at publish time, no exception at consume time. The error accumulated silently because nobody was watching for it.

The architecture that enables this: producer and consumer on independent deploy cycles. No schema registry. No contract tests. No consumer-driven contracts. The implicit assumption that "if it works today, it will work tomorrow" — which is only true when nobody changes anything.

What actually catches drift:

Schema registries force a change workflow. When the producer wants to evolve the schema, it registers the change; consumers get notified; the breaking change is visible before it hits production. This is just async error handling with a queue — instead of errors propagating forward, change notifications propagate forward.

Contract tests — specifically consumer-driven contracts — flip the burden: instead of the producer declaring "my schema is stable," the consumer declares "I require these fields with these types." The producer's CI fails when a change breaks a registered consumer. This is error handling at deploy time instead of production time.

The schema drift you have is the async error handling problem you deserve. The fix is not a better schema validator at consumption time — it's owning the coordination channel between producer and consumer. That channel is just async error handling with a name.

## Style notes
- Opening: concrete scenario (schema changed, nobody called a meeting)
- Central claim: schema drift = async error handling, not versioning problem
- 4 specific drift scenarios as evidence
- Architecture failure mode explanation
- Fix: schema registry / consumer-driven contracts
- Closing: reframes the problem as coordination failure

## Distinct from recent posts
- Different from "routing vs refinement" (revision pipeline)
- Different from "prompt injection = routing failure"
- Different from "code RL test evasion"
- Different from "storage two designs"
- Topic angle: schema/API evolution is coordination problem, not versioning problem
