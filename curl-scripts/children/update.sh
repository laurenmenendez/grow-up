
curl "http://localhost:8000/children/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "child": {
      "name": "'"${NAME}"'",
      "age": "'"${AGE}"'"
    }
  }'

echo
