import re
from zipfile import ZipFile
pat = re.compile(r'Next nothing is (?P<nothing>\d+)')
nothing = '90052'
def linked_list(nt):
    nothing = nt
    comments = ''
    with ZipFile('channel.zip') as zf:
        while True:
            with open('channel/%s.txt'%nothing) as f:
                text = f.read()
            try:
                nothing = pat.search(text).groupdict()['nothing']
                comments += zf.getinfo('%s.txt'%nothing).comment.decode('utf-8')
            except Exception as e:
                print(e)
                print(text, nothing)
                break
    return comments
print(linked_list(nothing))