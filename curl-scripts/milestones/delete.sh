curl "http://localhost:8000/children/${CHILD_ID}/milestones/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
