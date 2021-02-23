#!/bin/bash
echo "This script gets directory objects into S3 buckets"
cd static
echo $BUCKET_NAME
s3cmd get --recursive $BUCKET_NAME
echo "Done"
