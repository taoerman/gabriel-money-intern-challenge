import mongomock
from bson import ObjectId

from handlers import get_user


def test_get_user_invalid_user_id():
    mongo_client = mongomock.MongoClient()
    invalid_user_id = "invalid_user_id"
    event = {"params": {"path": {"userId": invalid_user_id}}}
    context = {}

    response = get_user(mongo_client, event, context)

    assert response["statusCode"] == 400
    assert response["body"] == "Invalid user id"


def test_get_user_user_id_not_found():
    mongo_client = mongomock.MongoClient()
    non_existent_user_id = ObjectId()
    event = {"params": {"path": {"userId": str(non_existent_user_id)}}}
    context = {}

    response = get_user(mongo_client, event, context)

    assert response["statusCode"] == 404
    assert response["body"] == "User id not found"


def test_get_user_success():
    mongo_client = mongomock.MongoClient()
    # Insert the user so it can be retrieved
    insert_result = mongo_client.users.users.insert_one(
        {
            "_id": ObjectId(),
            "first_name": "John",
            "last_name": "Doe",
        }
    )
    event = {"params": {"path": {"userId": str(insert_result.inserted_id)}}}
    context = {}

    response = get_user(mongo_client, event, context)

    assert response["statusCode"] == 200
    assert response["body"] == {
        "userId": str(insert_result.inserted_id),
        "first_name": "John",
        "last_name": "Doe",
    }
