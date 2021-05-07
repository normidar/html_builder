from html_builder.ExistElement import ExistElement
from html_builder.Head.Head import Head
from html_builder.Body.Body import Body


class Html(ExistElement):
    def __init__(self, title: str):
        super().__init__()
        self.addElement(Head(title))
        self.body = Body()
        self.addElement(self.body)

    def _getEleKey(self):
        return 'html'

    def __str__(self):
        return '<!DOCTYPE html>' + super().__str__()