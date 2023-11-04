import pytest
from lettings.models import Letting, Address
from django.urls import reverse
import logging


@pytest.fixture
def create_address():
    Address.objects.create(
        number=1,
        street='avenue de la république',
        city='paris',
        state='france',
        zip_code=92190,
        country_iso_code='fra'
    )


@pytest.fixture
def create_letting(create_address):
    address = Address.objects.get(id=1)
    Letting.objects.create(
        title='grande maison',
        address=address
    )


@pytest.mark.django_db
class TestModels:

    def test_create_address(self, create_address):
        address = Address.objects.get(id=1)
        expected_value = '1 avenue de la république'
        assert str(address) == expected_value

    def test_create_letting(self, create_letting):
        letting = Letting.objects.get(id=1)
        expected_value = 'grande maison'
        assert str(letting) == expected_value


@pytest.mark.django_db
class TestUrls:

    def test_letting_info_url(self, create_letting):
        path = reverse('letting', kwargs=({'letting_id': 1}))
        assert path == '/lettings/1/'


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

    def test_lettings_index_should_status_code_ok(self, client):
        response = client.get('/lettings/')
        assert response.status_code == 200

    def test_existing_letting_object_should_status_code_ok(self, client, create_letting):
        response = client.get('/lettings/1/')
        assert response.status_code == 200
        expected_content = 'grande maison'
        content = response.content.decode()
        # content.find() returns -1 if not found
        assert content.find(expected_content) != -1

    def test_unexisting_letting_object_should_raise_HTTP404(self, client):
        """
        Note that create_letting fixture has not been used here
        """
        response = client.get('/lettings/1/')
        assert response.status_code == 404
