from datetime import datetime
def difference_in_seconds(d1,d2):
    difference = d2 - d1

    difference_in_seconds = difference.total_seconds()
    return difference_in_seconds

current_datetime = datetime.now()
date1 = datetime(2025, 2, 4, 12, 0, 0)


print("Date 1:", date1)
print("Date 2(now):", current_datetime)
print("Difference in seconds:", int(difference_in_seconds(date1,current_datetime)))
