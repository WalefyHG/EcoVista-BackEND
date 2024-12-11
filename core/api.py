from ninja import Swagger
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from django.contrib.admin.views.decorators import staff_member_required


# Import Controllers

from modules.users.controllers import UsersController
from modules.token.controller import TokenController
from modules.biomes.controllers import BiomesController
from modules.picture.controllers import PictureController

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

# User Controllers
api.register_controllers(UsersController)

# Core Controllers
api.register_controllers(TokenController)

# Biomes Contollers
api.register_controllers(BiomesController)

# Picture Controllers
api.register_controllers(PictureController)