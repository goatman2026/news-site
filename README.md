# News Site

A simple Django news website with a list of articles and individual article pages. It includes a basic `Article` model, admin registration, and Bootstrap styling.

## Running locally
```bash
# Activate virtualenv
source .venv/bin/activate

# Apply migrations
python manage.py migrate

# Start dev server
python manage.py runserver
```

## Deploying
You can deploy this project to any platform that supports Django (Heroku, Render, Railway, etc.). See the platform’s docs for setting up environment variables and a WSGI server.
