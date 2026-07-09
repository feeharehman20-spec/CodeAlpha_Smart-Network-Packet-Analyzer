#  Smart Network Packet Analyzer

A Python-based network packet analyzer that captures and inspects live network traffic in real time using the Scapy library. The application extracts key packet information, provides live traffic statistics, and stores captured packet details in a CSV log for further analysis.

This project was developed as part of my **CodeAlpha Cybersecurity Internship** to strengthen my understanding of computer networks, packet analysis, and Python-based network security tools.


##  Project Overview

Every device connected to a network continuously sends and receives packets. Understanding these packets is an essential skill in cybersecurity, network troubleshooting, and threat detection.

This project monitors live network traffic and displays important packet information such as:

- Source IP Address
- Destination IP Address
- Network Protocol
- Source & Destination Ports
- Packet Size
- Live Traffic Statistics

The captured information is also automatically saved to a CSV file for future analysis.


##  Features

- Capture live network packets
- Analyze IP, TCP, UDP and ICMP packets
- Display source and destination IP addresses
- Display source and destination port numbers
- Show packet size
- Real-time packet counter
- Protocol-wise traffic statistics
- Automatic CSV logging
- Modular Python project structure
- Colorized terminal output for better readability


##  Technologies Used

- Python 3
- Scapy
- Colorama


##  Project Structure

Smart-Network-Packet-Analyzer/
│
├── logs/
│   └── packet_log.csv
│
├── modules/
│   ├── analyzer.py
│   ├── logger.py
│   ├── sniffer.py
│   ├── statistics.py
│   └── __init__.py
│
├── screenshots/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore


##  Installation

Clone the repository

```bash
git clone https://github.com/your-username/Smart-Network-Packet-Analyzer.git
```

Move into the project folder

```bash
cd Smart-Network-Packet-Analyzer
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

##  Example Output

Time              : 2026-07-06 20:13:34

Source IP         : 192.168.1.3
Destination IP    : 20.184.175.6

Protocol          : TCP
Source Port       : 19475
Destination Port  : 443

Packet Size       : 66 bytes

Traffic Statistics

Total Packets     : 17
TCP Packets       : 17
UDP Packets       : 0
ICMP Packets      : 0


##  Packet Logging

Every captured packet is automatically saved to:

```
logs/packet_log.csv
```

Each log entry contains:

- Timestamp
- Source IP
- Destination IP
- Protocol
- Source Port
- Destination Port
- Packet Size

This makes the captured traffic easy to review or analyze later using spreadsheet tools.



##  Screenshots

<img width="1002" height="642" alt="analyzer_code" src="https://github.com/user-attachments/assets/29db3cf1-5d39-4909-9d8a-420b453dffe0" />
<img width="722" height="638" alt="packet_log" src="https://github.com/user-attachments/assets/ec1c8be0-d0a9-4894-93f0-974b68f4c205" />
<img width="286" height="521" alt="project_structure" src="https://github.com/user-attachments/assets/85428ee6-f122-40cd-9a48-34ecc3e3def0" />
<img width="783" height="369" alt="running_program" src="https://github.com/user-attachments/assets/e7fbb1a6-f2c0-4dd7-82f6-98fdc891e901" />



##  Skills Demonstrated

This project helped me strengthen my understanding of:

- Network Packet Analysis
- TCP/IP Protocol Suite
- Packet Capture using Scapy
- Python Programming
- Modular Project Design
- File Handling & CSV Logging
- Basic Network Traffic Monitoring

---

##  Future Improvements

Some enhancements planned for future versions include:

- Packet filtering by protocol
- Payload inspection
- Suspicious traffic detection
- Network visualization dashboard
- PCAP file export
- Machine Learning-based anomaly detection


##  License

This project is licensed under the MIT License.

## Personal Reflection

Building this project gave me practical experience with how network packets travel across a network and how packet analysis can support cybersecurity tasks such as network monitoring and intrusion detection. It also strengthened my understanding of Python, Scapy, and the TCP/IP protocol suite, providing a foundation for more advanced projects in network security.
