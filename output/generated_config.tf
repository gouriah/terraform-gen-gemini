```terraform
resource "aws_instance" "example" {
  ami           = "ami-0c55b31ad2299a701" # Replace with a valid AMI ID for your region
  instance_type = "t2.micro"

  tags = {
    Name = "example"
  }
}
```
