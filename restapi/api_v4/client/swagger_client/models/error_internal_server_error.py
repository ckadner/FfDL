# coding: utf-8

"""
    IBM Watson Machine Learning API

    ## Authorization  Step by step instruction how to use Watson Machine Learning service can be found [here](https://console.ng.bluemix.net/docs/services/PredictiveModeling/using_pm_service_dsx.html#using_pm_service_dsx)  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://us-south.ml.cloud.ibm.com\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\",     \"instance_id\": \"a751c209-954e-dc32-b441-ad56ce7a9f40\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://us-south.ml.cloud.ibm.com/v4/identity/token `  The obtained `access token` needs to be prepended with `Bearer` word and it needs to be passed in the `Authorization` header for API calls.  Example of API request with `Bearer access token`:  ` curl https://us-south.ml.cloud.ibm.com/v4/models -H \"Authorization: Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRJZCI6ImU4YmQzZGM3LWI5Y2UtNDY1OC1iZ...\" `   # noqa: E501

    OpenAPI spec version: 4.x.y
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.error_internal_server_error_errors import ErrorInternalServerErrorErrors  # noqa: F401,E501


class ErrorInternalServerError(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'trace': 'str',
        'errors': 'list[ErrorInternalServerErrorErrors]'
    }

    attribute_map = {
        'trace': 'trace',
        'errors': 'errors'
    }

    def __init__(self, trace=None, errors=None):  # noqa: E501
        """ErrorInternalServerError - a model defined in Swagger"""  # noqa: E501

        self._trace = None
        self._errors = None
        self.discriminator = None

        self.trace = trace
        self.errors = errors

    @property
    def trace(self):
        """Gets the trace of this ErrorInternalServerError.  # noqa: E501


        :return: The trace of this ErrorInternalServerError.  # noqa: E501
        :rtype: str
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this ErrorInternalServerError.


        :param trace: The trace of this ErrorInternalServerError.  # noqa: E501
        :type: str
        """
        if trace is None:
            raise ValueError("Invalid value for `trace`, must not be `None`")  # noqa: E501

        self._trace = trace

    @property
    def errors(self):
        """Gets the errors of this ErrorInternalServerError.  # noqa: E501


        :return: The errors of this ErrorInternalServerError.  # noqa: E501
        :rtype: list[ErrorInternalServerErrorErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ErrorInternalServerError.


        :param errors: The errors of this ErrorInternalServerError.  # noqa: E501
        :type: list[ErrorInternalServerErrorErrors]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorInternalServerError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
