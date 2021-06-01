#!/bin/bash

curl "http://localhost:8000/children/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
