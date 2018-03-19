import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds011902.mlab.com:11902/quang_sbearfindingapp

host = "ds011902.mlab.com"
port = 11902
db_name = "quang_sbearfindingapp"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
