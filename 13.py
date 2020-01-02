from xmlrpc.client import ServerProxy
server = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(server.phone('Bert'))