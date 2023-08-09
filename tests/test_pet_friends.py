from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends

def get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.ger_api_key()
    assert status == 200
    assert 'key' in result

