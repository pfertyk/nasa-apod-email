# NASA APOD Email

A simple script that sends NASA's Astronomy Picture of the Day (APOD) in a form
of an email (using Mailgun). HTML version of APOD is available
[here](https://apod.nasa.gov/apod/).

## Installation

You will need a [Mailgun](https://www.mailgun.com/) account.
You can use a sandbox domain, but you will have to add authorized recipients
(one for each email address you want to send the APOD to).

Clone this repository. Copy `setting-sample.py` to `settings.py` and set the
values:
* `MAILGUN_AUTH_TOKEN` copy the value from Mailgun API configuration
* `MAILGUN_URL` copy the value from Mailgun API configuration
* `RECIPIENTS` list of email addressed to which the APOD will be sent (same as authorized recipients in Mailgun)
* `NASA_API_KEY` the default value of `DEMO_KEY` should do, but you can replace it with your own key (if you have one)

To send a single email to all recipients:

```
python nasa_apod_email.py
```

You can also add the script to crontab, e.g. to get an email every day at 8:30AM:

```
30 8 * * * /usr/bin/python3 /path/to/script/apod_email_service.py
```
