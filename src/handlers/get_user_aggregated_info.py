from security import safe_requests

BASE_URL = "https://dev.api.gabriel.money/backend-challenge/{type}/{{user_id}}"
USER_URL = BASE_URL.format(type="user")
ACCOUNTS_URL = BASE_URL.format(type="accounts")
CARDS_URL = BASE_URL.format(type="cards")
TRANSACTIONS_URL = BASE_URL.format(type="transactions")


def get_user_aggregated_info(mongo_client, event, context):
    # The user_id is fixed for testing purposes.
    # In practice we should read user_id from event.
    user_id = "375b799c-d2d4-4290-ba8a-3f32d4f5ca92"

    user_response = safe_requests.get(USER_URL.format(user_id=user_id))
    accounts_response = safe_requests.get(ACCOUNTS_URL.format(user_id=user_id))
    cards_response = safe_requests.get(CARDS_URL.format(user_id=user_id))
    transactions_response = safe_requests.get(TRANSACTIONS_URL.format(user_id=user_id))

    return {
        "statusCode": 200,
        "body": {
            "userInfo": user_response.json(),
            "accountInfo": accounts_response.json(),
            "cardInfo": cards_response.json(),
            "transactionsInfo": transactions_response.json(),
        },
    }
