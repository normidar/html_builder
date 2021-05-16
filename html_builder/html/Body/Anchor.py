from html_builder.html.ExistElement import ExistElement


class Anchor(ExistElement):
    def __init__(self, url: str, to_url=False):
        super().__init__()
        if to_url:
            if url[:8] != 'https://':
                if url[:7] != 'http://':
                    url = 'https://' + url
        self.__href = url
        self.__attrs = {}

    @classmethod
    def linkToId(cls, id: str):
        super().__init__()
        cls.__href = f'#{id}'

    def _getAttrs(self):
        self.__attrs['href'] = self.__href
        return self.__attrs

    def _getEleKey(self):
        return 'a'

    def nofollow(self,nofollow = True , sponsored = False, ugc = False):
        rel = []
        if nofollow:
            rel.append('nofollow')
        if sponsored:
            rel.append('sponsored')
        if ugc:
            rel.append('ugc')
        rel = ' '.join(rel)
        self.__attrs['rel'] = rel

