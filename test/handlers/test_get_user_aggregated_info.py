import mongomock

from handlers import get_user_aggregated_info


def test_get_user_aggregated_info():
    mongo_client = mongomock.MongoClient()
    event = {}
    context = {}

    response = get_user_aggregated_info(mongo_client, event, context)

    assert response["statusCode"] == 200
    assert "userInfo" in response["body"]
    assert "accountInfo" in response["body"]
    assert "cardInfo" in response["body"]
    assert "transactionsInfo" in response["body"]
