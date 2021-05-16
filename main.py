from html_builder.html import Html, Heading, Text, Anchor

import sys


def test_1():
    html = Html('abc')
    html.body.addElement(Heading(1).text('标<题'))\
        .addElement(Text('asdfasdf'))
    return write(html)


def test_2():
    html = Html('abc')
    body = html.body
    body.addElement(Anchor('google.com').text('ググって'))
    return write(html)


def write(html):
    print(html)
    # soup = BeautifulSoup(str(html), 'html.parser')
    # html = soup.prettify()
    with open('index.html', 'w') as f:
        f.write(str(html))
    return html


def main(params: list):
    if len(params) == 3:
        if params[1] == '-t':
            if params[2] == '1':
                return test_1()
            if params[2] == '2':
                return test_2()
    elif len(params) == 1:
        return test_1()
    return '命令不存在'


if __name__ == '__main__':
    params = sys.argv
    print(main(params))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
