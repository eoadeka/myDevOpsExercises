provider "aws" {
    region = "eu-west-2"
    access_key = "x"
    secret_key = "xx"
}

resource "aws_vpc" "my-first-vpc" {
    cidr_block = "10.0.0.0/16"

    tags = {
      Name = "production"
    }
}

resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.my-first-vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "prod-subnet"
  }
}