from backend.models.business_request_model import BusinessRequest
from backend.crud import add_business_request

def save_bussiness_request(bussines_request: BusinessRequest):
    return add_business_request(business_request=bussines_request)