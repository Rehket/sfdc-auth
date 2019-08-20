import requests  # Used to make http/s requests
import jwt  # JWT Library
import datetime
import os
from typing import Tuple

SFDC_CONSUMER_KEY = os.environ.get("SFDC_CONSUMER_KEY", None)
SFDC_USERNAME = os.environ.get("SFDC_USERNAME", None)
SFDC_PRIVATE_CERT = os.environ.get("SFDC_PRIVATE_CERT", None)
SFDC_ENVIRONMENT = os.environ.get("SFDC_ENVIRONMENT", None)


def jwt_login(
    consumer_id: str, username: str, private_key: str, environment: str
) -> Tuple[str, str]:
    if environment:
        if environment.lower() == "sandbox":
            endpoint = "https://test.salesforce.com"
        elif environment.lower() == "production":
            endpoint = "https://login.salesforce.com"
        else:
            raise EnvironmentError(
                f"SFDC_SANDBOX_ENVIRONMENT must be sandbox or production, got {environment}"
            )
    else:
        raise EnvironmentError(
            f"SFDC_SANDBOX_ENVIRONMENT must be sandbox or production"
        )

    jwt_payload = jwt.encode(
        {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30),
            "iss": consumer_id,
            "aud": endpoint,
            "sub": username,
        },
        private_key,
        algorithm="RS256",
    )

    # This makes a request againts the oath service endpoint in SFDC.
    # There are two urls, login.salesforce.com for Production and test.salesforce.com
    # for sanboxes/dev/testing environments. When using test.salesforce.com,
    # the sandbox name should be appended to the username.

    result = requests.post(
        # https://login.salesforce.com/services/oauth2/token -> PROD
        # https://test.salesforce.com/services/oauth2/token -> sandbox
        endpoint + "/services/oauth2/token",
        data={
            "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "assertion": jwt_payload,
        },
    )
    body = result.json()
    if result.status_code != 201:
        raise RuntimeError(f"Authentication Failed: <error: {body['error']}, description: {body['error_description']}>")
    return str(body["instance_url"]), str(body["access_token"])


def get_login() -> Tuple[str, str]:

    if (
        SFDC_PRIVATE_CERT is None
        or SFDC_USERNAME is None
        or SFDC_CONSUMER_KEY is None
        or SFDC_ENVIRONMENT is None
    ):
        raise EnvironmentError("SalesForce environment variables not configured.")
    return jwt_login(
        consumer_id=SFDC_CONSUMER_KEY,
        username=SFDC_USERNAME,
        private_key=SFDC_PRIVATE_CERT,
        environment=SFDC_ENVIRONMENT,
    )
