from app.exceptions.custom_exceptions import UserNotFoundException

# Temporary in-memory data.
# Later this layer can be replaced with PostgreSQL/Supabase.
USERS = {
    1: {
        "id": 1,
        "name": "Haripriya",
        "email": "haripriya@example.com"
    },
    2: {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    }
}


def get_user_by_id(user_id: int):
    user = USERS.get(user_id)

    if user is None:
        raise UserNotFoundException(user_id)

    return user
