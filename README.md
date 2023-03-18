# pywinrdp

A remote desktop client written in Python

[![PyPi](https://img.shields.io/pypi/v/pywinrdp.svg?style=flat-square)](https://pypi.python.org/pypi/pywinrdp)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/ambv/black)

# Motivation
Explore the use of the MS Windows Remote Desktop ActiveX component to build a remote deskto app in Python.

## Requirements
- Windows 10+
- Python 3.10+

## Testing requirements

- VirtualBox
- Vagrant

## Testing the code
### Using Vagrant and Virtualbox

This repo provides a Vagrantfile which will allow you to setup a Rocky Linux 8 VM which will run xrdp. This VM can then be used as the remote desktop target for experimentation

### How to test
From a PowerShell terminal:
```ps
cd vagrant && vagrant up &&  cd .
pip install -r requirements.txt
python -m pywinrdp
```

