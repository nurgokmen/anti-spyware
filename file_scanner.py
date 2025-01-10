import os


SUSPICIOUS_KEYWORDS = ["spyware", "keylogger", "steal"]

def scan_files(directory):
    print(f"Scanning files in directory: {directory}")
    for root, _,files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r") as f:
                    content = f.read()
                    if any(keyword in content.lower() for keyword in SUSPICIOUS_KEYWORDS):
                        print(f"suspicious file detected: {file_path}")
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

