# stockstash
> https://stockstash-prod.herokuapp.com/

"stockstash" is a full featured Flask web application that empowers individual investors with the information they need to achieve their personal financial goals. Users are given the ability to create a customizable stock portfolio and watchlist to track both current and prospective holdings. The application uses RESTful Web Services to pull live/historical stock data.

Technologies: Python, Flask, MongoDB, JavaScript, HTML, CSS, Alpha Vantage API

## Compile / Run Instructions
To run with Flask Development Server:
``` bash
$ pip install -r requirements.txt
$ python run.py
```

To run with Gunicorn WSGI Server:
```bash
$ pip install -r requirements.txt
$ ["gunicorn", "--config", "./stockstash/config/gunicorn_config.py", "stockstash:app"]
```


## The Team
Chris Ragasa:  [[LinkedIn](https://www.linkedin.com/in/cragasa/), [GitHub](https://github.com/chrisragasa)]

Derek Yang: [[LinkedIn](https://www.linkedin.com/in/yangd01234567/), [GitHub](https://github.com/yangd01234)]
