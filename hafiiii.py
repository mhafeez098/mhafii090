import psutil

def get_network_traffic():
    # Get network statistics
    network_stats = psutil.net_io_counters(pernic=True)

    # Display data for each network interface
    for interface, data in network_stats.items():
        print(f"Interface: {interface}")
        print(f"    Bytes Sent: {data.bytes_sent}")
        print(f"    Bytes Received: {data.bytes_recv}")
        print(f"    Packets Sent: {data.packets_sent}")
        print(f"    Packets Received: {data.packets_recv}")
        print()

if __name__ == "__main__":
    get_network_traffic()