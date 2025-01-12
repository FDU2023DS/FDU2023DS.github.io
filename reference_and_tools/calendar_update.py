import datetime
from zoneinfo import ZoneInfo
import re

date=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
date = date.replace('+00:00',"+08:00',")

with open('_pages/calendar.md', 'r+', encoding='utf-8') as fp:
    lines=fp.readlines()
    flag=0
    for line in lines:
        if re.search(r'initialDate:', line):
            line = re.sub(r'....-..-..T..:..:.....:..*', date, line)
            lines[flag] = line
            break
        flag+=1
    fp.seek(0)
    fp.writelines(lines)
    fp.truncate()