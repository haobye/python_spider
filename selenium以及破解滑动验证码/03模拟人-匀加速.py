# 滑动验证码：先拖动超过的距离，再拖动回来进入缺失部分，可以有效迷惑后台


def get_socket(distance):
    t = 0.2
    v = 0
    mid = distance * 3/5
    current = 0
    lst = []
    while current < distance:
        if current < mid:
            a = 3
        elif current > mid:
            a = -3
        v0 = v
        s = v0 * t + 0.5 * a * (t ** 2)
        current += s
        v = v0 + a * t
        lst.append(round(s))    # 函数round为四舍五入
    return lst


print(get_socket(165))


