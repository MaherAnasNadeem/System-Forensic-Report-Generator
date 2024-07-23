System Forensic Report Generator
This Python script generates a comprehensive forensic report of your system's information, including details about the operating system, hardware, disks, and network interfaces. It is designed to assist IT professionals and system administrators in gathering critical system diagnostics quickly and efficiently.

Features
System Information: Retrieves hostname, IP address, OS details, processor information, architecture, and boot time.
Disk Information: Collects details of all disk partitions, including device names, mountpoints, file system types, total size, used space, free space, and percentage used.
Network Information: Gathers details of all network interfaces, including interface names, IP addresses, netmasks, and broadcast addresses.

Code Overview
The script is divided into several functions:

gather_system_info(): Gathers system-related information such as hostname, IP address, OS details, processor, architecture, and boot time.
gather_disk_info(): Collects disk-related information such as device names, mountpoints, file system types, total size, used space, free space, and percentage used.
gather_network_info(): Gathers network-related information such as interface names, IP addresses, netmasks, and broadcast addresses.
generate_report(): Generates a comprehensive forensic report by calling the above functions and writes the report to a text file.
