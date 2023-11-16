resource "aws_instance" "teamcity" {
  ami                    = "ami-03a6eaae9938c858c"
  instance_type          = "t2.small"
  vpc_security_group_ids = [aws_security_group.tc_sg.id]
  key_name               = "api_test_key"
  user_data              = file("tc_userdata.sh")
  tags = {
    Name = "TCtest"
  }
}

resource "aws_security_group" "tc_sg" {
  name = "tcssh"
  # description = "api ports"
  # vpc_id      = aws_vpc.main.id

  ingress {
    description = "ssh"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "custom"
    from_port   = 8111
    to_port     = 8111
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
