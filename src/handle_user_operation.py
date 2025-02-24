import os

from pymongo import MongoClient

from .handlers import (
    create_user,
    delete_user,
    get_user,
    get_user_aggregated_info,
    update_user,
)

# Create a new client and connect to the server
mongo_client = MongoClient(os.getenv("ATLAS_URI"))


def user_operation_handler(event, context):
    handler_function = get_handler_function(event, context)
    return handler_function(mongo_client, event, context)


def get_handler_function(event, context):
    http_method = event["context"]["http-method"]
    resource_path = event["context"]["resource-path"]
    match (http_method, resource_path):
        case ("POST", "/users"):
            return create_user
        case ("GET", "/users/{userId}"):
            return get_user
        case ("GET", "/users/{userId}/aggregated-info"):
            return get_user_aggregated_info
        case ("PUT" | "PATCH", "/users/{userId}"):
            return update_user
        case ("DELETE", "/users/{userId}"):
            return delete_user
    return return_invalid_method_response


def return_invalid_method_response(mongo_client, event, context):
    return {"statusCode": 400, "body": "Invalid method"}
