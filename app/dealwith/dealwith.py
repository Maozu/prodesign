from .facerec import getres
from .getans import JOJO
from .mysql import select


def main(base64):
    base64 = base64[23:].decode('utf-8')
    print(base64)
    # a = str(getres(url))
    # print(a)
    # a = JOJO(a)
    # li = []
    # if not a:
    #     li.append("他是好人哦")
    #     print("这是a哦")
    # else:
    #     for k in a:
    #         b = k[1]
    #         li.append(b)
    #         # li.append(select(k[0]))
    return base64




