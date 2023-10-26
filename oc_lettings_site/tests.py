import pytest


@pytest.mark.django_db(transaction=True)
class TestResponse:
    """
    Testing app http responses
    """
    def test_index_should_status_code_ok(self, client):
        response = client.get('/')
        assert response.status_code == 200
        expected_content = 'Welcome to Holiday Homes'
        content = response.content.decode()
        # content.find() returns -1 if not found
        assert content.find(expected_content) != -1

    def test_unexisting_route_should_status_code_not_found(self, client):
        response = client.get('/gorgonzola/')
        assert response.status_code == 404

    def test_profiles_index_should_status_code_ok(self, client):
        response = client.get('/profiles/')
        assert response.status_code == 200
