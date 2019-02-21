## AWS Command Line Interface (CLI)

### Introduction

Amazon's CLI allows for programatic interaction with AWS product through the command line. CLI provide many pre-built functions that allow for interaction with Amazon's Elastic Compute Cloud (EC2) instances and S3 storage.

### Prerequisites
* [Linux](https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md)
* [Python](https://github.com/cloudmesh-community/book/blob/master/chapters/prg/python/python-install.md)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [AWS Account](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#creating-an-account)
* [AWS Key Pair](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#setting-up-key-pair)

#### Install CLI
Run the follwoing code to install CLI.

```bash
pip install awscli
```

#### Configure CLI
Using the following code to configure AWS using. You will need to specify four parameters:

1. AWS Access Key ID
2. AWS Secret Access Key
3. Default region name (this is the default region that will be used when you create EC2 instances)
4. Default output format (the default format is json)

```bash
aws configure
```



