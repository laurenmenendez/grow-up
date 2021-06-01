#!/bin/bash

curl "http://localhost:8000/children/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "child": {
      "name": "'"${NAME}"'",
      "age": "'"${AGE}"'"
    }
  }'

echo
