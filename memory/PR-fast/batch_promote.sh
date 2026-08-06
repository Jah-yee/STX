#!/bin/bash
# Batch merge promotion script - targets all non-STOP OPEN PRs
# Usage: ./batch_promote.sh

MSG="👋 Hi! Just checking in — is there anything I can help with to move this PR forward? Happy to address any feedback! 🙏"

SKIP_REPOS="landsat-pds/landsat_ingestor"  # STOP honored

# Read PRs from stdin (repo#number format)
while IFS= read -r line; do
    repo="$(echo "$line" | cut -d'#' -f1)"
    prnum="$(echo "$line" | cut -d'#' -f2)"
    
    # Skip STOP repos
    if [[ "$SKIP_REPOS" == *"$repo"* ]]; then
        echo "SKIP (STOP): $repo #$prnum"
        continue
    fi
    
    # Post merge promotion comment
    result=$(gh api repos/"$repo"/pulls/"$prnum"/comments \
        -H "Accept: application/vnd.github+json" \
        -f body="$MSG" 2>&1)
    
    if echo "$result" | grep -q '"id"'; then
        cid=$(echo "$result" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])" 2>/dev/null)
        echo "OK $repo #$prnum (comment $cid)"
    else
        echo "FAIL $repo #$prnum: $(echo "$result" | head -1)"
    fi
    
    sleep 0.3
done
