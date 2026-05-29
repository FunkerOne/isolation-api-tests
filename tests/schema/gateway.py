from pydantic import BaseModel

from tests.schema.accounts import AccountTestSchema
from tests.schema.cards import CardTestSchema
from tests.schema.users import UserTestSchema


class UserDetailsTestSchema(BaseModel):
    """
    Тестовая схема деталей пользователя.
    """

    user: UserTestSchema
    accounts: list[AccountTestSchema]


class GetUserDetailsResponseTestSchema(BaseModel):
    """
    Схема ответа API при получении деталей пользователя.
    """

    details: UserDetailsTestSchema


class AccountDetailsTestSchema(BaseModel):
    """
    Тестовая схема деталей банковского счёта.
    """

    cards: list[CardTestSchema]
    account: AccountTestSchema


class GetAccountDetailsResponseTestSchema(BaseModel):
    """
    Схема ответа API при получении деталей счёта.
    """

    details: AccountDetailsTestSchema
