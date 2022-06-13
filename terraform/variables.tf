variable "aws_access_key" {
  default = "AKIAZIZACOCZEMU6SOVS"
}
variable "aws_secret_key" {
  default = "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"
}
variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "ec2_ami" {
  type = map(any)

  default = {
    us-east-1 = "ami-09d56f8956ab235b3"
  }
}

variable "type" {
  type        = string
  description = "Instance type for the EC2 instance by Terraform"
  default     = "t2.micro"
  sensitive   = true
}

# variable "bucket_name" {
#   default = "terrform-s3-bucket"
# }

# variable "acl_value" {
#   default = "private"
# }
