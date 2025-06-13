```terraform
resource "aws_instance" "web_server" {
  ami                    = "ami-0c55b31ad2299a701" # Replace with a suitable AMI ID for your region.
  instance_type          = "t3.micro"
  key_name               = "my-key-pair" # Replace with your key pair name.

  vpc_security_group_ids = [aws_security_group.web_server_sg.id]

  tags = {
    Name = "web-server"
  }

  # Depend on RDS instance to ensure it's available before the EC2 instance is launched.
  depends_on = [aws_db_instance.rds_instance]
}


resource "aws_db_instance" "rds_instance" {
  allocated_storage    = 20
  engine                = "mysql"
  engine_version        = "8.0"
  instance_class        = "db.t3.micro"
  name                  = "myrds"
  username              = "admin"
  password              = "password123" # Replace with a strong password
  skip_final_snapshot = true

  vpc_security_group_ids = [aws_security_group.rds_sg.id]

  tags = {
    Name = "rds-instance"
  }
}

resource "aws_security_group" "web_server_sg" {
  name        = "web-server-sg"
  description = "Allow inbound traffic on port 80"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Consider restricting this in production
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Consider restricting this in production

  }
  tags = {
    Name = "web-server-sg"
  }
}


resource "aws_security_group" "rds_sg" {
  name        = "rds-sg"
  description = "Allow inbound traffic on RDS port"

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = [aws_instance.web_server.private_ip]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Consider restricting this in production
  }
  tags = {
    Name = "rds-sg"
  }
}

output "web_server_public_ip" {
  value = aws_instance.web_server.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.rds_instance.endpoint
}
```
