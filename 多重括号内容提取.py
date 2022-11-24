# 不校验括号的完整性
def get_text_in_brackets(text):
    tmp = []
    res = []
    for i in text:
        tmp.append(i)
        if i in ")）】」}]":
            tmp_res = ''
            j = tmp.pop()
            while j not in "(（【[{「":
                j = tmp.pop()
                if j in "(（【[{「": continue
                tmp_res+=j
            res.append(tmp_res[::-1])
    print(res)
    return res

get_text_in_brackets('(., P)(马兵., P)(天津市, A1)(静海区, A3)(主干二路四九传媒, A4)(15590445567, T)\n')

