#!/usr/bin/env bash

set -e

STACK_NAME="ollama-stack"

aws cloudformation create-stack \
  --stack-name $STACK_NAME \
  --template-body file://ec2-ollama.yaml \
  --capabilities CAPABILITY_NAMED_IAM

echo "Stack creation initiated. Use 'describe-stacks' to check status:"
echo "aws cloudformation describe-stacks --stack-name $STACK_NAME"
