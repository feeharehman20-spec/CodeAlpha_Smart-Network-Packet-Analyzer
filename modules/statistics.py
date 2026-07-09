# modules/statistics.py

class TrafficStats:

    def __init__(self):

        self.total_packets = 0

        self.tcp_packets = 0

        self.udp_packets = 0

        self.icmp_packets = 0

        self.other_packets = 0


stats = TrafficStats()