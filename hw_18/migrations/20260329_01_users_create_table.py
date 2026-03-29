from yoyo import step


steps = [
    step(
        """
        CREATE TABLE users (
            id BIGSERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
        """,
        "DROP TABLE users;",
    )
]
