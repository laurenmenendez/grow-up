#!/bin/bash

curl "http://localhost:8000/children/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
