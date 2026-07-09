from modules.statistics import stats
from modules.logger import log_packet

from scapy.layers.inet import IP, TCP, UDP, ICMP

from datetime import datetime

from colorama import Fore, init

init(autoreset=True)


def analyze_packet(packet):

    stats.total_packets += 1

    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Ignore packets that don't have an IP layer
    if IP not in packet:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    print(Fore.MAGENTA + f"Source IP      : {src_ip}")
    print(Fore.MAGENTA + f"Destination IP : {dst_ip}")

    # Default values
    protocol = "Other"
    src_port = "-"
    dst_port = "-"

    if TCP in packet:
        stats.tcp_packets += 1
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(Fore.GREEN + f"Protocol       : {protocol}")
        print(f"Source Port    : {src_port}")
        print(f"Destination Port: {dst_port}")

    elif UDP in packet:
        stats.udp_packets += 1
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        print(Fore.YELLOW + f"Protocol       : {protocol}")
        print(f"Source Port    : {src_port}")
        print(f"Destination Port: {dst_port}")

    elif ICMP in packet:
        stats.icmp_packets += 1
        protocol = "ICMP"

        print(Fore.BLUE + f"Protocol       : {protocol}")

    else:
        stats.other_packets += 1
        print(Fore.WHITE + f"Protocol       : {protocol}")

    print(f"Packet Size    : {len(packet)} bytes")

    # Save packet to CSV
    log_packet(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        src_ip,
        dst_ip,
        protocol,
        src_port,
        dst_port,
        len(packet)
    )

    print(Fore.CYAN + "=" * 60)

    print(Fore.CYAN + "\nTraffic Statistics")
    print(Fore.GREEN + f"Total Packets : {stats.total_packets}")
    print(Fore.GREEN + f"TCP Packets   : {stats.tcp_packets}")
    print(Fore.YELLOW + f"UDP Packets   : {stats.udp_packets}")
    print(Fore.BLUE + f"ICMP Packets  : {stats.icmp_packets}")
    print(Fore.WHITE + f"Other Packets : {stats.other_packets}")