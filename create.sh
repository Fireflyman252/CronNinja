#!/usr/bin/env bash

set -e

# STACK_NAME="cronninja-stack"
# BUCKET_NAME="${STACK_NAME}-templates"
BUCKET_NAME="cronninja-stack-templates"
REGION="us-east-1"
#
if ! aws s3api head-bucket --bucket "$BUCKET_NAME" 2>/dev/null; then
  echo "Creating S3 bucket: $BUCKET_NAME"
  aws s3api create-bucket \
    --bucket "$BUCKET_NAME" \
    --region "$REGION"

  aws s3api put-public-access-block \
    --bucket "$BUCKET_NAME" \
    --public-access-block-configuration \
      BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false

  aws s3api put-bucket-policy \
    --bucket "$BUCKET_NAME" \
    --policy file://s3-bucket-policy.json

fi

echo "Uploading templates..."
for file in ./*.yaml; do
  aws s3 cp "$file" "s3://$BUCKET_NAME/$(basename "$file")"
done
aws s3 cp "Dockerfile" "s3://$BUCKET_NAME/Dockerfile"
aws s3 cp "./app.py" "s3://$BUCKET_NAME/app.py"

aws cloudformation create-stack \
  --stack-name cronninja-stack \
  --template-body file://main.yaml \
  --parameters ParameterKey=KeyPairName,ParameterValue=CronNinjaKey \
  --capabilities CAPABILITY_NAMED_IAM

# Get the IP address of EC2
while true; do

  EC2_PUBLIC_IP=$(aws cloudformation describe-stacks \
    --stack-name cronninja-stack \
    --query "Stacks[0].Outputs[?OutputKey=='EC2InstancePublicIP'].OutputValue" \
    --output text)

  if [[ -n "$EC2_PUBLIC_IP" && "$EC2_PUBLIC_IP" != "None" ]]; then
    echo "Public IP: $EC2_PUBLIC_IP"
    break
  fi

  echo "Still waiting for IP... retrying in 10 seconds."
  sleep 10
done

scp -i ./CronNinjaKey.pem -o StrictHostKeyChecking=no ./app.py ubuntu@${EC2_PUBLIC_IP}:/home/ubuntu/
scp -i ./CronNinjaKey.pem -o StrictHostKeyChecking=no ./ec2-init.sh ubuntu@${EC2_PUBLIC_IP}:/home/ubuntu/
ssh -i ./CronNinjaKey.pem -o StrictHostKeyChecking=no ubuntu@"$EC2_PUBLIC_IP" "chmod +x ./ec2-init.sh && sudo ./ec2-init.sh"

echo "EC2 IP: $EC2_PUBLIC_IP"
