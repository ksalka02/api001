#!/bin/bash
yum -y update
echo "###################################  install docker  #############################"
yum -y install docker


Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0

--//
Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="cloud-config.txt"

#cloud-config
cloud_final_modules:
- [scripts-user, always]

--//
Content-Type: text/x-shellscript; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="userdata.txt"



echo "###################################  start docker  #############################"
systemctl start docker
echo "###################################  run docker  #############################"
docker run -v team_city_data:/data/teamcity_server/datadir -v team_city_logs:/opt/teamcity/logs -p 8111:8111 -d jetbrains/teamcity-server
echo "###################################  test docker  #############################"
docker ps