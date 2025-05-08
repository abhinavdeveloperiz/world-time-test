from django.db import models
from django.utils import timezone
import pytz

class WorldClock(models.Model):
    uk_time = models.DateTimeField()  # Changed from TimeField to DateTimeField

    def get_time_for_timezone(self, timezone_str):
        target_timezone = pytz.timezone(timezone_str)
        return self.uk_time.astimezone(target_timezone)
    
    def __str__(self):
        return self.uk_time.strftime('%Y-%m-%d %H:%M:%S')  # Display UK time in a readable format