import pytest
from profiles.models import Profile, User
from django.urls import reverse
import logging


@pytest.fixture
def create_user():
    User.objects.create(
        username='toto'
    )


@pytest.fixture
def create_profile(create_user):
    user = User.objects.get(id=1)
    Profile.objects.create(
        favorite_city='paris',
        user=user
    )


@pytest.mark.django_db
class TestModels:

    def test_create_user(self, create_user):
        user = User.objects.get(id=1)
        expected_value = 'toto'
        assert str(user) == expected_value

    def test_create_profile(self, create_profile):
        profile = Profile.objects.get(id=1)
        expected_value = 'toto'
        assert str(profile) == expected_value


@pytest.mark.django_db
class TestUrls:

    def test_profile_info_url(self, create_profile):
        path = reverse('profile', kwargs=({'username': 'toto'}))
        assert path == '/profiles/toto/'


@pytest.mark.django_db
class TestHttpResponse:

    @classmethod
    def setup_class(cls):
        # Disable logging for this test class
        logging.disable(logging.CRITICAL)

    @classmethod
    def teardown_class(cls):
        # Reenable logging after tests
        logging.disable(logging.NOTSET)

    def test_profiles_index_should_status_code_ok(self, client):
        response = client.get('/profiles/')
        assert response.status_code == 200

    def test_existing_profile_object_should_status_code_ok(self, client, create_profile):
        response = client.get('/profiles/toto/')
        assert response.status_code == 200
        expected_content = 'toto'
        content = response.content.decode()
        # content.find() returns -1 if not found
        assert content.find(expected_content) != -1

    def test_unexisting_profile_object_should_raise_HTTP404(self, client):
        """
        Note that create_profile fixture has not been used here
        """
        response = client.get('/profiles/toto/')
        assert response.status_code == 404
