# 把不标准的日期格式都改成标准的2022-9-7格式

import re

content = "这次，我看2022/09/07到了草原，这里的天2022.09.07比别处的更可爱，\n空气是那么清鲜，\
天空是那么明朗，\n是我总07.09.2022想高歌一曲，表示07/09/2022我满心的愉快。"

content = re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\1-\2-\3", content)
print(content)

content = re.sub(r"(\d{4}).(\d{2}).(\d{2})", r"\1-\2-\3", content)
print(content)

content = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", content)
print(content)

content = re.sub(r"(\d{2}).(\d{2}).(\d{4})", r"\3-\2-\1", content)
print(content)
