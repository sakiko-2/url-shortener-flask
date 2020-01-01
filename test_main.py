from urlshort import create_app

def test_get_short_code(client):
    response = client.get('/')
    assert b'Get Short Code' in response.data
