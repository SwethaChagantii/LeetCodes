import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_time = datetime.datetime(year,month,day)
        day_of_week = date_time.weekday()
        week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return week_days[day_of_week % 7]

        
        