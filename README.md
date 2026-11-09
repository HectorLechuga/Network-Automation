# Network Automation using Cisco Devices

## Project Overview

Demostrating the use of Python and Netmiko to automate network management tasks across Cisco networking devices.

This project uses Cisco Devent Sandbox to create a virtual environment for developing and testing network automation scripts.

My goal is to gain hands on experience with network automation by simplifying repetitive network management tasks.

## Tools and Platforms

- **Python** - Network automation scripting
- **Netmiko** - SSH based network device management
- **Cisco IOS XE** - Cisco operating system
- **Cisco DevNet Sandbox** - Virtual lab environment
- **Github** - Version control
- **VS Code** - Developement environment

## Project Phases

## Phase 1: Automated Device Inventory 

Created a Python script using Netmiko to establish an SSH connection to a Cisco Catalyst 8000v router running IOS XE

**Python Script:** [device_inventory.py](scripts/device_inventory.py)

The script automatically executed the following commands:
- 'show version'
- 'show ip interface brief'
- 'show ip route'

**Result:** Successfully connected to the Cisco Catalyst 8000v and retrieved device information, interface status, and routing information.

## Security 

- Authentication credentials are not hardcoded into Python script
- SSH passwords are retrieved from environment variables using Python's 'os' module

## Documentation 

Detailed explaination, script execution, and screenshots are available in the 'doc/' directory

- [Phase 1: Automated Device Inventory}(docs/phase1-device-inventory.md)
