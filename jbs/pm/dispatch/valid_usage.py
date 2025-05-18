from dispatch import register


class Portmind:
    def __str__(self):
        return f'{self.__class__.__name__}'

@register
def func_() -> None:
    pass

@register
def func_int(x: int) -> int:
    return x

@register
def func_float(x: float) -> float:
    return x

@register
def func_int_float(x: int, y: float) -> tuple[int, float]:
    return x,y

@register
def func_float_int(y: float, x: int) -> tuple[float, int]:
    return y,x

@register
def func_portmind(x: Portmind) -> Portmind:
    return x

func_()
func_int(1)
func_float(1.0)
func_int_float(1,1.0)
func_float_int(1.0,1)
func_portmind(Portmind())
