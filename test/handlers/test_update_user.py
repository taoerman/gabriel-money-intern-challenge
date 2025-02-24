import mongomock
from bson import ObjectId

from handlers import update_user


def test_update_user_invalid_user_id():
    mongo_client = mongomock.MongoClient()
    invalid_user_id = "invalid_user_id"
    event = {"params": {"path": {"userId": invalid_user_id}}}
    context = {}

    response = update_user(mongo_client, event, context)

    assert response["statusCode"] == 400
    assert response["body"] == "Invalid user id"


def test_update_user_no_updates_provided():
    mongo_client = mongomock.MongoClient()
    # Insert the user so it can be updated
    insert_result = mongo_client.users.users.insert_one(
        {
            "_id": ObjectId(),
            "first_name": "John",
            "last_name": "Doe",
        }
    )
    event = {
        "params": {
            "querystring": {},
            "path": {"userId": str(insert_result.inserted_id)},
        }
    }
    context = {}

    response = update_user(mongo_client, event, context)

    assert response["statusCode"] == 400
    assert response["body"] == "No updates provided"


def test_update_user_user_id_not_found():
    mongo_client = mongomock.MongoClient()
    non_existent_user_id = ObjectId()
    event = {
        "params": {
            "querystring": {"first_name": "John"},
            "path": {"userId": str(non_existent_user_id)},
        }
    }
    context = {}

    response = update_user(mongo_client, event, context)

    assert response["statusCode"] == 404
    assert response["body"] == "User id not found"


def test_update_user_success():
    mongo_client = mongomock.MongoClient()
    # Insert the user so it can be updated
    insert_result = mongo_client.users.users.insert_one(
        {
            "_id": ObjectId(),
            "first_name": "John",
            "last_name": "Doe",
        }
    )
    event = {
        "params": {
            "querystring": {"first_name": "Alice"},
            "path": {"userId": str(insert_result.inserted_id)},
        }
    }
    context = {}

    response = update_user(mongo_client, event, context)

    assert response["statusCode"] == 200
    assert response["body"] == {
        "userId": str(insert_result.inserted_id),
        "first_name": "Alice",
        "last_name": "Doe",
    }
