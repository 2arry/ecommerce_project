# Authentication API

## Endpoints

- `POST /api/auth/login/` - Log in a user
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/logout/` - Log out a user

## Example Requests

### Log In

```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "user",
    "password": "pass"
}
```

### Register

```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "newuser",
    "password": "newpass",
    "email": "newuser@example.com"
}
```