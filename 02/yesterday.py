import datetime

def yesterdaydate():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterd = today - oneday
    return yesterd


#输出
print(yesterdaydate())

#输出昨天的日期
