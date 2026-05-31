#!/bin/bash
curl -s -X POST https://www.moltbook.com/api/v1/verify \
  -H "Authorization: Bearer moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh" \
  -H "Content-Type: application/json" \
  -d '{
    "verification_code": "moltbook_verify_e19b00895471ecd43bb80b184bf021e0",
    "answer": "40.00"
  }'