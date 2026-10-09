import os
from collections import Counter

def main():
    log_path = os.path.join("..", "logs", "auth.log")

    with open(log_path, "r") as f:
        lines = f.readlines()

    total_entries = len(lines)

    failed_attempts = sum(1 for line in lines if "status=FAIL" in line)

    ips = []
    for line in lines:
        parts = line.split()
        for part in parts:
            if part.startswith("ip="):
                ip = part.replace("ip=", "")
                ips.append(ip)

    unique_ip = len(set(ips))

    ip_counts = Counter(ips)

    top_three = ip_counts.most_common(3)

    print("=== AccessWatch Lite Report ===")
    print(f"Total log entries: {total_entries}")
    print(f"Failed login attempts: {failed_attempts}")
    print(f"Unique IP addresses: {unique_ip}")
    print("\nTop 3 most active IPs:")
    for ip, count in top_three:
        print(f"{ip}: {count} attempts")

if __name__ == "__main__":
    main()
