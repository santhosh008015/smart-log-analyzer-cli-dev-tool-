# Smart Log Analyzer CLI (Dev Tool)

A production-style Python command-line tool that analyzes server log files and generates actionable insights such as error frequency, log distribution, and timeline analysis.

This project simulates real-world backend log analysis used by developers and DevOps engineers to debug, monitor, and understand system failures.

---

## 🚀 Overview

Modern backend systems generate large log files containing INFO, WARNING, and ERROR events.  
Manually scanning logs is inefficient and time-consuming.

This CLI tool automates log analysis by:

- Streaming log files line-by-line  
- Classifying log levels  
- Extracting and isolating error entries  
- Identifying recurring failures  
- Tracking error time ranges  
- Generating summary reports  

---

## 🧠 Problem Statement

Given a structured log file:

2025-01-10 10:22:10 ERROR Database connection failed

Build a system that can:

- Count log level distribution  
- Identify the most frequent error  
- Extract error logs into a separate file  
- Determine when errors started and stopped  
- Produce a structured summary report  

---

## ✨ Features

- Log level statistics (INFO / WARNING / ERROR)  
- Most frequent error detection  
- First and last error timestamps  
- Automatic error log extraction  
- Summary report generation  
- Handles empty lines and missing files safely  
- Fully CLI-based execution  

---

## 🛠 Tech Stack

- Python 3.14.0
- File Handling  
- Dictionaries  
- Command Line Interface (CLI)  

---

## 📂 Project Structure

smart-log-analyzer-cli-dev-tool-/

log_analyzer.py        # Main script  
log.txt                # Sample input log file  
error_logs.txt         # Generated error logs  
summary_report.txt     # Generated summary report  
README.md              # Documentation  

---

## ▶️ How to Run

1. Clone the repository:

git clone https://github.com/santhosh008015/smart-log-analyzer-cli-dev-tool-.git

2. Navigate into the folder:

cd smart-log-analyzer-cli-dev-tool-

3. Run:

python log_analyzer.py

Make sure log.txt is present in the same folder.

---

## 📊 Sample Output

Analyzing log file...

LOG SUMMARY  
Total logs: 5  
INFO logs: 2  
WARNING logs: 1  
ERROR logs: 2  

Most frequent error: Database connection failed  
Occurrences: 2  

First error at: 2025-01-10 10:22:10  
Last error at: 2025-01-10 10:23:00  

<img width="1920" height="1080" alt="output" src="https://github.com/user-attachments/assets/a1431ad9-54dc-4391-9cb7-23f76eb697c1" />


---

## 🧩 How It Works

1. Reads the log file line by line  
2. Skips empty lines  
3. Identifies INFO, WARNING, and ERROR logs  
4. Extracts error messages  
5. Counts frequency using dictionary  
6. Finds first and last error timestamps  
7. Generates summary report  

Time Complexity: O(n)  
Space Complexity: O(k) where k = unique error types  

---

## 💡 Why This Project Matters

This project demonstrates real-world backend log analysis and data processing.  
It shows the ability to work with files, analyze patterns, and generate useful insights — skills required for backend and Python developer roles.

---

## 🔮 Future Improvements

- JSON output support  
- Advanced log parsing  
- REST API version using Django REST Framework  
- Log visualization dashboard  

---

## 👨‍💻 Author

Santhosh M  
Aspiring Backend Developer  



