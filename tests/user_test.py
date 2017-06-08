from lib.user_helper import UserAPI
from lib.utils import Utils


class TestUser:
    user_api = UserAPI()

    # Test case: List users
    def test_user_amount(self, expected=10):
        user_list_size = len(self.user_api.request_user_list())
        assert user_list_size == expected, "User list should be %s" %expected

    # Test case: Find a user by username
    def test_find_user(self, username="Bret", expected="Bret"):
        user_list = self.user_api.request_user_by_username(username)
        if len(user_list) > 0:
            user_finding = user_list[0]
        assert user_finding["username"] == expected, "User name should be %s" %expected

    # Test case: create a user
    def test_create_user(self, expected_status=201):
        user = {"name": "Kevin", "username": "kevinng", "email": "kevinng@april.biz","address": {"street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough","zipcode": "92998-3874","geo": {"lat": "-37.3159","lng": "81.1496"}},
    "phone": "1-770-736-8031 x56442","website": "hildegard.org", "company": {"name": "Romaguera-Crona","catchPhrase": "Multi-layered client-server neural-net","bs": "harness real-time e-markets"}}
        response = self.user_api.request_create_user(user)
        user_created = Utils.get_data_in_json(response)
        assert response.getcode() == expected_status, "Expected status should be %s" %expected_status
        assert user["username"] == user_created["username"]
        assert user["name"] == user_created["name"]

    # Test case: Update a user
    def test_update_user(self, old_user_name="Bret", new_name ="Kevin", expected_status=200):
        user_finding = self.user_api.request_user_by_username(old_user_name)
        user_id = user_finding["id"]
        data = {"name": new_name}
        response = self.user_api.request_update_user(user_id, data)
        assert response.getcode() == expected_status, "Expected status should be %s" %expected_status

    # Test case: Delete a user
    def test_delete_user(self, user_name="Bret", expected_status=200):
        user_list = self.user_api.request_user_by_username(user_name)
        if len(user_list) > 0:
            user_finding = user_list[0]
        user_id = user_finding["id"]
        response = self.user_api.request_delete_user(user_id)
        assert response.getcode() == expected_status, "Expected status should be %s" %expected_status

    # Test case: Find a user which not existing on sys
    def test_find_non_existed_user(self, username="hahaha", expected_user_list_size=0):
        user_list = self.user_api.request_user_by_username(username)
        assert len(user_list) == expected_user_list_size, "Expected user list size %s" %expected_user_list_size
