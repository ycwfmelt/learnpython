"""
for...else...
在 for 循环中找到了，就正常退出(break)
没有找到(不是通过 break 退出循环)，就执行 else
"""


def f(ham: str, eggs: str = "eggs") -> str:
    pass


if __name__ == "__main__":
    # find 'sukinaso'
    oshi = ["cocoa", "piyo", "ayumin"]
    for i, member in enumerate(oshi):
        if member == "sukinaso":
            print("find 好きなそ　in {} position".format(i))
    else:
        print("好きなそがいない")

    print(f.__annotations__)

