#!/bin/bash
# Usage: ./upload.sh <local_file> <bucket_name> <expiration_seconds>
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <local_file> <bucket_name> <expiration_seconds>"
    exit 1
fi

LOCAL_FILE=$1
BUCKET=$2
EXPIRATION=$3

aws s3 cp "$LOCAL_FILE" s3://"$BUCKET"/
aws s3 presign s3://"$BUCKET"/"$LOCAL_FILE" --expires-in "$EXPIRATION"
