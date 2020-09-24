# ExchangeRate

Test, a REST web service for currency conversion.

```
Default currencies:
Czech koruna
Euro
Polish złoty
US dollar
```

Base currency is EUR.

Exchange rates taken from free sources https://api.exchangeratesapi.io/latest?base=EUR&symbols=CZK,PLN,USD 

Every work day at 18:00 CET or 16:00 UTC is update currencies rates

## Install

### Requests

Python 3.7

### Back-end Django
```
sudo apt install redis-server libsqlite3-dev

git clone git@github.com:Feduch/ExchangeRate.git

cd  ExchangeRate/

pip install -r requirements.txt

./manage.py runserver 127.0.0.1:8000

celery -A ExchangeRate worker -l info

celery -A ExchangeRate beat -l info
```

### Front-end Vue.js
```
git clone git@github.com:Feduch/ExchangeRate-Frontend.git

yarn install

yarn serve
```

Example of work, https://www.youtube.com/watch?v=0rTs95_DVp0&feature=youtu.be
