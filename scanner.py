# Simple Port Scanner by Throne-ir
import socket
import sys
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            return True
        sock.close()
    except Exception:
        pass
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target_ip>")
        sys.exit(1)

    target = sys.argv[1]
    
    try:
        socket.inet_aton(target)
    except socket.error:
        print("Invalid IP address")
        sys.exit(1)

    print(f"Starting scan for {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []
    
    for port in range(1, 1025):
        if scan_port(target, port):
            print(f"Port {port}: OPEN")
            open_ports.append(port)

    print("-" * 50)
    print(f"Scan completed at {datetime.now()}")
    print(f"Total open ports found: {len(open_ports)}")
    
    if open_ports:
        print("Open ports:", open_ports)

if __name__ == "__main__":
    main()
