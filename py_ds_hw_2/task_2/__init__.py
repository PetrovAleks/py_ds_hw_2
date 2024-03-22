import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["customers"]
new_customer = {
    "name": "barsik",
    "age": 3,
    "features": ["ходить в капці", "дає себе гладити", "рудий"]
}

def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кот с именем {name} не найден")

def update_cat_age(name, new_age):
    query = {"name": name}
    new_values = {"$set": {"age": new_age}}
    result = collection.update_one(query, new_values)
    print(f"Обновлено {result.modified_count} записей")

def add_cat_feature(name, new_feature):
    query = {"name": name}
    new_values = {"$push": {"features": new_feature}}
    result = collection.update_one(query, new_values)
    print(f"Обновлено {result.modified_count} записей")


def delete_cat_by_name(name):
    query = {"name": name}
    result = collection.delete_one(query)
    print(f"Удалено {result.deleted_count} записей")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"Удалено {result.deleted_count} записей")



def init():
    collection.insert_one(new_customer)
    read_all_cats()
    read_cat_by_name("barsik")
    update_cat_age("barsik", 4)
    add_cat_feature("barsik", "принимает ванну")
    delete_cat_by_name("barsik")
    delete_all_cats()
    client.close()