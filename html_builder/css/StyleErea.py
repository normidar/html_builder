from abc import ABCMeta, abstractmethod
from typing import List
from html_builder.css.Style.Style import Style
from . import CssObj

class StyleErea(CssObj,metaclass=ABCMeta):
    def __init__(self, aim:str, styles:List[Style]):
        self.aim = aim
        self.styles = styles

    def _get_str(self):
        stys_str = ''.join([str(x) for x in self.styles])
        return self.aim + '{' + stys_str + '}'
    