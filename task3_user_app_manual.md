# user app manual

## register

**POST** http://127.0.0.1:8000/accounts/register

### required body (in json)

```json
{
    "password": "123"
}
```

### sample request

```bash
$ curl -d '{"password": "123"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/accounts/register
```

### sample response

```json
{"username":1777613459}
```

## login

**POST** http://127.0.0.1:8000/accounts/login

### required body (in json)

```json
{
    "username": 1777613459,
    "password": "123"
}
```

### sample request

```bash
$ curl -d '{"username": 1777613459, "password": "123"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/accounts/login
```

### sample response

```json
{"token":"cbe94c06503f4bedb179862762d956a4"}
```

## view home page after login

**GET** http://127.0.0.1:8000

### required header

```
Authorization: token {token}
```

### sample request

```bash
$ curl -H 'Authorization: token cbe94c06503f4bedb179862762d956a4' http://127.0.0.1:8000
```

### sample response

```json
{"message":"welcome home 1777613459"}
```
