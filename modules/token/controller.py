from ninja_extra import api_controller, route
from ninja_extra.controllers import ControllerBase
from .schemas import CustomTokenObtain, CustomTokenOutObtain


@api_controller(
    "/token",
    tags=["Token"],
)

class TokenController(ControllerBase):
    
    @route.post("/login", response={200: CustomTokenOutObtain})
    def login(self, request, payload: CustomTokenObtain):
        
        payload = payload.check_user_authentication_rule()
        
        token = payload.output_schema()
        
        return token