resource "aws_launch_template" "players_instance" {

  instance_type          = "t2.micro"
  image_id               = "ami-03a6eaae9938c858c"
  vpc_security_group_ids = [aws_security_group.players_api.id]
  key_name               = "api_test_key"
  user_data              = filebase64("../players_userdata.sh")
}

resource "aws_autoscaling_group" "asg_api" {

  name                      = "asg_for_api"
  availability_zones        = ["us-east-1a", "us-east-1b"]
  max_size                  = 1
  min_size                  = 1
  desired_capacity          = 1
  health_check_grace_period = 300

  launch_template {
    id = aws_launch_template.players_instance.id
  }
  # depends_on = [module.aws_lb]
  target_group_arns = [aws_lb_target_group.api_tg.arn]
}

# resource "aws_autoscaling_attachment" "lb_asg" {
#   autoscaling_group_name = aws_autoscaling_group.asg_api.id
#   lb_target_group_arn    = aws_lb_target_group.api_tg.arn
# }