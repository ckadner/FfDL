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

from swagger_client.models.resource_meta_parent import ResourceMetaParent  # noqa: F401,E501


class ResourceMeta(object):
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
        'guid': 'str',
        'url': 'str',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'parent': 'ResourceMetaParent'
    }

    attribute_map = {
        'guid': 'guid',
        'url': 'url',
        'created_at': 'created_at',
        'modified_at': 'modified_at',
        'parent': 'parent'
    }

    def __init__(self, guid=None, url=None, created_at=None, modified_at=None, parent=None):  # noqa: E501
        """ResourceMeta - a model defined in Swagger"""  # noqa: E501

        self._guid = None
        self._url = None
        self._created_at = None
        self._modified_at = None
        self._parent = None
        self.discriminator = None

        self.guid = guid
        self.url = url
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if parent is not None:
            self.parent = parent

    @property
    def guid(self):
        """Gets the guid of this ResourceMeta.  # noqa: E501


        :return: The guid of this ResourceMeta.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ResourceMeta.


        :param guid: The guid of this ResourceMeta.  # noqa: E501
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501

        self._guid = guid

    @property
    def url(self):
        """Gets the url of this ResourceMeta.  # noqa: E501


        :return: The url of this ResourceMeta.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ResourceMeta.


        :param url: The url of this ResourceMeta.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def created_at(self):
        """Gets the created_at of this ResourceMeta.  # noqa: E501


        :return: The created_at of this ResourceMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ResourceMeta.


        :param created_at: The created_at of this ResourceMeta.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this ResourceMeta.  # noqa: E501


        :return: The modified_at of this ResourceMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ResourceMeta.


        :param modified_at: The modified_at of this ResourceMeta.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def parent(self):
        """Gets the parent of this ResourceMeta.  # noqa: E501


        :return: The parent of this ResourceMeta.  # noqa: E501
        :rtype: ResourceMetaParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ResourceMeta.


        :param parent: The parent of this ResourceMeta.  # noqa: E501
        :type: ResourceMetaParent
        """

        self._parent = parent

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
        if not isinstance(other, ResourceMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
