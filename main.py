from modules.sniffer import start_sniffer
from modules.logger import initialize_logger

def main():

    print("=" * 60)
    print(" Smart Network Packet Analyzer ")
    print("=" * 60)

    initialize_logger()

    print("Starting packet capture...\n")

    start_sniffer()
if __name__ == "__main__":
    main()