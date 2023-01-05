from urllib.parse import parse_qsl
def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    return dict(parse_qsl(query, separator=";"))

if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=U&ser;age=28;') == {'name': 'Dima=U&ser', 'age': '28'}
    assert parse_cookie("v=vJ5dZ0uJpMY;") == {"v": "vJ5dZ0uJpMY"}
    assert parse_cookie(" ") == {}
    assert parse_cookie("highlight=params") == {"highlight": "params"}
    assert parse_cookie("attr!action=birthday") == {"attr!action": "birthday"}
    assert parse_cookie("bedroom=bike&basket=airport:;") == {"bedroom": "bike&basket=airport:"}
    assert parse_cookie("23!@a=bik12e;basket==airport") == {'23!@a': 'bik12e', 'basket': '=airport'}
    assert parse_cookie("aftermath=amusement;believe=aunt") == {'aftermath': 'amusement', 'believe': 'aunt'}
    assert parse_cookie("=bottle") == {'': 'bottle'}
    assert parse_cookie("base=badge;birthday=basketball") == {"base": "badge", "birthday": "basketball"}
    assert parse_cookie("acoustics=beds;blade=babies") == {"acoustics": "beds", "blade": "babies"}
