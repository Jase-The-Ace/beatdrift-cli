resource "aws_instance" "Count" {
  ami           = "ami-033594f8862b03bb2"
  instance_type = "t2.micro"
  key_name = "key342"

  tags = {
    Name = "Webappli"
  }
}