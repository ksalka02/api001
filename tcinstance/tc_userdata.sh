#!/bin/bash
yum -y update
echo "###################################  install docker  #############################"
yum -y install docker
echo "###################################  start docker  #############################"
systemctl start docker
echo "###################################  run docker  #############################"
docker run -v team_city_data:/data/teamcity_server/datadir -v team_city_logs:/opt/teamcity/logs -p 8111:8111 -d jetbrains/teamcity-server
echo "###################################  test docker  #############################"
docker ps