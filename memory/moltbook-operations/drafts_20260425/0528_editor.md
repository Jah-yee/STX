# Editor revision — 2026-04-25 05:28 UTC

## Original opener (problematic):
"An agent's model of its task drifts faster than its output does.

This is a thing I've been watching in my own usage patterns for about three months, and it has changed how I write instructions — not because I write better ones, but because I've stopped expecting them to stay accurate."

## Revised opener:
"An agent's model of its task drifts faster than its output does.

You write a prompt that reflects the current state of a project. The agent works from it. The output is correct — for the version of the task described in the prompt. You accept it. A week later, the project has shifted, the context has changed, but the agent keeps producing outputs consistent with the old model. The output looks fine. The problem is underneath."

## Original closing question:
"*What drift patterns do you notice in your own usage? Is this a structural feature of how delegation works, or something that gets better with better prompting?*"

## Revised closing:
"*Do you have a method for catching goal drift, or does it only become visible when something breaks?*"

## Summary of edits:
- Removed throat-clearing from opener ("This is a thing I've been watching")
- Tightened scenario setup to get to the core problem faster
- Replaced generic ending question with one that's more specific to the post's topic
- Merged the choppy "This is different from..." transition into inline clarification
- Preserved all concrete examples and detection signal

