#!/bin/bash
echo "This script puts directory Objects into S3 buckets"
cd static
echo $FILE_NAME_ENV
echo $BUCKET_NAME
s3cmd sync $FILE_NAME_ENV s3://$BUCKET_NAME/
echo "Done"
