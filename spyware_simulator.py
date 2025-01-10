import threading
import socket
import time

def spyware_simulator():

    def dummy_spyware():
        while True:
            time.sleep(1)
            print("Spyware-like process running...")


    thread = threading.Thread(target=dummy_spyware, daemon=True)
    thread.start()


def simulate_network_activity():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1",9999))
        s.listen(1)
        print("Fake network activity running on 127.0.0.1:9999")
        s.accept()
    except Exception as e:
        print(f"Error simulating network : {e}")
