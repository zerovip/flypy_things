import json
import re

with open('flypy.json', 'r') as ori_file:
    ori_data = json.load(ori_file)

new_data = []
level = "0"

for i in ori_data:
    if i[0][0] == "#":
        level = i[0][1]
        continue
    else:
        pass
    d = {
        "character": i[6],
        "level": level,
        "fly_code": re.search(r'：\u3000\u3000(.*)$' ,i[0]).group(1),
        "order": i[1],
        "first_part": i[2],
        "first_py": i[4],
        "last_part": i[3],
        "last_py": i[5],
        }
    new_data.append(d)

with open ('flypy_n.json', 'w') as new_file:
    json.dump(new_data, new_file, ensure_ascii=False, indent=2)

