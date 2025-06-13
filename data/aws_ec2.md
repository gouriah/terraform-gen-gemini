resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe01e"
  instance_type = "t2.micro"
}