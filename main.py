from urllib.parse import parse_qsl, urlparse
def parse(query: str) -> dict:
    return dict(parse_qsl(urlparse(query).query))

if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse("https://www.youtube.com/watch?v=vJ5dZ0uJpMY") == {'v': 'vJ5dZ0uJpMY'}
    assert parse("https://lms.ithillel.ua/groups/634317c22fa78f4b3a6fd66c/homeworks/63ab49bedd0ec14f08fb1d8f") == {}
    assert parse("http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing") == {'highlight': 'params'}
    assert parse("http://www.example.com/basket?attr!action=birthday") == {'attr!action': 'birthday'}
    assert parse("http://www.example.com/?bedroom=bike&basket=airport") == {"bedroom": "bike", "basket": "airport"}
    assert parse("http://www.example.com/?123!@a=bik12e&basket==airport") == {'123!@a': 'bik12e', 'basket': '=airport'}
    assert parse("http://www.example.com/?aftermath=amusement&believe=aunt") == {'aftermath': 'amusement', 'believe': 'aunt'}
    assert parse("http://bells.example.com/amusement/bee.htm?border=bottle") == {"border": "bottle"}
    assert parse("http://www.example.com/?base=badge&birthday=basketball") == {"base": "badge", "birthday": "basketball"}
    assert parse("https://example.com/agreement/brick.php?acoustics=beds&blade=babies") == {"acoustics": "beds", "blade": "babies"}

def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
