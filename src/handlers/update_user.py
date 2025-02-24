from bson import ObjectId


def update_user(mongo_client, event, context):
    collection = mongo_client.users.users
    try:
        user_id = ObjectId(event["params"]["path"]["userId"])
    except Exception as error:
        return {
            "statusCode": 400,
            "body": "Invalid user id",
            "errorMessage": str(error),
        }

    updates = event["params"]["querystring"]
    if not updates:
        return {
            "statusCode": 400,
            "body": "No updates provided",
        }
    update_result = collection.update_one({"_id": user_id}, {"$set": updates})
    if update_result.matched_count == 0:
        return {
            "statusCode": 404,
            "body": "User id not found",
        }

    read_result = collection.find_one({"_id": user_id})
    # Replace _id with string id because ObjectId is not JSON serializable
    read_result = {"userId": str(read_result.pop("_id"))} | read_result
    return {
        "statusCode": 200,
        "body": read_result,
    }
