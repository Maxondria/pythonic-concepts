import datetime

dt = datetime.datetime(year=2020, month=2, day=10, hour=13,
                       minute=34, second=23, microsecond=100000)  # 2020-02-10 13:34:23.100000

print(dt)
print(dt.date())  # 2020-02-10
print(dt.time())  # 13:34:23.100000
print(dt.hour)  # 13

# time delta
tdelta = datetime.timedelta(days=7)
print(dt + tdelta)  # 2020-02-17 13:34:23.100000


# Today (now)
print('\n============NOW()==============\n')

# Current Local DateTime with a timezone of Nonw
dt_today = datetime.datetime.today()  # 2020-01-30 19:38:18.780558

# We have option of passing in the option of TIMEZONE
dt_now = datetime.datetime.now()  # 2020-01-30 19:38:18.780571

# Current UTC time with timezone set to None
dt_utcnow = datetime.datetime.utcnow()  # 2020-01-30 16:38:18.780574

print(dt_today)
print(dt_now)
print(dt_utcnow)
