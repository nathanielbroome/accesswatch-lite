import os
from datetime import datetime
from collections import Counter

def main():
    log_path = os.path.join("..", "logs", "auth.log")

    with open(log_path, "r") as f:
        lines = f.readlines()

    total_entries = len(lines)

    failed_attempts = sum(1 for line in lines if "status=FAIL" in line)
    
    failed_by_ip = {}
    logs = []
    ips = []
    for line in lines:
        ip = None
        status = None
        parts = line.split()
        timestamp_text = parts[0] + " " + parts[1]
        timestamp_object = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")


        for part in parts:
            if part.startswith("ip="):
                ip = part.replace("ip=", "")
                ips.append(ip)
            if part.startswith("status="):
                status = part.replace("status=", "")
        entry = {
            "timestamp": timestamp_object,
            "ip": ip,
            "status": status
        }       
        logs.append(entry)
        
    #loop through each log entry
    for entry in logs:
        if(entry["status"] != "FAIL"):
            continue
        if entry["ip"] not in failed_by_ip:
            failed_by_ip[entry["ip"]] = []

        failed_by_ip[entry["ip"]].append(entry["timestamp"])



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
