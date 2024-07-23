import os
import platform
import psutil
from datetime import datetime
import socket

def gather_system_info():
    system_info = {
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture(),
        "Boot Time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
    }
    return system_info

def gather_disk_info():
    disk_info = []
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append({
            "Device": partition.device,
            "Mountpoint": partition.mountpoint,
            "File System Type": partition.fstype,
            "Total Size (GB)": usage.total / (1024 ** 3),
            "Used (GB)": usage.used / (1024 ** 3),
            "Free (GB)": usage.free / (1024 ** 3),
            "Percentage Used": usage.percent,
        })
    return disk_info

def gather_network_info():
    network_info = []
    for name, snic in psutil.net_if_addrs().items():
        for snicaddr in snic:
            if snicaddr.family == socket.AF_INET:
                network_info.append({
                    "Interface": name,
                    "IP Address": snicaddr.address,
                    "Netmask": snicaddr.netmask,
                    "Broadcast IP": snicaddr.broadcast,
                })
    return network_info

def generate_report():
    system_info = gather_system_info()
    disk_info = gather_disk_info()
    network_info = gather_network_info()
    
    report = f"""
    Forensic Report
    ===============

    System Information
    ------------------
    Hostname: {system_info['Hostname']}
    IP Address: {system_info['IP Address']}
    OS: {system_info['OS']}
    OS Version: {system_info['OS Version']}
    Processor: {system_info['Processor']}
    Architecture: {system_info['Architecture']}
    Boot Time: {system_info['Boot Time']}

    Disk Information
    ----------------
    """
    for disk in disk_info:
        report += f"""
        Device: {disk['Device']}
        Mountpoint: {disk['Mountpoint']}
        File System Type: {disk['File System Type']}
        Total Size (GB): {disk['Total Size (GB)']:.2f}
        Used (GB): {disk['Used (GB)']:.2f}
        Free (GB): {disk['Free (GB)']:.2f}
        Percentage Used: {disk['Percentage Used']}%
        """
    
    report += "\nNetwork Information\n-------------------\n"
    for net in network_info:
        report += f"""
        Interface: {net['Interface']}
        IP Address: {net['IP Address']}
        Netmask: {net['Netmask']}
        Broadcast IP: {net['Broadcast IP']}
        """
    
    with open("forensic_report.txt", "w") as file:
        file.write(report)
    
    print("Forensic report generated successfully!")

if __name__ == "__main__":
    generate_report()
