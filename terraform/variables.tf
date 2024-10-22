variable "region" {
  default = "us-west-2"
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  default = "10.0.1.0/24"
}

variable "db_username" {
  default = "your_db_username"
}

variable "db_password" {
  default = "your_db_password"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "The AWS key pair name for EC2 access"
  default     = "your_key_name"
}
