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
echo "###################################  install git  #############################"
yum -y install git
echo "###################################  install pip  #############################"
yum -y install python3-pip
echo "###################################  clone repo  #############################"
git clone https://github.com/ksalka02/api001.git

cd api001
echo "###################################  install requirements  #############################"
pip install -r requirements.txt
echo "###################################  run main.py  #############################"
python3 moreinfo.py