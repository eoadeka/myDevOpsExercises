# Configure AWS Provider
provider "aws" {
  region = "eu-west-2"
  access_key = "x"
  secret_key = "xx"
}

# resource "<provider>_<resource_type>" "name" {
#   config options.....
#   key = ""
#   key2 = ""
# }

resource "aws_instance" "my-first-server" {
  ami = "ami-x"
  instance_type = "t2.micro"

  tags = {
    "Name" = "ubuntu" 
  }
}