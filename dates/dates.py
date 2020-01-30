import datetime

# datetime.date() - Working with year, month and day

d = datetime.date(year=2020, month=7, day=23)  # 2020-07-23
print(d)

today = datetime.date.today()  # 2020-01-30
print(today)
print(today.year)
print(today.day)
print(today.month)
print(today.weekday())  # Monday = 0, Sunday = 6
print(today.isoweekday())  # Monday = 1, Sunday = 7

# time deltas (Durations)
tdelta = datetime.timedelta(days=7)

# A week from today
print(today + tdelta)  # 2020-02-06

# Days to my birthday
bday = datetime.date(2020, 7, 19)

till_bday = bday - today

print(till_bday)  # 171 days, 0:00:00
print(till_bday.days)  # 171
print(till_bday.total_seconds())  # 14774400.0
