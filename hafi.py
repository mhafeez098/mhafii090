import psutil
download = psutil.net_io_counters(pernic=True)["Wi-Fi"][1]
print(download)
import datetime
log_filename = "Wi-Fi"

# Generate timestamp for the log file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"{timestamp}_{log_filename}"
print(timestamp)
# Create or open the log file in append mode
log_file = open(log_filename, "a")

