resource "aws_instance" "flask" {
  ami             = "ami-0c55b159cbfafe1f0" # Ubuntu AMI in us-west-2
  instance_type   = var.instance_type
  key_name        = var.key_name
  subnet_id       = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "Flask-Backend"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install python3-pip -y
              pip3 install flask psycopg2
              # Add commands to run your Flask app (e.g., from GitHub)
              EOF
}

resource "aws_instance" "react" {
  ami             = "ami-0c55b159cbfafe1f0" 
  instance_type   = var.instance_type
  key_name        = var.key_name
  subnet_id       = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "React-Frontend"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install nodejs npm -y
              # Add commands to run your React app (e.g., from GitHub)
              EOF
}

resource "aws_instance" "rust" {
  ami             = "ami-0c55b159cbfafe1f0" 
  instance_type   = var.instance_type
  key_name        = var.key_name
  subnet_id       = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "Rust-Backend"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install rustc cargo -y
              # Add commands to run your Rust app
              EOF
}
