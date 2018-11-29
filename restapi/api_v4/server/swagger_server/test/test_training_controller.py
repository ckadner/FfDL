# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_auth import ErrorAuth  # noqa: E501
from swagger_server.models.error_bad_request import ErrorBadRequest  # noqa: E501
from swagger_server.models.error_internal_server_error import ErrorInternalServerError  # noqa: E501
from swagger_server.models.error_not_found import ErrorNotFound  # noqa: E501
from swagger_server.models.training_resource import TrainingResource  # noqa: E501
from swagger_server.models.training_resource_entity_request import TrainingResourceEntityRequest  # noqa: E501
from swagger_server.models.training_resources import TrainingResources  # noqa: E501
from swagger_server.models.training_websocket import TrainingWebsocket  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrainingController(BaseTestCase):
    """TrainingController integration test stubs"""

    def test_v4_trainings_get(self):
        """Test case for v4_trainings_get

        Get the list of all trainings
        """
        query_string = [('start', 'start_example'),
                        ('limit', 8.14),
                        ('tag_value', 'tag_value_example'),
                        ('type', 'type_example')]
        response = self.client.open(
            '//v4/trainings',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v4_trainings_post(self):
        """Test case for v4_trainings_post

        Create a new Machine Learning training
        """
        payload = TrainingResourceEntityRequest()
        response = self.client.open(
            '//v4/trainings',
            method='POST',
            data=json.dumps(payload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v4_trainings_training_id_delete(self):
        """Test case for v4_trainings_training_id_delete

        Cancel an ongoing training.
        """
        response = self.client.open(
            '//v4/trainings/{training_id}'.format(training_id='training_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_v4_trainings_training_id_get(self):
        """Test case for v4_trainings_training_id_get

        Get the training status
        """
        response = self.client.open(
            '//v4/trainings/{training_id}'.format(training_id='training_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
