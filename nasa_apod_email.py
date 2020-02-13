import requests

from settings import (
    RECIPIENTS, NASA_API_KEY, MAILGUN_AUTH_TOKEN, MAILGUN_URL, SENDER
)


HTML_TEMPLATE = """
<html>
    <h2>{title}</h2>
    <div>
        <a href="{hdurl}">
            <img max-width="600px" src="{url}" alt="{title}"></img>
        </a>
    </div>
    <div>{explanation}</div>
</html>
"""

TEXT_TEMPLATE = """{title}
Image url: {hdurl}
{explanation}
"""

SUBJECT_TEMPLATE = """Astronomy Picture of the Day {date}"""

NASA_APOD_URL = "https://api.nasa.gov/planetary/apod?api_key={}&hd=True"


def send_apod_email():
    response_json = requests.get(NASA_APOD_URL.format(NASA_API_KEY)).json()

    if "hdurl" not in response_json:
        response_json["hdurl"] = response_json["url"]

    html = HTML_TEMPLATE.format(**response_json)
    text = TEXT_TEMPLATE.format(**response_json)
    subject = SUBJECT_TEMPLATE.format(**response_json)

    for recipient in RECIPIENTS:
        requests.post(
            MAILGUN_URL,
            auth=("api", MAILGUN_AUTH_TOKEN),
            data={
                "from": SENDER,
                "to": recipient,
                "subject": subject,
                "html": html,
                "text": text
            }
        )


if __name__ == "__main__":
    send_apod_email()
