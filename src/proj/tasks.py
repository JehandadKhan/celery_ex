from .celery import app
import time

@app.task
def add(context : dict):
    # time.sleep(context['x'] % 10)
    time.sleep(1)
    res = { 'sum' : context['x'] + context['y']}
    return res


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
