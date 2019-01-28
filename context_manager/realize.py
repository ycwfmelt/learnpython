class ContextIllustration:
    def __enter__(self):
        print("进入上下文管理器")

    def __exit__(self, exc_type, exc_value, traceback):
        print("离开上下文管理器")

        if exc_type is None:
            print("没有发生错误")
        else:
            print("发生了一个错误：{}".format(exc_value))


if __name__ == "__main__":
    with ContextIllustration():
        print("inside")
    
    with ContextIllustration():
        raise RuntimeError("raise within 'with'")
