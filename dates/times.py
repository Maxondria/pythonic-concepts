import datetime

# datetime.time - Working with hours, minutes, seconds, ms

t = datetime.time(hour=9, minute=30, second=45,
                  microsecond=100000)  # 09:30:45.100000
print(t)

print(t.hour)  # 9
