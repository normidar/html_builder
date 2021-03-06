from html_builder.html.ExistElement import ExistElement
from html_builder.html.Title import Title
from html_builder.html.Meta import MCharset


class Head(ExistElement):
    def _getEleKey(self):
        return 'head'

    def __init__(self, title: str):
        super().__init__()
        self.title = title
        self.addElement(MCharset())
        self.addElement(Title(title))
