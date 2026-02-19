# SMART LOG ANALYZER CLI TOOL

info_count = 0
warning_count = 0
error_count = 0
total_logs = 0

error_frequency = {}
error_times = []

print(" Analyzing log file...\n")

try:
    with open("log.txt", "r") as file:
        for line in file:

            # Skip empty lines
            if not line.strip():
                continue

            total_logs += 1

            # Count log types
            if "INFO" in line:
                info_count += 1

            elif "WARNING" in line:
                warning_count += 1

            elif "ERROR" in line:
                error_count += 1

                # Extract error message
                parts = line.split("ERROR", 1)
                error_message = parts[1].strip()

                # Count frequency of each error
                if error_message in error_frequency:
                    error_frequency[error_message] += 1
                else:
                    error_frequency[error_message] = 1

                # Extract timestamp
                timestamp = parts[0].strip()
                error_times.append(timestamp)

    # 🖨 PRINT SUMMARY
    print(" LOG SUMMARY")
    print("-----------------------")
    print("Total logs:", total_logs)
    print("INFO logs:", info_count)
    print("WARNING logs:", warning_count)
    print("ERROR logs:", error_count)

    print()

    # Most frequent error
    if error_frequency:
        most_common_error = max(error_frequency, key=error_frequency.get)
        print(" Most frequent error:", most_common_error)
        print("Occurrences:", error_frequency[most_common_error])
    else:
        print("No ERROR logs found")

    print()

    # Error time range
    if error_times:
        print(" First error at:", error_times[0])
        print(" Last error at:", error_times[-1])

    # Save error logs separately
    with open("error_logs.txt", "w") as outfile:
        with open("log.txt", "r") as infile:
            for line in infile:
                if "ERROR" in line:
                    outfile.write(line)

    print("\n Error logs saved to error_logs.txt")

    # Write summary report
    with open("summary_report.txt", "w") as report:
        report.write("LOG ANALYSIS SUMMARY\n")
        report.write("----------------------\n")
        report.write(f"Total logs: {total_logs}\n")
        report.write(f"INFO logs: {info_count}\n")
        report.write(f"WARNING logs: {warning_count}\n")
        report.write(f"ERROR logs: {error_count}\n\n")

        if error_frequency:
            report.write(f"Most frequent error: {most_common_error}\n")
            report.write(f"Occurrences: {error_frequency[most_common_error]}\n\n")

        if error_times:
            report.write(f"First error time: {error_times[0]}\n")
            report.write(f"Last error time: {error_times[-1]}\n")

    print(" Summary report saved to summary_report.txt")

except FileNotFoundError:
    print(" log.txt file not found. Please create the log file.")
