# Orders API

## Endpoints

- `GET /api/orders/` - List all orders
- `POST /api/orders/` - Create a new order
- `GET /api/orders/{id}/` - Retrieve an order by ID
- `PUT /api/orders/{id}/` - Update an order by ID
- `DELETE /api/orders/{id}/` - Delete an order by ID

## Example Requests

### List Orders

```http
GET /api/orders/
```

### Create Order

```http
POST /api/orders/
Content-Type: application/json

{
    "product_id": 1,
    "quantity": 2
}
```