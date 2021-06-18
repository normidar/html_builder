from .Value import Value

class BoxValue(Value):
    """1,全部　2,上下・左右　3,上・左右・下　4,上・右・下・左"""
    def __init__(self, *args:int):
        l = len(args)
        if l < 1 or l > 4:
            raise Exception('value over')
        self.args = args

    def _get_str(self):
        return ' '.join([str(x) + 'px' for x in self.args])
        
