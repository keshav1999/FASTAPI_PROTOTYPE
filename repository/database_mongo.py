import pymongo
# from config.config import db_config_dev
# URI, collection_name = db_config_dev()



# from config.config import db_config
# local_url, local_collection = db_config()

# def pymongo_dev_db():
#     try:
#         from motor.motor_asyncio import AsyncIOMotorClient
#         client = AsyncIOMotorClient(URI)
#         database = client["khulkeV1"]
#         collection = database[collection_name]
#         return database, collection
#
#     except Exception as ex:
#         print("\nError At pymongo_db : ", str(ex))


def pymongo_dev_db():
    try:
        client = pymongo.MongoClient("")
        database = client["khulkeV1"]
        collection = database["users"]
        return database, collection

    except Exception as ex:
        print("\nError At pymongo_db : ", str(ex))

# def pymongo_db():
#     try:
#         client = pymongo.MongoClient(local_url)
#         # dblist = client.list_database_names()
#         # print("\ndblist : ", dblist)
#         database = client["Khulke"]
#         collection = database[local_collection]
#         return database, collection
#
#     except Exception as ex:
#         print("\nError At pymongo_db : ", str(ex))


