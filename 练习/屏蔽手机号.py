# 屏蔽手机号，改成1**********

import re

str1 = "这次，我看18912252972到了草原，这里的天584546比别处的更可爱，\n空气是那么清鲜，\
天空是那么明朗，\n是我总15365546322想高歌一曲，表示我12345满心的愉快。"

print(re.sub(r"1[1-9]\d{9}", r"1**********", str1))