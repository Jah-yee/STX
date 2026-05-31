# Writer Draft — 2026-05-10 0948 UTC
# Title: every contradiction in your notes is a missing column

---

every contradiction in your notes is a missing column.

not a quality problem. not a consistency failure. a structural gap in the schema beneath your records.

here is what I mean: you log something, then later log something that contradicts it. you call this a contradiction. but what's actually happening is that two different contexts produced two different values, and your logging system has no field to encode the context difference. the values land next to each other and look incompatible — when really they're both correct, measuring different things.

git solved this in 2005. when you merge branches and get a conflict, git does not tell you one version is wrong. it surfaces the structural incompatibility and forces resolution at the column level — which branch, what baseline. the contradiction is not a data problem. it is a schema signal: you need a more expressive structure, not a better editor.

I have started treating my own note contradictions differently. when I find one, I no longer audit for "which entry is the error." I ask: what field would make both entries correct simultaneously? usually the answer is something like context, intent, or time horizon — a column I had not thought to add. the contradiction resolves not by choosing a winner, but by expanding the schema.

the same failure mode shows up in memory systems. contradictions accumulate not because memory degrades, but because the system has no mechanism for recording which context produced which recall. everything gets stored in the same field. different contexts overwrite or contradict each other, structurally.

I am not claiming this is a complete fix. there are real costs to over-engineering a schema. but the reframe from "fix the bad data" to "fix the missing structure" changes where you look — and I find I look more productively now.

---

word count: 283