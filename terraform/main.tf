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


# resource "null_resource" "more_info" {

#   triggers = {
#     test = timestamp()
#   }

#   provisioner "local-exec" {
#       command = "curl --location '${aws_instance.public_instance.public_dns}:5000/moreinfo'"
#   }

# }


# output "get_player_api" {
#   description = "players address"
#   value       = "${aws_instance.players_api_instance.public_dns}:5000/players"
# }

# output "get_moreinfo_api" {
#   description = "moreinfo address"
#   value       = "${aws_instance.moreinfo_api_instance.public_dns}:5000/moreinfo"
# }
