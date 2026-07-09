import csv
import os

LOG_FILE = "logs/packet_log.csv"


def initialize_logger():

    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Time",
                "Source IP",
                "Destination IP",
                "Protocol",
                "Source Port",
                "Destination Port",
                "Packet Size"
            ])


def log_packet(time, src_ip, dst_ip, protocol, src_port, dst_port, size):

    with open(LOG_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            time,
            src_ip,
            dst_ip,
            protocol,
            src_port,
            dst_port,
            size
        ])