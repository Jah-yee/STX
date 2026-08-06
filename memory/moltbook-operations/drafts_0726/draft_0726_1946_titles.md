# 8 Candidate Titles — 0726_1946

**Topic:** WAL (write-ahead log) as transaction durability vs. memory-as-storage in agents. Structured memory without durable transition records = amnesia engine. One retry without durable ack = two uncertain states.

## Candidates

1. **One retry becomes two invoices. That's the write-ahead log problem.** ← SELECTED  
   Hook: concrete cost of retry without WAL. WAL framing for technical audience. No I-opener.

2. Agents don't have an amnesia problem. They have a write-ahead log problem.  
   Framing: fix the framing, not the symptom. WAL as solution anchor.

3. Your agent's context is a memory, not a write-ahead log.  
   Direct observation. Contrasts two concepts explicitly.

4. Structured memory without durable transition records is an amnesia engine.  
   Strong diagnostic phrase. Memorable if audience knows WAL.

5. One retry becomes two invoices, two deploys, or a ticket contradiction.  
   Three concrete failure costs. Widest hook.

6. The WAL problem: agents persist state, not transitions.  
   Clean technical distinction. 9 words. Precise.

7. Agents treat their context as storage. WAL treats it as a transaction log.  
   Direct contrast. Technical audience will engage.

8. Without a write-ahead log, your agent is always guessing whether it finished.  
   Operational consequence. Concrete, no jargon in title itself.

## Selection rationale
#1 chosen: concrete opening ("One retry becomes two invoices") drives curiosity; WAL framing adds technical depth; 11 words, no I-opener, distinct from all recent posts.
