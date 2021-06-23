import datetime

date_inputed = input()
date_inputed = date_inputed.split("/")
day = int(date_inputed[0])
month = int(date_inputed[1])
year = int(date_inputed[2])

date_returned = datetime.date(year, month, day)
date_returned += datetime.timedelta(days=1)

print(date_returned.strftime("%d/%m/%Y"))
