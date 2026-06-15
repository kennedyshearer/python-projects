## Restaurant Menu (Django)

A simple Django app to publish a restaurant menu with categories, prices, and per-item detail pages. Includes class-based views, templates, and an admin backend.

## Quick start

```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell
# If needed: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 2) Install dependencies
# If requirements.txt is present:
pip install -r requirements.txt
# Otherwise (see Dependencies below):
pip install "Django>=5.0,<6.0"

# 3) Apply migrations and run
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Project structure

```
app17-restaurant-menu/
├─ mysite/
│  ├─ settings.py
│  └─ urls.py   # includes restaurant_menu.urls at root
├─ restaurant_menu/
│  ├─ models.py
│  ├─ views.py
│  ├─ urls.py   # '' → menu list, 'item/<int:pk>/' → item detail
│  └─ templates/
│     ├─ base.html
│     ├─ index.html
│     └─ menu_item_detail.html
└─ manage.py
```

## URLs

- `/` → Menu list
- `/item/<pk>/` → Menu item detail
- `/admin/` → Django admin

Wired via `mysite/urls.py` including `restaurant_menu/urls.py` at the root.

## Data model

`restaurant_menu.models.Item`

- `meal`: CharField, unique name
- `description`: CharField
- `price`: DecimalField
- `meal_type`: CharField with choices: `starters`, `salads`, `main_dishes`, `desserts`
- `author`: ForeignKey to `auth.User` (PROTECT on delete)
- `status`: Integer choices: `0` Unavailable, `1` Available (default)
- `date_created`: DateTime (auto_now_add)
- `date_updated`: DateTime (auto_now)

## Running locally

```bash
python manage.py migrate
python manage.py createsuperuser  # optional, to manage items in admin
python manage.py runserver
```

Log into `/admin/` to add `Item` entries.

## Templates

- `index.html`: Lists items ordered by `date_created` (newest first). Provides `meals` context with MEAL_TYPE choices for UI grouping/filtering.
- `menu_item_detail.html`: Shows a single `Item`.

## Dependencies

- Python 3.11+ recommended
- Django 5.x

If no `requirements.txt` is present:

```bash
pip install "Django>=5.0,<6.0"
# Optional: freeze
pip freeze > requirements.txt
```

## Deployment

- Set `DEBUG=False` and configure `ALLOWED_HOSTS` in `mysite/settings.py`.
- Run `collectstatic` if you add static files.
- Use a production server (e.g., gunicorn/uvicorn + reverse proxy) and a managed DB.

## License

MIT

## Notes

A `qr.png` is included if you want to share a QR pointing to your menu URL for table tents.
