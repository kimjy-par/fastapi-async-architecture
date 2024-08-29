from dependency_injector import containers, providers

from app.core.database import Database
from app.repositories.user_repository import UserRepository
from app.repositories.post_repository import PostRepository
from app.repositories.tag_repository import TagRepository

from app.services.user_service import UserService
from app.services.post_service import PostService
from app.services.tag_service import TagService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.routers.user_router",
            "app.routers.post_router",
            "app.routers.tag_router",
        ]
    )

    # secret에 담아야하는 내용이나, 예제 코드이므로 하드코딩하였음
    db = providers.Singleton(
        Database, db_url="mariadb+aiomysql://root:root@localhost:3306/mnc_onboarding"
    )

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )
    post_repository = providers.Factory(
        PostRepository, session_factory=db.provided.session
    )
    tag_repository = providers.Factory(
        TagRepository, session_factory=db.provided.session
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
    post_service = providers.Factory(PostService, post_repository=post_repository)
    tag_service = providers.Factory(TagService, tag_repository=tag_repository)
