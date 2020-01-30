import datetime
import pytz  # pip install pytz

dt = datetime.datetime(year=2020, month=2, day=10, hour=13,
                       minute=34, second=23, tzinfo=pytz.UTC)

print(dt)  # 2020-02-10 13:34:23+00:00

dt_now = datetime.datetime.now(tz=pytz.UTC)

# Another way
# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

# Converting to different timezones
dt_kla = dt_now.astimezone(pytz.timezone('Africa/Kampala'))

# List all timezones
for tz in pytz.all_timezones:
    print(tz)

# Format Dates and Times
formatted_dt_now = dt_now.strftime('%B %d, %Y')  # February 10, 2020
print(formatted_dt_now)

# Format string to date

dt_str = 'February 10, 2020'

fmt_dt_str = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(fmt_dt_str)  # 2020-02-10 00:00:00

# strftime -> DATETIME TO STRING
# strptime -> STRING TO DATETIME
