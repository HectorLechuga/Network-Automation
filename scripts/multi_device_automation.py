from netmiko import ConnectHandler
import os

password = os.environ.get("dev_ssh")

if not password:
    raise SystemExit("Error: dev_ssh environment variable is not set.")

devices = [
    {
        "device_type": "cisco_xe",
        "host": "10.10.20.49",
        "username": "developer",
        "password": password
    },
    {
        "device_type": "cisco_nxos",
        "host": "10.10.20.41",
        "username": "developer",
        "password": password
    },
    {
        "device_type": "cisco_xr",
        "host": "10.10.20.35",
        "username": "developer",
        "password": password
    }
]

commands = {
    "cisco_xe": ["show version", "show ip interface brief"],
    "cisco_nxos": ["show version", "show interface brief"],
    "cisco_xr": ["show version", "show ip interface brief"]
}

for device in devices:
    try:
        with ConnectHandler(**device) as connection:
            print(f"\n{"=" * 50}")
            print(f"Hostname: {connection.find_prompt()} | IP Address: {device["host"]}")
            print(f"OS: {device["device_type"]}")
            print(f"=" * 50)

            device_commands = commands[device["device_type"]]
            
            for command in device_commands:
                print(f"\n--- {connection.find_prompt()} {command} ---")
                output = connection.send_command(command)
                print(output)
    except Exception as error:
        print(f"Connection failed for {device["host"]}: {error}")