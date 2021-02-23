#!/bin/bash
echo "This script puts Objects into S3 buckets"
cd static
echo $FILE_NAME_ENV
echo $BUCKET_NAME
s3cmd put $FILE_NAME_ENV s3://$BUCKET_NAME
echo "Done"
