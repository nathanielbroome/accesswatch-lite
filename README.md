# AccessWatch Lite

AccessWatch Lite is a lightweight log‑analysis tool designed to help identify suspicious authentication activity, including brute‑force login attempts. It parses standard auth logs, extracts meaningful fields, groups failed attempts by IP, and prepares the data for time‑window analysis.

---

## 🚀 Current Features

### ✔ Log Parsing
- Extracts timestamps from each log entry  
- Extracts IP addresses  
- Extracts login status (SUCCESS / FAIL)  
- Structures each entry into a clean dictionary for analysis  

### ✔ Failed Attempt Grouping
- Builds a dictionary of failed login attempts per IP  
- Stores timestamps for each failed attempt  
- Prepares data for brute‑force detection logic  

### ✔ Summary Report
- Total log entries  
- Total failed login attempts  
- Unique IP count  
- Top 3 most active IPs  

---

## 🔧 In Progress

### ⏳ Brute‑Force Detection
Next steps include:
- Sorting timestamps per IP  
- Sliding time‑window analysis  
- Threshold‑based detection (e.g., 5 failures in 30 seconds)  
- Flagging suspicious IPs  

These features will turn AccessWatch Lite into a functional early‑warning system for authentication attacks.

---

## 📅 Development Notes

This project is being built incrementally with clean, consistent commits. Each update reflects a stable milestone in the development process, including parsing improvements, structural changes, and new detection logic.

---

## 📂 Project Structure

accesswatch-lite/
│
├── src/
│   └── main.py        # Main log analysis script
│
├── logs/
│   └── auth.log       # Sample authentication log file
│
└── README.md

---

## 🧭 Roadmap

- [ ] Sort timestamps per IP  
- [ ] Implement sliding time‑window brute‑force detection  
- [ ] Add suspicious IP reporting  
- [ ] Add configurable thresholds  
- [ ] Add optional JSON/CSV export  
- [ ] Add command‑line arguments for log path and thresholds  

---

## 🛠 Requirements

- Python 3.x  
- Standard library only (no external dependencies)

---

## 📜 License

MIT License (or whichever you choose)

