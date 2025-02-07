import pytest

from lesson_07_testing.task_03_pytest_fixtures.src.managers.user_manager import UserManager
from lesson_07_testing.task_03_pytest_fixtures.src.models.user import User


@pytest.fixture
def user_manager_fixture():
    um = UserManager()
    um.add_user(User("Alice", 30))
    um.add_user(User("Bob", 25))
    return um


class TestUserManager:
    def test_get_list_users_method(self, user_manager_fixture):
        """
        Test getting whole list of users
        :param user_manager_fixture:
        :return:
        """
        assert 2 == len(user_manager_fixture.get_all_users())

    def test_remove_user_method(self, user_manager_fixture):
        """
        Test removing user by name from user list
        :param user_manager_fixture:
        :return:
        """
        user_manager_fixture.remove_user("Alice")
        assert 1 == len(user_manager_fixture.get_all_users())

    def test_add_user_method(self, user_manager_fixture):
        """
        Test add user method
        :param user_manager_fixture:
        :return:
        """
        new_user = User('Test', 22)
        user_manager_fixture.add_user(new_user)
        users_count = len(user_manager_fixture.get_all_users())

        assert new_user == user_manager_fixture.get_all_users()[users_count - 1]

    def test_remove_user_method_with_four_users(self, user_manager_fixture):
        """
        Test removing user by name from user list
        :param user_manager_fixture:
        :return:
        """
        if len(user_manager_fixture.get_all_users()) < 4:
            pytest.skip('It should be 3 users in the list at least')
        user_manager_fixture.remove_user("Alice")
        assert 1 == len(user_manager_fixture.get_all_users())
