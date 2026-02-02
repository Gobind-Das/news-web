release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py loaddata admin_user.json
web: gunicorn config.wsgi --bind 0.0.0.0:$PORT --log-file -
