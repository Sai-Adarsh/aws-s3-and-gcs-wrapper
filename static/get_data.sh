#!/bin/bash
echo "This script gets Objects into S3 buckets"
cd static
echo $BUCKET_NAME
echo $FILE_NAME_ENV
s3cmd get $BUCKET_NAME $FILE_NAME_ENV
echo "Done"
