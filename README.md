# Network Automation using Cisco Devices

## Project Overview

This projects demostrates the use of Python and Netmiko to automate network management tasks across Cisco networking devices.

Using Cisco DevNet Sandbox, I developed and test Python scripts in a virtual networking environment to gain hands on experience with network automation to simplify repetitive network management tasks.

## Tools and Platforms

- **Python** - Network automation scripting
- **Netmiko** - SSH based network device management
- **Network Operating Systems** - Cisco IOS XE, NX-OS, and IOS XR
- **Cisco DevNet Sandbox** - Virtual lab environment
- **Github** - Version control
- **VS Code** - Developement environment

## Project Phases

### Phase 1: Automated Device Inventory 

Developed a Python script to establish an SSH connection to a Cisco Catalyst 8000v router and automatically retrieve device information, interface status, and routing information.

**Python Script:** [device_inventory.py](scripts/device_inventory.py)

**Documentation:** [Phase 1: Automated Device Inventory](docs/phase1-device-inventory.md)

### Phase 2: Multi-Device Automation

Expanded the automation to support multiple Cisco devices running IOS XE, NX-OS, and IOS XR. Implemented OS command execution, organized device output, and connection error handling.

**Python Script:** [multi_device_automation.py](scripts/multi_device_automation.py)

**Documentation:** [Phase 2: Multi-Device Automation](docs/phase2-multi-device-automation.md)

## Security
- Authentication credentials are not hardcoded into Python scripts
- SSH passwords are retrieved from environment variables using Python's `os` module

## Documentation 

Each project phases includes detailed explainations, testing results, and screenshots in the [docs](docs/) directory.