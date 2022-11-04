from business.product_service import ProductService


class Events:
	def __init__(self, product_service: ProductService):
		self.__service = product_service

	def remove_reservation(self, product_id: int):
		return self.__service.unreserve_product(product_id)

	def sell_item(self, product_id: int):
		return self.__service.sell_product(product_id)