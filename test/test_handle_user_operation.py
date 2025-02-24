import mongomock

from src.handle_user_operation import (
    get_handler_function,
    return_invalid_method_response,
)
from src.handlers import (
    create_user,
    delete_user,
    get_user,
    get_user_aggregated_info,
    update_user,
)


def test_get_handler_function():
    test_cases = [
        {
            "http_method": "POST",
            "resource_path": "/users",
            "expected_function": create_user,
        },
        {
            "http_method": "GET",
            "resource_path": "/users/{userId}",
            "expected_function": get_user,
        },
        {
            "http_method": "PUT",
            "resource_path": "/users/{userId}",
            "expected_function": update_user,
        },
        {
            "http_method": "PATCH",
            "resource_path": "/users/{userId}",
            "expected_function": update_user,
        },
        {
            "http_method": "DELETE",
            "resource_path": "/users/{userId}",
            "expected_function": delete_user,
        },
        {
            "http_method": "GET",
            "resource_path": "/users/{userId}/aggregated-info",
            "expected_function": get_user_aggregated_info,
        },
        {
            "http_method": "GET",
            "resource_path": "/users",
            "expected_function": return_invalid_method_response,
        },
    ]

    for case in test_cases:
        event = {
            "context": {
                "http-method": case["http_method"],
                "resource-path": case["resource_path"],
            }
        }
        context = {}
        handler_function = get_handler_function(event, context)
        assert handler_function == case["expected_function"]
