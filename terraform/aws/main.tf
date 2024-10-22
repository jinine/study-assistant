provider "aws" {
  region = var.region
}

module "vpc" {
  source = "./vpc.tf"
}

module "rds" {
  source = "./rds.tf"
}

module "ec2_instances" {
  source = "./ec2_instances.tf"
}

output "flask_public_ip" {
  value = aws_instance.flask.public_ip
}

output "react_public_ip" {
  value = aws_instance.react.public_ip
}

output "rust_public_ip" {
  value = aws_instance.rust.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
