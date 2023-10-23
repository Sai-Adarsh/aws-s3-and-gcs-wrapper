## AWS S3 and GCS Wrapper
This repository contains code that helps you build a web service to upload and download files from an S3 bucket and Google Cloud Storage. It also assists you in deploying it to the cloud as a Function as a Service (FaaS). Take a look at [setup.md](https://github.com/Sai-Adarsh/aws-s3-and-gcs-wrapper/blob/master/docs/setup.md) to learn how to set up this project. You can also communicate with multiple SDKs to perform the same job, i.e., AWS S3 and Google Cloud Storage.

### Functions

**POST** - PUT files
```
curl -X POST /put_data -F "file=@sample.png" -F "bucket_name=mtx-appendly-test"
```
**POST** - PUT folders
```
curl -X POST /put_dir -F "file=folder_1" -F "bucket_name=mtx-appendly-test"
```
**POST** - GET files
```
curl -X POST /get_data -F "file=@sample.png" -F "bucket_name=mtx-appendly-test
```
**POST** - GET folders
```
curl -X POST /get_dir -F "bucket_name=mtx-appendly-test/folder_1"
```
**POST** - Switch Config between AWS and GCP
```
curl -X POST /switch_config -F "base=AWS"
```
**POST** - List all buckets
```
curl -X POST /list_buckets
```

You can also import the provided Postman Collection to quickly inspect the exposed endpoints. Additionally, ensure that you fill up the `access_key` and `secret_key` environment variables to enable interaction with the deployed API.
