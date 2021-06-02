curl "http://localhost:8000/children/${CHILD_ID}/milestones/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
