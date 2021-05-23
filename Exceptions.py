class StraightIsParallelError(Exception):
    """Исключение возникает, когда прямые оказываются параллельны, то есть не имеют точек пересечения """

    def __init__(self):
        super().__init__("Прямые параллельны и не имеют точки пересечения")


class StraightIsEqualError(Exception):
    """Исключение возникает, когда прямые совпадают. И прямые имеют бесконечное множество точек пересечения"""

    def __init__(self):
        super().__init__("Прямые совпадают")


#try:
#    raise StraightIsEqualError()
#except Exception as e:
#    print(e)
        