release: python manage.py migrate --noinput
# release: python manage.py loaddata boat/fixtures/db.json
web: gunicorn boat.wsgi --log-file -
