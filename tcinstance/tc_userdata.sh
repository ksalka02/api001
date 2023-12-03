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
#!/bin/bash
yum -y update
echo "###################################  install docker  #############################"
yum -y install docker
# echo "###################################  fix volume vid #############################"
# df -h
# mkfs -t xfs /dev/xvdf
# file -s /dev/xvdf
# mkdir -p /apps/volume/new_volume
# mount /dev/sdf /apps/volume/new_volume
# df -h
echo "###################################  fix volume article #############################"
lsblk
file -s /dev/xvdf
# file -s /dev/xvdf1
# file -s /dev/xvdf2
mkfs -t xfs /dev/xvdf
# mkfs -t xfs /dev/xvdf1
# mkfs -t xfs /dev/xvdf2
mkdir -p /newvolume
mkdir -p /tcagent
mount /dev/xvdf /newvolume/
# mount /dev/xvdf2 /tcagent/
# mkdir -p newvolume/data
# mkdir -p newvolume/logs
# cd /newvolume
# df -h
echo "###################################  start docker  #############################"
systemctl start docker
echo "###################################  run docker  #############################"
# docker logs "container name"
# chown -R 1000:1000 /newvolume
docker run -v /newvolume:/data/teamcity_server/datadir -v /newvolume:/opt/teamcity/logs -p 8111:8111 -d jetbrains/teamcity-server
instance_ip=$(ec2-metadata --public-ipv4 | awk 'NR==1{print $2}')
docker run -v /tcagent:/data/teamcity_agent/conf -e SERVER_URL="$${instance_ip}:8111" -d jetbrains/teamcity-agent
# echo "###################################  test docker  #############################"
# docker ps
# echo "###################################  start sleep  #############################"
# sleep 20
# echo "###################################  end sleep  #############################"
# systemctl restart docker
# docker run -v /newvolume/data:/data/teamcity_server/datadir -v /newvolume/logs:/opt/teamcity/logs -p 8111:8111 -d jetbrains/teamcity-server
docker ps


# ######################################################### PARTING VOLUME ####################################
# unmount and make gpt partition table instead of loop
# umount /dev/xvdf
# parted /dev/xvdf
# mktable gpt
# mkpart xfs 0mb 8590mb
# print
# ######################################################### PARTING VOLUME ####################################