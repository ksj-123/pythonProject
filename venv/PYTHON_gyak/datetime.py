# # https://docs.python.org/3/library/datetime.html
# # object
# #     timedelta
# #     tzinfo
# #         timezone
# #     time
# #     date
# #         datetime

from datetime import datetime, timezone

print(datetime.now(timezone.utc))

#---

from datetime import datetime, data, time, timezone
nowutc = datetime.now(timezone.utc)
print(nowutc)
print(nowutc.date())
print(date(2000, 1, 1))

