# Standard library imports...
from unittest import mock, TestCase
import responses

mock_environ = {
    "SFDC_CONSUMER_KEY": "false",
    "SFDC_USERNAME": "foo",
    "SFDC_PRIVATE_CERT": "foo",
    "SFDC_PRIVATE_CERT_PATH": "foo",
}


# This test is broken for some reason when all the tests are run together.
class TestSandboxSFDCAuth(TestCase):
    def test_get_sandbox_login(self):
        with responses.RequestsMock() as rsps:
            with mock.patch("SFJWT.SFJWT.jwt.encode") as encode:
                encode.return_value = "my_secret_string"
                from SFJWT.SFJWT import jwt_login

                rsps.add(
                    responses.POST,
                    "https://test.salesforce.com/services/oauth2/token",
                    body='{"instance_url": "salesforce.com", "access_token": "my_access_token"}',
                    status=201,
                    content_type="application/json",
                )
                instance_url, token = jwt_login(
                    "consumer_id", "username", "private_key", "sandbox"
                )

        assert instance_url == "salesforce.com"
        assert token == "my_access_token"

    def test_get_prod_login(self):
        with responses.RequestsMock() as rsps:
            with mock.patch("SFJWT.SFJWT.jwt.encode") as encode:
                encode.return_value = "my_secret_string"
                from SFJWT.SFJWT import jwt_login

                rsps.add(
                    responses.POST,
                    "https://login.salesforce.com/services/oauth2/token",
                    body='{"instance_url": "salesforce.com", "access_token": "my_access_token"}',
                    status=201,
                    content_type="application/json",
                )
                instance_url, token = jwt_login(
                    "consumer_id", "username", "private_key", "production"
                )

        assert instance_url == "salesforce.com"
        assert token == "my_access_token"
