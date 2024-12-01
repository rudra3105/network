from scapy.all import sniff, wrpcap
import os

def capture_packets(output_file="captured_packets.pcap", packet_count=100):
    """
    Captures packets from the network interface and saves them to a PCAP file.
    """
    print(f"Capturing {packet_count} packets...")
    packets = sniff(count=packet_count)
    wrpcap(output_file, packets)
    print(f"Captured packets saved to {output_file}")

if __name__ == "__main__":
    output_dir = "pcap_files"
    os.makedirs(output_dir, exist_ok=True)
    capture_packets(output_file=os.path.join(output_dir, "captured_packets.pcap"))
