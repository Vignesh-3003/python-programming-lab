# Create and write sample log file

with open("sample_log.txt", "w") as file:

    file.write("INFO: Application started\n")
    file.write("WARNING: Low disk space\n")
    file.write("ERROR: Unable to connect\n")


# Read log file

with open("sample_log.txt", "r") as file:

    lines = file.readlines()

print("LOG FILE CONTENTS")

for line in lines:

    print(line.strip())

print("Total log entries:", len(lines))