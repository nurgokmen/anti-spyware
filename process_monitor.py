import psutil

def monitor_process():
    print("Monitoring processes...")

    for proc in psutil.process_iter(['pid','name']):
        try:
            process_name = proc.info.get('name', '')
            if "spyware" in process_name.lower():
                print(f"Suspicious process detected: {proc.info}")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

