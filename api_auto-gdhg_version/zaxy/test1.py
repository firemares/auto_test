import datetime
now = datetime.datetime.now() + datetime.timedelta(minutes=2)
print(now.strftime("%H:%M"))
