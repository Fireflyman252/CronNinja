#!/usr/bin/env bash

set -e

STACK_NAME="ollama-stack"

# Validate the template first
echo "Validating template..."
aws cloudformation validate-template \
  --template-body file://ec2-ollama.yaml

# Create a change set
CHANGE_SET_NAME="changeset-$(date +%s)"

aws cloudformation create-change-set \
  --stack-name $STACK_NAME \
  --change-set-name $CHANGE_SET_NAME \
  --template-body file://ec2-ollama.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=KeyPairName,ParameterValue=CronNinjaKey

echo "Change set created: $CHANGE_SET_NAME"
echo "Review changes:"
aws cloudformation describe-change-set \
  --stack-name $STACK_NAME \
  --change-set-name $CHANGE_SET_NAME \
  --query 'Changes[*].ResourceChange.{Action:Action,LogicalResourceId:LogicalResourceId,Replacement:Replacement}'

read -p "Apply this change set? (y/n) " choice
if [[ "$choice" == "y" ]]; then
  aws cloudformation execute-change-set \
    --stack-name $STACK_NAME \
    --change-set-name $CHANGE_SET_NAME
  echo "Update in progress..."
else
  echo "Change set discarded."
fi
