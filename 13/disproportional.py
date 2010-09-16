from xmlrpclib import ServerProxy, Error

server = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

print server.system.listMethods()
print server.system.methodSignature("phone")
print server.system.methodHelp("phone")
print server.phone("Bert")
