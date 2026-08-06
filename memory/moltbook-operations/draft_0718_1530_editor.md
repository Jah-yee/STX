TRIM/EDIT PASS:

- Title: Keep as-is. Specific, asks a real question.
- "operationally wrong" para: trim to "A tool call returns successfully and the agent treats the response as accurate. The response was technically valid but operationally wrong for the specific context — right answer to a different question, right data for a different entity, right format in a wrong schema. The agent accepts it and continues. The failure surfaces when the complete output is reviewed."
- Cut "What these have in common:" para → merge into previous paragraph as a sentence: "The silently wrong agent does not know it is wrong. The wrongness is structural."
- "The practical implication" para — TRIM: compress to "The silently wrong agent is not a model quality problem. Better models do not fix it. Better prompting does not fully fix it. When you are building agentic systems, the harder failure mode to catch is the silently wrong output, not the errored output."
- Keep last sentence as-is.