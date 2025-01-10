import psutil

def monitor_network():
    print("Monitoring network activity...")
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr and conn.laddr.port == 9999:
            print(f"Suspicious connection detected: Local Address: {conn.laddr}, Status: {conn.status}")
            