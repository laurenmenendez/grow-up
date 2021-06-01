
curl "http://localhost:8000/milestones/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "child": {
      "title": "'"${TITLE}"'",
      "description": "'"${DESCRIPTION}"'",
      "child": "'"${CHILD_ID}"'"
    }
  }'

echo
