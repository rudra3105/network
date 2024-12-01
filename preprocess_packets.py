from scapy.all import rdpcap
import pandas as pd

def preprocess_pcap(input_file, output_file):
    """
    Reads a PCAP file and converts it into a CSV with relevant packet details.
    """
    packets = rdpcap(input_file)
    data = []

    for packet in packets:
        if hasattr(packet, 'haslayer') and packet.haslayer('IP'):
            data.append({
                "src_ip": packet['IP'].src,
                "dst_ip": packet['IP'].dst,
                "protocol": packet['IP'].proto,
                "length": len(packet)
            })

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    input_pcap = "pcap_files/captured_packets.pcap"
    output_csv = "csv_files/preprocessed_packets.csv"
    
    preprocess_pcap(input_pcap, output_csv)
