from dependency_injector import containers, providers
from business.merchant_service import MerchantService

from infrastructure.settings import Settings
from persistence.db_config import DbConfig
from persistence.merchant_repository import MerchantRepository
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

	merchant_repository = providers.Singleton(
		MerchantRepository,
		database_provider
	)

	merchant_service = providers.Factory(
		MerchantService,
		merchant_repository
	)