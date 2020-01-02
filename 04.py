import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
pat = re.compile(r'and the next nothing is (?P<nothing>\d+)')
nothing = '12345'
def linked_list(nt):
    nothing = nt
    while True:
        text = requests.get(url, params={'nothing': nothing}).text
        try:
            nothing = pat.search(text).groupdict()['nothing']
        except Exception as e:
            print(e)
            print(nothing, text)
            break
    return nothing
nothing = linked_list(nothing)
nothing = int(nothing)/2
nothing = linked_list(nothing)
