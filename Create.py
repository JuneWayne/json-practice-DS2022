import json

myvals = [{"repo_name":"json-practice", "repo_url":"https://github.com/nmagee/json-practice/"}, {"repo_name":"fastapi-demo", "repo_url":"https://github.com/nmagee/fastapi-demo/"}]
myjson = json.dumps(myvals)

first = ('sape', 4139)
second = ('guido', 4127)
third = ('jack', 4098)

# combine tuples into list. Can .append one by one or .extend all at once
mylist = []
mylist.extend((first, second, third))

# convert to dict
mydict = dict(mylist)
mydict

# convert to JSON
myjson = json.dumps(mydict)
myjson