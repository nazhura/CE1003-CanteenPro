import datetime


def compareTime(timing):
    nowTiming = datetime.datetime.now()
    startBreakfastTime = "07:00:00"
    startbreakfastTiming = datetime.datetime.strptime(startBreakfastTime, "%H:%M:%S")
    startbreakfastTiming = nowTiming.replace(hour=startbreakfastTiming.time().hour,
                                             minute=startbreakfastTiming.time().minute,
                                             second=startbreakfastTiming.time().second, microsecond=0)

    endBreakfastTime = "11:00:00"
    endbreakfastTiming = datetime.datetime.strptime(endBreakfastTime, "%H:%M:%S")
    endbreakfastTiming = nowTiming.replace(hour=endbreakfastTiming.time().hour, minute=endbreakfastTiming.time().minute,
                                           second=endbreakfastTiming.time().second, microsecond=0)

    startClosingTime = "22:00:00"
    startClosingTiming = datetime.datetime.strptime(startClosingTime, "%H:%M:%S")
    startClosingTiming = nowTiming.replace(hour=startClosingTiming.time().hour, minute=startClosingTiming.time().minute,
                                           second=startClosingTiming.time().second, microsecond=0)

    if (startbreakfastTiming and endBreakfastTime < nowTiming < startClosingTiming):
        print("It's LUNCH time")





