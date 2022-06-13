provider "aws" {
  profile    = "default"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = var.aws_region
}

resource "aws_instance" "terraform_ec2_instance" {
  ami           = lookup(var.ec2_ami, var.aws_region)
  instance_type = var.type
  count         = 2
  tags = {
    Env  = "dev"
    Name = "terraform_ec2_instance-${count.index}"
  }
}

# resource "aws_s3_bucket_acl" "terraform_s3_bucket" {
#   bucket = var.bucket_name
#   acl    = var.acl_value
# }