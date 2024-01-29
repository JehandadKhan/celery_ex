# import celeryconfig
from celery import Celery

app = Celery('proj',
             broker='redis://localhost:6379/14',
             backend='redis://localhost:6379/15',
             include=['proj.tasks'])
# app.config_from_object(celeryconfig)
# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    broker_pool_limit=20
)

if __name__ == '__main__':
    app.start()
