import psutil
import json
from datetime import datetime

def get_network_traffic():
    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Get network statistics
    network_stats = psutil.net_io_counters(pernic=True)

    # Prepare data to save
    data_to_save = {
        "timestamp": timestamp,
        "network_interfaces": {}
    }

    # Store data for each network interface
    for interface, data in network_stats.items():
        interface_data = {
            "bytes_sent": data.bytes_sent,
            "bytes_received": data.bytes_recv,
            "packets_sent": data.packets_sent,
            "packets_received": data.packets_recv,
        }
        data_to_save["network_interfaces"][interface] = interface_data

    # Save data to a JSON file
    file_name = f"network_traffic_{timestamp}.json"
    with open(file_name, 'w') as file:
        json.dump(data_to_save, file, indent=4)

    print(f"Network traffic data saved to {file_name}")

if __name__ == "__main__":
    get_network_traffic()