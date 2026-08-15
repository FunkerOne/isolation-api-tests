from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from tests.tools.config.postgres import PostgresClientTestConfig


def get_postgres_test_session_factory(config: PostgresClientTestConfig) -> sessionmaker[Session]:
    """
    Фабрика создания sessionmaker для тестового слоя.
    """

    engine = create_engine(
        url=str(config.dsn),
        echo=config.echo,
        future=True,
        pool_pre_ping=True,
    )

    return sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
