#!/usr/bin/env bash
set -e

STACK_NAME="cronninja-stack"

read -p "Are you sure you want to delete the stack '$STACK_NAME'? This cannot be undone. (y/n) " choice
if [[ "$choice" == "y" ]]; then
  aws cloudformation delete-stack --stack-name $STACK_NAME
  echo "Delete initiated. Use 'describe-stacks' to check status."
else
  echo "Delete aborted."
fi
