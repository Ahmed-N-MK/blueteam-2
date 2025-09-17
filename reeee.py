import re

date = "Logins on 2025-09-16 and 2025/09/15"

date_ = re.findall(r'\d+\W\d+\W\d+', date)

print(date_)