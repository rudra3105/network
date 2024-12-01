import pandas as pd
import re

def detect_anomalies_with_regex(csv_file, output_file):
    """
    Detect anomalies using regex patterns.
    """
    data = pd.read_csv(csv_file)
    anomalies = []

    ip_pattern = r"^(192\.168|10\.)"
    for index, row in data.iterrows():
        if not re.match(ip_pattern, row["src_ip"]):
            anomalies.append(row)

    anomalies_df = pd.DataFrame(anomalies)
    anomalies_df.to_csv(output_file, index=False)
    print(f"Anomalies saved to {output_file}")

if __name__ == "__main__":
    input_csv = "csv_files/preprocessed_packets.csv"
    output_csv = "csv_files/anomalies.csv"
    
    detect_anomalies_with_regex(input_csv, output_csv)
