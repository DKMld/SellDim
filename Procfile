web: daphne quickmeals.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layers --settings=quickmeals.settings -v2