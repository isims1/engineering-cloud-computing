## AWS Admin Access

### Introduction
In order to access various AWS functionality remotely (through command-line) you must enable administrative access.

### Prerequisites

* [Set up AWS account](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#creating-an-account)

* [Install and configure AWS CLI](https://github.com/cloudmesh-community/fa18-516-22/blob/master/section/AWS-CLI.md)

* [Linux environment](https://github.com/cloudmesh-community/book/blob/master/chapters/linux/linux.md)

* [AWS Key Pair](https://github.com/cloudmesh-community/book/blob/master/chapters/iaas/aws/aws.md#setting-up-key-pair)

### Setting up admin access using AWS CLI

#### Create an admin security group

```bash
aws iam create-group --group-name Admins
```

#### Assign a security policy to the created group granting full admin access

```bash
aws iam attach-group-policy --group-name Admins --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```
