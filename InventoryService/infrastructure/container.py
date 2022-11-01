from dependency_injector import containers, providers

from business.product_service import ProductService
from infrastructure.settings import Settings
from persistence.db_config import DbConfig
from persistence.product_repository import ProductRepository
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

    product_repository = providers.Singleton(
        ProductRepository,
        database_provider
    )

    product_service = providers.Factory(
        ProductService,
        product_repository
    )
