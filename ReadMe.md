# SalesForce JWT Auth
[![Coverage Status](https://coveralls.io/repos/gitlab/Rehket/salesforce-jwt/badge.svg)](https://coveralls.io/gitlab/Rehket/salesforce-jwt)

A git installable python module to use server client auth against SalesForce

## Installation
```shell script
python -m pip install git+https://gitlab.com/Rehket/salesforce-jwt.git
```

## Usage
```python
import SFJWT
import requests
# With environment variables set:
instance_url, bearer_token = SFJWT.get_login()

# or if you just want to pass them:
#instance_url, bearer_token = SFJWT.jwt_login(
#    consumer_id="my_connected_app_consumer_id",
#    username="my_sfdc_user_id_that_is_preauthorized@sfdc.com",
#    private_key="my_connected_app_private_key",
#    environment="(sandbox|production)",
#)

# Make a request.
my_headers = {"Accept": "application/json", "Authorization": f"Bearer {bearer_token}"}
my_instance_data = requests.post(f"https://{instance_url}//services/data/v46.0/", headers = my_headers)

```