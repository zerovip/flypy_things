import json

with open('flypy_n.json', 'r') as ori_file:
    ori_data = json.load(ori_file)
# 原始数据是按字排列，每个字后面跟着码

dic = {}    # 按码排序，每个码后面跟着能出现的字

def put(character, pinyin):
    if pinyin[0:4] in dic:
        dic[pinyin[0:4]].append(character + '(' + pinyin + ')')
    else:
        dic[pinyin[0:4]] = [character + '(' + pinyin + ')']

check_ms = []   # 看看那些带 “-” 和 “*” 号的是不是都是有重字的码
# 如果不是就记进来

def check_m_s(character, pinyin):
    if ("-" in pinyin) or ("*" in pinyin):
        if len(dic[pinyin[0:4]]) == 1:
            if character[0] == dic[pinyin[0:4]][0][0]:
                check_ms.append(pinyin + character)
                return character[2]
            else:
                print("这就有点奇怪了哦！")
                return 0
        else:
            return 0
    else:
        return 0

level = ''  # 字的等级，字分 1、2、3 级
multi = 0   # 多音（码）字计数
single = 0  # 单音（码）字计数
for i in ori_data:
    level = i["level"]
    code_ori = i["fly_code"]
    character = i["character"] + "(" + level + ")"
    if ' ' in code_ori:
        l = code_ori.split(' ')
        multi = multi + 1
        for j in l:
            put(character, j)
    else:
        single = single + 1
        put(character, code_ori)

check3 = {} # 有重字的那些码的前三码检查
l1 = 0
l2 = 0
l3 = 0
for i in ori_data:
    level = i["level"]
    code_ori = i["fly_code"]
    character = i["character"] + "(" + level + ")"
    if ' ' in code_ori:
        l = code_ori.split(' ')
        for j in l:
            lc = check_m_s(character, j)
    else:
        lc = check_m_s(character, code_ori)
    if lc == "1":
        l1 += 1
    elif lc == "2":
        l2 += 1
    elif lc == "3":
        l3 += 1

result = {}
unique = 0  # 无重字的码
non_unique = 0  # 有重字的码
dist = {}   # 重码分布
for key, value in dic.items():
    if len(value) == 1:
        unique = unique + 1
    else:
        non_unique = non_unique + 1
        if key[0:3] in check3:
            # 前三码的分布也做个字典，键是前三码，值是一个列表，
            # 列表的每一项都是该四键全码（以键为前三码）的候选字的数量
            check3[key[0:3]].append(str(len(value)))
        else:
            check3[key[0:3]] = [str(len(value))]
        if len(value) in dist:
            # 重码的分布情况做个字典，键是候选字的数目，值是一个列表，
            # 列表里的元素都是字符串，用 “:” 隔开，
            # 冒号前面是四键全码（该四键全码能打出键值那么多个候选字）
            # 冒号后面是其所有候选字
            dist[len(value)].append(key + ': ' + ''.join(value))
        else:
            dist[len(value)] = [key + ': ' + ''.join(value)]

check3_out = []     # 有重字的码的前三码的重复情况
for k, v in check3.items():
    if len(v) == 1:
        pass
    else:
        check3_out.append(k + '(' + ''.join(v) + ')')

result["重码分布"] = dist
for key, value in dist.items():
    result["候选字有 " + str(key) + " 个的码"] = len(value)
result["有重的码的数量（按完四个码后需要候选）"] = non_unique
result["无重的码的数量（按完四个码后直接上屏）"] = unique
result["码的总数"] = len(dic)
result["多音（码）字的个数"] = multi
result["单音（码）字的个数"] = single
result["有重码的那 " + str(non_unique) + " 个取前三码后的重码分布"] = check3_out
result["有重码的那 " + str(non_unique) + " 个取前三码后的重码数"] = len(check3_out)
result["带 - 和 * 号却无重字的码"] = check_ms
result["带 - 和 * 号却无重字的码的个数"] = len(check_ms)
result["其中一级字有"] = str(l1)
result["其中二级字有"] = str(l2)
result["其中三级字有"] = str(l3)

with open ('result.json', 'w') as new_file:
    json.dump(result, new_file, ensure_ascii=False, indent=2)

