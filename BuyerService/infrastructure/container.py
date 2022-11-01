from dependency_injector import containers, providers
from persistence.buyer_repository import BuyerRepository
from business.buyer_service import BuyerService
from infrastructure.settings import Settings
from persistence.db_config import DbConfig
from persistence.buyer_repository import BuyerRepository
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

    buyer_repository = providers.Singleton(
        BuyerRepository,
        database_provider
    )

    buyer_service = providers.Factory(
        BuyerService,
        buyer_repository
    )

