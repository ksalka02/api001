terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.17.0"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "main"
}

########  Security Group ######


resource "aws_security_group" "players_api" {
  name        = "players_api"
  description = "api ports"
  # vpc_id      = aws_vpc.main.id

  ingress {
    description = "ssh"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "https"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "custom"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

########  EC2 INSTANCE ######

resource "aws_instance" "players_api_instance" {
  ami                    = "ami-03a6eaae9938c858c"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.players_api.id]
  key_name               = "api_test_key"
  user_data              = file("../players_userdata.sh")
  tags = {
    Name = "players"
  }
}

resource "aws_instance" "moreinfo_api_instance" {
  ami                    = "ami-03a6eaae9938c858c"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.players_api.id]
  key_name               = "api_test_key"
  user_data              = file("../moreinfo_userdata.sh")
  tags = {
    Name = "moreinfo"
  }
}

###################### LOAD BALANCER #######################

# resource "aws_lb_target_group" "api-lb" {
#   name     = "api-lb"
#   port     = 5000
#   protocol = "TCP"
#   #how to show vpc
#   slow_start = 0

#   # load_balancing_algorithm_type = "round_robin"
# }







# resource "null_resource" "more_info" {

#   triggers = {
#     test = timestamp()
#   }

#   provisioner "local-exec" {
#       command = "curl --location '${aws_instance.public_instance.public_dns}:5000/moreinfo'"
#   }

# }


output "get_player_api" {
  description = "players address"
  value       = "${aws_instance.players_api_instance.public_dns}:5000/players"
}

output "get_moreinfo_api" {
  description = "moreinfo address"
  value       = "${aws_instance.moreinfo_api_instance.public_dns}:5000/moreinfo"
}
