from django.conf import settings
from rest_framework_jwt import utils

def jwt_payload_handler(user):
    payload = utils.jwt_payload_handler(user)
    payload['role'] = user.role
    return payload