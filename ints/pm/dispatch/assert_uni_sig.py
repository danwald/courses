import dispatch

class C1:
    @dispatch.register
    def func_int(self, x: int) -> int:
        return x

class C2:
    @dispatch.register
    def func_int(self, x: int) -> int:
        return x
