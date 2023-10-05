locals {
  user_data5 = templatefile("../players_userdata.sh", { "env" = 5000 })
  user_data3 = templatefile("../players_userdata.sh", { "env" = 3000 })
}
resource "aws_launch_template" "players_instance5" {

  instance_type          = "t2.micro"
  image_id               = "ami-03a6eaae9938c858c"
  vpc_security_group_ids = [aws_security_group.players_api5.id]
  key_name               = "api_test_key"
  # user_data              = filebase64(templatefile("../players_userdata.sh", { "env" = 5000 }))
  # user_data              = templatefile("../players_userdata.sh", { "env" = 5000 })
  user_data              = base64encode("${local.user_data5}")
}

resource "aws_autoscaling_group" "asg_api5" {

  name                      = "asg_for_api_5"
  availability_zones        = ["us-east-1c", "us-east-1d"]
  max_size                  = 1
  min_size                  = 1
  desired_capacity          = 1
  health_check_grace_period = 300

  launch_template {
    id = aws_launch_template.players_instance5.id
  }
}

resource "aws_autoscaling_attachment" "lb_asg5" {
  autoscaling_group_name = aws_autoscaling_group.asg_api5.id
  lb_target_group_arn    = aws_lb_target_group.api_tg5.arn
}
############################################################################################################################

resource "aws_launch_template" "players_instance3" {

  instance_type          = "t2.micro"
  image_id               = "ami-03a6eaae9938c858c"
  vpc_security_group_ids = [aws_security_group.players_api3.id]
  key_name               = "api_test_key"
  # user_data              = filebase64(templatefile("../players_userdata.sh", { "env" = 3000 }))
  # user_data              = templatefile("../players_userdata.sh", { "env" = 3000 })
  user_data              = base64encode("${local.user_data3}")
}
resource "aws_autoscaling_group" "asg_api3" {

  name                      = "asg_for_api_3"
  availability_zones        = ["us-east-1c", "us-east-1d"]
  max_size                  = 1
  min_size                  = 1
  desired_capacity          = 1
  health_check_grace_period = 300

  launch_template {
    id = aws_launch_template.players_instance3.id
  }
}

resource "aws_autoscaling_attachment" "lb_asg3" {
  autoscaling_group_name = aws_autoscaling_group.asg_api3.id
  lb_target_group_arn    = aws_lb_target_group.api_tg3.arn
}