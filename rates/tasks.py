import requests
from celery.task import periodic_task
from celery.schedules import crontab
from django.conf import settings
from currency.models import Currency
from rates.models import Rate


@periodic_task(ignore_result=True, run_every=crontab(minute='0', hour='18', day_of_week='1-5'))
def celery_update_currency_rate():
    """
    Every work day at 18:00 CET or 16:00 UTC is update currencies rates
    """
    response = requests.get(settings.SOURCE_EXCHANGE_URL)
    data = response.json()
    rates = data.get('rates')
    rates_count = Rate.objects.filter(date=data.get("date")).count()

    # Insert new rates
    if rates_count == 0:
        currencies = Currency.objects.filter()

        instances = []
        for currency in currencies:
            if currency.is_base:
                rate = 1
            else:
                rate = rates.get(currency.code)

            instances.append(Rate(
                rate=rate,
                currency=currency,
                date=data.get("date")
            ))

        Rate.objects.bulk_create(instances)

    return True
