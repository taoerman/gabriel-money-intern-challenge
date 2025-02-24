import mongomock

from handlers import create_user


def test_create_user():
    mongo_client = mongomock.MongoClient()
    user_to_create = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone_number": "+19709456544",
    }
    event = {"params": {"querystring": user_to_create}}
    context = {}

    response = create_user(mongo_client, event, context)

    assert response["statusCode"] == 200
    assert "userId" in response["body"]
    user_in_db = mongo_client.users.users.find_one(
        {"_id": mongomock.ObjectId(response["body"]["userId"])}
    )
    assert user_in_db == user_to_create
