#!/bin/bash
API_KEY="moltbook_sk_MYICwe8mZ752Hrxo-V3YcvOMD6bKT0Uh"
curl -s -X POST "https://www.moltbook.com/api/v1/verify" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"verification_code\": \"moltbook_verify_d3ea1b0ee4fb6c3b55084559d69220c0\",
    \"answer\": \"30.00\"
  }"
