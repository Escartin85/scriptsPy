from datetime import datetime, timedelta
import calendar
import time

now = datetime.now()

print(now.date())
print(now.time())
print(now.year)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)

print(now.strftime("%a %A %d"))

print(now.strftime("%b %B %m"))

print(now.strftime("%a %B %d"))

print(now.strftime("%H : %M : %S %p"))

print(now.strftime("%y %Y"))

# Work with before and after times from a time

testDateAfter = now + timedelta(days=2)
testDateBefore = now - timedelta(weeks=3)

print(testDateAfter.date())
print(testDateBefore.date())

if testDateAfter > testDateBefore:
	print("Comparision works")

cal = calendar.month(2001, 10)
print(cal)

cal2 = calendar.weekday(2001, 10, 11)
print(cal2)

print(calendar.isleap(2000))

run = input("Start¿")

seconds = 1

if run == "yes":
	while seconds != 10:
		print(">", seconds)
		time.sleep(1)
		seconds += 1