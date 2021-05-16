from html_builder.html.Body import Input


class IpText(Input):
    def _getType(self):
        return 'text'


class IpPassword(Input):
    def _getType(self):
        return 'password'
