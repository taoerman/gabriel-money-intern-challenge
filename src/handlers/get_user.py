from bson import ObjectId


def get_user(mongo_client, event, context):
    collection = mongo_client.users.users
    try:
        user_id = ObjectId(event["params"]["path"]["userId"])
    except Exception as error:
        return {
            "statusCode": 400,
            "body": "Invalid user id",
            "errorMessage": str(error),
        }

    result = collection.find_one({"_id": user_id})
    if not result:
        return {
            "statusCode": 404,
            "body": "User id not found",
        }

    # Replace _id with string id because ObjectId is not JSON serializable
    result = {"userId": str(result.pop("_id"))} | result
    return {
        "statusCode": 200,
        "body": result,
    }
