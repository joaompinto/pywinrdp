sed -i 's/enforcing/disabled/g' /etc/selinux/config
setenforce 0 && sestatus
systemctl stop firewalld
systemctl disable firewalld
dnf groupinstall -y "Server with GUI"
dnf install -y xrdp
systemctl start xrdp
systemctl enable xrdp