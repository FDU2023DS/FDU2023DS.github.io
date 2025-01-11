from datetime import datetime
from zoneinfo import ZoneInfo
import re

current_datetime = datetime.now()
timezone = ZoneInfo("Asia/Shanghai")
current_datetime_in_timezone = current_datetime.astimezone(timezone)
date = str(current_datetime_in_timezone.date())

with open('_pages/calendar.md', 'r+', encoding='utf-8') as fp:
    lines=fp.readlines()
    flag=0
    for line in lines:
        if re.search(r'initialDate:', line):
            line = re.sub(r'....-..-..', date, line)
            lines[flag] = line
            break
        flag+=1
    fp.seek(0)
    fp.writelines(lines)
    fp.truncate()