class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutesAngle = minutes * 6 # 一分鐘6度
        hourAngle = ((hour+minutes/60) %12) *30 # 一小時 
        if minutesAngle > hourAngle:
            hourAngle , minutesAngle = minutesAngle , hourAngle
        return min(hourAngle - minutesAngle , minutesAngle+360-hourAngle)