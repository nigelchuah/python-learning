# MIT Licensed
# https://github.com/exercism/python/blob/master/LICENSE
from calendar import day_name
from calendar import monthrange
from datetime import date

def weekdays_in_month(year, month, weekday):
    """Return list of all 4/5 dates with given weekday and year/month."""

    day_on_first, month_length = monthrange(year,month)
    first_date = (weekday - day_on_first)%7 +1
    return [
        date(year,month,day) 
        for day in range(first_date, month_length+1, 7)
    ]


def meetup_day(year, month, weekday, nth):
    
    if weekday.title() not in day_name:
        raise Exception(
            "Weekday not recognised. It should be Monday, Tuesday, Wednesday, etc."
            )
        
    weekday_names = list(day_name)
    shift_by = {'1st': 0, '2nd': 1, '3rd': 2, '4th': 3, '5th': 4, 'last': -1}   
    dates = weekdays_in_month(year, month, weekday_names.index(weekday.title()))
    
    if nth == 'teenth':
        return next(d for d in dates if d.day > 12)
    else:
        return dates[shift_by[nth]]
