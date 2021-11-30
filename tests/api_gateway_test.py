import os
from unittest import TestCase

import boto3
import requests

"""
Make sure env variable AWS_API_URI exists with the name of the stack we are going to test. 
"""


class TestApiGateway(TestCase):
    api_endpoint: str

    @classmethod
    def get_api_endpoint(cls) -> str:
        #a good refactoring here would be to inject the url via env variables/config. but it will do for now on this project. Tech debt shame abounds
        endpoint_uri = "https://2suw3xvc05.execute-api.ap-southeast-2.amazonaws.com/Prod/readdb"
        if not endpoint_uri:
            raise Exception(
                "Cannot find env var AWS_API_URI. \n"
                "Please setup this environment variable with the stack name where we are running integration tests."
            )

        return endpoint_uri

    def setUp(self) -> None:
        api_uri = TestApiGateway.get_api_endpoint()
        self.api_endpoint = api_uri

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(self.api_endpoint)
        response_value = response.json()
        assert isinstance(response_value, int)

test = TestApiGateway()
TestApiGateway.setUp(test)
TestApiGateway.test_api_gateway(test)