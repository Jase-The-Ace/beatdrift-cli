terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16.0"
    }
  }

  required_version = ">= 0.14.9"
}

#Provider profile and region in which all the resources will create
provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

#Resource to create s3 bucket
resource "aws_s3_bucket" "demo-bucket"{
  bucket = ""

  tags = {
    Name = "S3Bucket"
  }
}