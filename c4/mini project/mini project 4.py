import json

logs = [

    {
        "level": "INFO",
        "message": "Application started"
    },

    {
        "level": "ERROR",
        "message": "Database connection failed"
    },

    {
        "level": "WARNING",
        "message": "Low memory"
    },

    {
        "level": "ERROR",
        "message": "File not found"
    }

]


# Store data in JSON file

with open("logs.json", "w") as file:

    json.dump(logs, file, indent=4)


# Read JSON file

with open("logs.json", "r") as file:

    data = json.load(file)


# Analyze logs

counts = {}

for entry in data:

    level = entry["level"]

    counts[level] = counts.get(level, 0) + 1


print("LOG FILE ANALYSIS")

for level, count in counts.items():

    print(level, ":", count)

print("Total log entries:", len(data))