from html_builder.html.ExistElement import ExistElement
from html_builder.html.Head import Head
from html_builder.html.Body.Body import Body


class Html(ExistElement):
    def __init__(self, title: str):
        super().__init__()
        self.head = Head(title)
        self.addElement(self.head)
        self.body = Body()
        self.addElement(self.body)

    def _getEleKey(self):
        return 'html'

    def __str__(self):
        return '<!DOCTYPE html>' + super().__str__()
    
    def set_style(self, styles:list):
        stys_str = ''.join([str(x) for x in styles])
        self.head.addElement(ele) # html style ele を入れる


class SEOHtml(Html):
    def __init__(self,title: str,description: str):
        super().__init__(title)
        self.head.addElement(MDescription(description))
