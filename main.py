from file_scanner import scan_files
from process_monitor import monitor_process
from network_monitor import monitor_network
from spyware_simulator import spyware_simulator, simulate_network_activity


def menu():
    while True:
        print("\nAnti-Spyware Program")
        print("1. Scan Files")
        print("2. Monitor Processes")
        print("3. Monitor Network Activity")
        print("4. Simulate Spyware (Safe)")
        print("5. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            directory = input("Enter the directory to scan: ")
            scan_files(directory)
        elif choice == "2":
            monitor_process()
        elif choice == "3":
            monitor_network()
        elif choice == "4":
            spyware_simulator()
            simulate_network_activity()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("You entered an invalid choice. PLease try again.")


if __name__ == "__main__":
    menu()