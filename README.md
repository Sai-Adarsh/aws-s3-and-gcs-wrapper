<p align="center">
  <img src="docs/img/banner.png">
</p>

### Description
This repository contains code that helps you build a web service to upload and download files to S3 buckets and helps you deploy it to cloud as FaaS .i.e., Wrapper API for AWS S3 and Google Cloud Storage. Take a look at [setup.md](https://github.com/Sai-Adarsh/mtx-hacks/blob/master/docs/setup.md) to learn how to setup this project. You can also communicate with multiple SDKs to perform the same jobs .i.e., **AWS S3** and **Googe Cloud Storage**.

### Functions

- **POST** - PUT files
    - `curl -X POST http://localhost:5000/put_data -F "file=@sample.png" -F "bucket_name=mtx-appendly-test"`
- **POST** - PUT folders
    -  `curl -X POST http://localhost:5000/put_dir -F "file=folder_1" -F "bucket_name=mtx-appendly-test"`
- **POST** - GET files
    -  `curl -X POST http://localhost:5000/get_data -F "file=@sample.png" -F "bucket_name=mtx-appendly-test`
- **POST** - GET folders
    -  `curl -X POST http://localhost:5000/get_dir -F "bucket_name=mtx-appendly-test/folder_1"`
- **POST** - Switch Config between AWS and GCP
    -  `curl -X POST http://localhost:5000/switch_config -F "base=AWS"`
- **POST** - List all buckets
    -  `curl -X POST http://localhost:5000/list_buckets`

You can also import the provided Postman Collection to take a quick look at the exposed endpoints. Also make sure to fill up `access_key` and `secret_key` environment variables to make endpoints intract with the deployed API.

**Screenshots**<br />
<img src="docs/img/one.png" height=520 width =270 />
<img src="docs/img/two.png" height=520 width =270 />
<img src="docs/img/three.png" height=520 width =270 />

### Architecture

<p align="center">
  <img src="docs/img/arch.png">
</p>
