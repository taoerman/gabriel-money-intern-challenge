def create_user(mongo_client, event, context):
    user_info = event["params"]["querystring"]
    collection = mongo_client.users.users
    result = collection.insert_one(user_info)
    return {
        "statusCode": 200,
        "body": {
            "userId": str(result.inserted_id),
        },
    }
