# hw_18

## Files

- `docker-compose.yaml`
- `.env`
- `Makefile`
- `requirements.txt`
- `migrations/20260329_01_users_create_table.py`
- `migrations/20260329_02_users_add_lastname.py`

## Commands

```bash
make dev.install
make db.migration.new name="users: create table"
make db.migrate
make db.rollback
```
