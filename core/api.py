from ninja import Swagger
from ninja_extra import NinjaExtraAPI
from modules.users.controllers import UsersController
from modules.token.controller import TokenController
from ninja_jwt.authentication import JWTAuth
from django.contrib.admin.views.decorators import staff_member_required

api = NinjaExtraAPI(
    title= "EcoVista API",
    version= "1.0.0",
    description= "Nossa API",
    app_name= "ecovista",
    auth=JWTAuth(),
    docs_decorator=staff_member_required,
    docs=Swagger(
        settings={
            'docExpansion': 'none',
            'tagsSorter': 'alpha',
            'filter': True,
            'syntaxHighlight': {
                'theme': 'monokai',
                'activate': True,
            },
            'persistAuthorization': True,
        }
    )
)

api.register_controllers(UsersController)

api.register_controllers(TokenController)