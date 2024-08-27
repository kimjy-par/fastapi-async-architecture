from app.repositories.user_repository import UserRepository

from app.models.user import User


class UserService():
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_by_id(self, id: int) -> User:
        user: User = self.user_repository.get_by_id(id)
        #Session 밖에서는 db와 connection이 끊겨서 lazy loading이 안됨.
        #따라서 모델 정의 부분에 eager loading으로 설정
        #print([post.title for post in user.posts])
        return user
        