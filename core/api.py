from ninja_extra import NinjaExtraAPI
from modules.users.controllers import UsersController
from modules.token.controller import TokenController
from ninja_jwt.authentication import JWTAuth

api = NinjaExtraAPI(
    title= "EcoVista API",
    version= "1.0.0",
    description= "Nossa API",
    app_name= "ecovista",
    auth=JWTAuth()
)

api.register_controllers(UsersController)

api.register_controllers(TokenController)