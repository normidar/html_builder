from html_builder.html.Body import Input


# Single
class IpBoxS(Input):

    def _getType(self):
        return 'radio'


# Multiple
class IpBoxM(Input):

    def _getType(self):
        return 'checkbox'
