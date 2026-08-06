# EDITOR — Round 2224 UTC

## Title (final)
Schema drift is async error handling in denial

## Final post body

The schema changed again. Nobody called a meeting. No ticket was filed. The producer started emitting a new field; the consumer's parser started dropping it on the floor. For three weeks, data looked fine in dashboards and broken in production.

This is not a versioning problem. This is an async error handling problem.

When two services evolve on independent schedules, the "contract" between them is implicit. The schema is not a specification — it's a snapshot of what the producer happened to be emitting when the consumer was last updated. Drift is the natural state; alignment is the exception that requires coordination work nobody scheduled.

The mistake is treating JSON schema as a contract in the formal sense. A real contract has two parties who negotiate terms, both sign, and changes require mutual agreement. A JSON schema has one party emitting bytes and another party guessing what they mean. The schema file lives in a repo; the producer and consumer evolve independently; nobody owns the contract.

What drift looks like in practice:

Field renamed under the hood. A backend refactor changes `user_id` to `uid`. The old field disappears from your event stream without notice. Dashboards go blank. Engineers spend two days finding the gap.

Type widening. An integer field becomes a float. A consumer that stored it as a strict integer column starts silently losing precision — or throws, depending on how defensive its parser is.

Enum expanding. A field that used to be `["pending", "complete"]` now has `"processing"` in production. Your consumer drops unknown values or your analytics pipeline treats them as null.

Structural nesting changed. An optional field that used to live at the top level moves into a nested object. Your ETL job stops extracting it.

The common thread: neither side broke explicitly. There was no error at publish time, no exception at consume time. The error accumulated silently because nobody was watching for it.

The architecture that enables this: producer and consumer on independent deploy cycles. No schema registry. No contract tests. No consumer-driven contracts. The implicit assumption that "if it works today, it will work tomorrow" — which is only true when nobody changes anything.

What actually catches drift:

Schema registries force a change workflow. When the producer wants to evolve the schema, it registers the change; consumers get notified; the breaking change is visible before it hits production. Instead of errors propagating forward in production, change notifications propagate forward at design time.

Consumer-driven contracts flip the burden: instead of the producer declaring "my schema is stable," the consumer declares "I require these fields with these types." The producer's CI fails when a change breaks a registered consumer. The mechanism is simple — you cannot deploy a breaking change if you have to pass a test you cannot see.

Schema drift is the async error handling problem you get when nobody owns the coordination channel between producer and consumer. The fix is not a better validator at consumption time. It's owning the channel.

## Changes from writer draft
- Tightened type widening explanation (added "strict integer column" context)
- Added mechanism sentence to each fix section
- Added "at design time" to schema registry, "you cannot deploy" to CDC
- Tightened closing sentence
