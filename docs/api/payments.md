# Payments API

## Endpoints

- `GET /api/payments/` - List all payments
- `POST /api/payments/` - Create a new payment
- `GET /api/payments/{id}/` - Retrieve a payment by ID
- `PUT /api/payments/{id}/` - Update a payment by ID
- `DELETE /api/payments/{id}/` - Delete a payment by ID

## Example Requests

### List Payments

```http
GET /api/payments/
```

### Create Payment

```http
POST /api/payments/
Content-Type: application/json

{
    "order_id": 1,
    "amount": 100.00
}
```