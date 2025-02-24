from bson import ObjectId


def delete_user(mongo_client, event, context):
    collection = mongo_client.users.users
    try:
        user_id = ObjectId(event["params"]["path"]["userId"])
    except Exception as error:
        return {
            "statusCode": 400,
            "body": "Invalid user id",
            "errorMessage": str(error),
        }

    result = collection.delete_one({"_id": user_id})
    if result.deleted_count == 0:
        return {
            "statusCode": 404,
            "body": "User id not found",
        }
    return {
        "statusCode": 200,
        "body": {
            "message": "User deleted successfully",
        },
    }
