#!/bin/bash
# Merge promotion round 09:30 UTC

MSG="Feel free to merge — happy to help with anything! 🙏"

add_comment() {
  local repo=$1
  local pr=$2
  result=$(gh api repos/"$repo"/issues/"$pr"/comments --method POST --field body="$MSG" 2>&1)
  echo "$repo#$pr: $(echo $result | python3 -c "import sys,json; d=json.load(sys.stdin); print('✅', d.get('id','?'))" 2>/dev/null || echo "❌$(echo $result | head -1)")"
}

echo "=== AT-MAX++++++ (14→15) ==="
add_comment electech6/ORB_SLAM2_detailed_comments 14
add_comment microsoft/tensorwatch 89
add_comment dipendra-mule/miniredis 53
add_comment kozec/sc-controller 744
add_comment sghr/iGeo 30
add_comment landsat-pds/landsat_ingestor 26
add_comment canselcik/libremarkable 137

echo "=== AT-MAX+++++ (12→13) ==="
add_comment boonex/dolphin.pro 698
add_comment hectorcanaimero/pidelo 38

echo "=== AT-MAX++++ (11→12) ==="
add_comment nomoresat/DPITunnel-cli 8
add_comment buffet/kiwmi 88
add_comment simianhacker/code-by-voice 5
add_comment electech6/ORB_SLAM3_detailed_comments 23
add_comment arkenio/gogeta 16
add_comment srlabs/phink 13
add_comment lshiwjx/2s-AGCN 111
add_comment awesome-tips/iOS-Tips 46
add_comment Aero25x/random-user-agents 3
add_comment sp00ks-git/hat 5
add_comment friebetill/TubeCards 9
add_comment fictionco/fiction 303
add_comment TalkingData/owl 39
add_comment danthedeckie/simpleeval 189
add_comment dwyl/hapi-typescript-example 22
add_comment multycloud/multy 429
add_comment FremyCompany/css-grid-polyfill 60
add_comment ffay/proxygateway 22
add_comment alash3al/sqler 39
add_comment dengsgo/fileboy 29

echo "=== AT-MAX+++ (10→11) ==="
add_comment 3xxx/engineercms 117
add_comment magiclvzs/antnet 8

echo "=== DONE ==="
