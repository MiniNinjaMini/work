from datetime import datetime

current_datetime = datetime.now()

datetime_without_microseconds = current_datetime.replace(microsecond=0)

print("With Microseconds:", current_datetime)
print("Without Microseconds:", datetime_without_microseconds)
