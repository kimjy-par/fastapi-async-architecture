from dependency_injector import containers, providers

from app.core.database import Database
from app.repositories.user_repository import UserRepository

from app.services.user_service import UserService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.routers.routers",
        ]
    )

    # secret에 담아야하는 내용이나, 예제 코드이므로 하드코딩하였음
    db = providers.Singleton(Database, db_url="mariadb+aiomysql://root:root@localhost:3306/mnc_onboarding")
     
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)
    #post_repository = providers.Factory(PostRepository, session_factory=db.provided.session)

    #async_post_repository = providers.Factory(AsyncPostRepository, session_factory=db.provided.session)

    user_service = providers.Factory(UserService, user_repository=user_repository)
    #post_service = providers.Factory(PostService, post_repository=post_repository)

    #async_post_service = providers.Factory(AsyncPostService, post_repository=async_post_repository)
