from netmiko import ConnectHandler
import os

password = os.environ.get("dev_ssh")

if not password:
    raise SystemExit("Error: dev_ssh environment variable is not set")

router = {
    "device_type": "cisco_xe",
    "host": "10.10.20.48",
    "username": "developer",
    "password": password
}

try:
    with ConnectHandler(**router) as connection:
        print(f"Connected to {connection.find_prompt()}")

        commands = [
            "show version",
            "show ip interface brief",
            "show ip route"
        ]

        for command in commands:
            print(f"\n--- {command} ---")
            output = connection.send_command(command)
            print(output)
except Exception as error:
    print(f"Connection failed: {error}")