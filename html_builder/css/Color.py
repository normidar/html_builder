

class Color(Value):
    # 4 * 4 = 16 colors
    BLACK = 'black'
    GRAY = 'gray'
    SILVER = 'silver'
    WHITE = 'white'

    BLUE = 'blue'
    # 濃いブルー
    NAVY = 'navy'
    # 湖藍
    TEAL = 'teal'
    GREEN = 'green'

    # 明るい緑
    LIME = 'lime'
    AQUA = 'aqua'
    YELLOW = 'yellow'
    RED = 'red'

    FUCHSIA = 'fuchsia'
    OLIVE = 'olive'
    PURPLE = 'purple'
    MAROON = 'maroon'

    def __init__(self, value:str):
        self.value = value

    @classmethod
    def by_rgb(cls,r:int,g:int,b:int):
        rt = ''
        for i in (r, g, b):
            if i > 255 or i < 0:
                raise Exception('the rgb can not over and lower than 0')
            pr = hex(i)[2:]
            rt += pr if len(pr) == 2 else '0' + pr
        cls.value = '#' + rt

    def _get_str(self):
        return self.value