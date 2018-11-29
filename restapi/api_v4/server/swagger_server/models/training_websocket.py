# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.resource_meta import ResourceMeta  # noqa: F401,E501
from swagger_server.models.status import Status  # noqa: F401,E501
from swagger_server import util


class TrainingWebsocket(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, metadata: ResourceMeta=None, entity: Status=None):  # noqa: E501
        """TrainingWebsocket - a model defined in Swagger

        :param metadata: The metadata of this TrainingWebsocket.  # noqa: E501
        :type metadata: ResourceMeta
        :param entity: The entity of this TrainingWebsocket.  # noqa: E501
        :type entity: Status
        """
        self.swagger_types = {
            'metadata': ResourceMeta,
            'entity': Status
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'entity': 'entity'
        }

        self._metadata = metadata
        self._entity = entity

    @classmethod
    def from_dict(cls, dikt) -> 'TrainingWebsocket':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The training_websocket of this TrainingWebsocket.  # noqa: E501
        :rtype: TrainingWebsocket
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> ResourceMeta:
        """Gets the metadata of this TrainingWebsocket.


        :return: The metadata of this TrainingWebsocket.
        :rtype: ResourceMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: ResourceMeta):
        """Sets the metadata of this TrainingWebsocket.


        :param metadata: The metadata of this TrainingWebsocket.
        :type metadata: ResourceMeta
        """

        self._metadata = metadata

    @property
    def entity(self) -> Status:
        """Gets the entity of this TrainingWebsocket.


        :return: The entity of this TrainingWebsocket.
        :rtype: Status
        """
        return self._entity

    @entity.setter
    def entity(self, entity: Status):
        """Sets the entity of this TrainingWebsocket.


        :param entity: The entity of this TrainingWebsocket.
        :type entity: Status
        """

        self._entity = entity
