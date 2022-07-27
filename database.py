import dataset

db = dataset.connect('sqlite:///db.sqlite3')
table = db['gold']
if not table.find_one(id=0):
    table.insert({'id':0, 'cnt': 0})

def get_gold_count():
    """ """
    return table.find_one(id=0)['cnt']

def inc_gold(count):
    """ """
    cnt = get_gold_count() + count
    table.update({'id': 0, 'cnt': cnt}, keys=['id'])

def des_gold(count):
    """ """
    cnt = get_gold_count() - count
    table.update({'id': 0, 'cnt': cnt}, keys=['id'])