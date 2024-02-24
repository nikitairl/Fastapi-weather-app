from celery import Celery
from celery.schedules import crontab
from celery.signals import beat_init, worker_process_init
from . import models, crud, schemas, db, main

celery_app = Celery(__name__)
settings = {
    'broker_url': 'redis://localhost:6379',
}

# celery --app app.worker.celery_app worker --beat -s celerybeat-schedule --loglevel INFO

celery_app.conf.broker_url = settings['broker_url']
celery_app.conf.result_backend = settings['broker_url']

@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, *args, **kwargs):
    sender.add_periodic_task(
        crontab(minute="1"),
        main.get_all_cities_tmp.s(),
        name='get_cities'
    )


@celery_app.task
def get_all_cities_tmp():
    main.get_cities(db)