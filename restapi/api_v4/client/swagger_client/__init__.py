# coding: utf-8

# flake8: noqa

"""
    IBM Watson Machine Learning API

    ## Authorization  Step by step instruction how to use Watson Machine Learning service can be found [here](https://console.ng.bluemix.net/docs/services/PredictiveModeling/using_pm_service_dsx.html#using_pm_service_dsx)  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://us-south.ml.cloud.ibm.com\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\",     \"instance_id\": \"a751c209-954e-dc32-b441-ad56ce7a9f40\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://us-south.ml.cloud.ibm.com/v4/identity/token `  The obtained `access token` needs to be prepended with `Bearer` word and it needs to be passed in the `Authorization` header for API calls.  Example of API request with `Bearer access token`:  ` curl https://us-south.ml.cloud.ibm.com/v4/models -H \"Authorization: Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6ImU4YmQzZGM3LWI5Y2UtNDY1OC1iZ...\" `   # noqa: E501

    OpenAPI spec version: 4.x.y
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.training_api import TrainingApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.error import Error
from swagger_client.models.error_auth import ErrorAuth
from swagger_client.models.error_auth_errors import ErrorAuthErrors
from swagger_client.models.error_bad_request import ErrorBadRequest
from swagger_client.models.error_bad_request_errors import ErrorBadRequestErrors
from swagger_client.models.error_bad_request_target import ErrorBadRequestTarget
from swagger_client.models.error_errors import ErrorErrors
from swagger_client.models.error_internal_server_error import ErrorInternalServerError
from swagger_client.models.error_internal_server_error_errors import ErrorInternalServerErrorErrors
from swagger_client.models.error_not_found import ErrorNotFound
from swagger_client.models.error_not_found_errors import ErrorNotFoundErrors
from swagger_client.models.experiment_object import ExperimentObject
from swagger_client.models.metrics import Metrics
from swagger_client.models.metrics_inner import MetricsInner
from swagger_client.models.node_parameters_object import NodeParametersObject
from swagger_client.models.node_parameters_object_inner import NodeParametersObjectInner
from swagger_client.models.object_location import ObjectLocation
from swagger_client.models.pagination import Pagination
from swagger_client.models.pipeline_object import PipelineObject
from swagger_client.models.pipeline_object_data_bindings import PipelineObjectDataBindings
from swagger_client.models.resource_meta import ResourceMeta
from swagger_client.models.resource_meta_parent import ResourceMetaParent
from swagger_client.models.status import Status
from swagger_client.models.status_message import StatusMessage
from swagger_client.models.tags import Tags
from swagger_client.models.tags_inner import TagsInner
from swagger_client.models.training_resource import TrainingResource
from swagger_client.models.training_resource_entity_request import TrainingResourceEntityRequest
from swagger_client.models.training_websocket import TrainingWebsocket
from swagger_client.models.url_object import UrlObject
from swagger_client.models.data_reference import DataReference
from swagger_client.models.training_resource_entity import TrainingResourceEntity
from swagger_client.models.training_resources import TrainingResources
