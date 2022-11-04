from dependency_injector import containers, providers

from business.order_service import OrderService
from infrastructure.settings import Settings
from persistence.db_config import DbConfig
from persistence.order_repository import OrderRepository
from persistence.postgres_connection import PostgresConnection


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_pydantic(Settings('./infrastructure/.env'))

    database_config = providers.Singleton(
        DbConfig,
        host=config.postgres_host,
        user=config.postgres_user,
        password=config.postgres_password,
        database=config.postgres_database
    )

    database_provider = providers.Singleton(
        PostgresConnection,
        database_config
    )

    order_repository = providers.Singleton(
        OrderRepository,
        database_provider
    )

    order_service = providers.Factory(
        OrderService,
        order_repository
    )
