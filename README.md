# T-301-HONN ~ Project 2 ~ Microservices

**Members:**
* Daníel Freyr Grétarsson
* Helgi Hákonarsson
* Margrét Halla María Johnsson
* Patrekur Þór Agnarsson

## Start program
1. Update `./EmailService/.env` to include your Google Email and app password.
2. Run `docker compose up -d --scale email_service=2` from the root directory.

### Request body
Please make sure to use snake_case in the request body.
Like so:
```json
{
    "product_id": 1,
    "merchant_id": 1,
    "buyer_id": 1,
    "credit_card": {
        "card_number": "4510164231949222",
        "expiration_month": "7",
        "expiration_year": "2024",
        "cvc": "321"
    },
    "discount": 0.2
}
```