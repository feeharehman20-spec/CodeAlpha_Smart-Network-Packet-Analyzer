from scapy.all import sniff
from modules.analyzer import analyze_packet

def packet_callback(packet):
    analyze_packet(packet)

def start_sniffer():
    print("[INFO] Sniffer is running...")
    print("[INFO] Press Ctrl + C to stop.\n")

    sniff(
        prn=packet_callback,
        store=False
    )