# coding: utf-8

"""
    Azure Blockchain Workbench REST API

    The Azure Blockchain Workbench REST API is a Workbench extensibility point, which allows developers to create and manage blockchain applications, manage users and organizations within a consortium, integrate blockchain applications into services and platforms, perform transactions on a blockchain, and retrieve transactional and contract data from a blockchain.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.capabilities import Capabilities  # noqa: F401,E501
from swagger_client.models.user import User  # noqa: F401,E501


class Me(object):
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
        'current_user': 'User',
        'capabilities': 'Capabilities'
    }

    attribute_map = {
        'current_user': 'currentUser',
        'capabilities': 'capabilities'
    }

    def __init__(self, current_user=None, capabilities=None):  # noqa: E501
        """Me - a model defined in Swagger"""  # noqa: E501

        self._current_user = None
        self._capabilities = None
        self.discriminator = None

        if current_user is not None:
            self.current_user = current_user
        if capabilities is not None:
            self.capabilities = capabilities

    @property
    def current_user(self):
        """Gets the current_user of this Me.  # noqa: E501


        :return: The current_user of this Me.  # noqa: E501
        :rtype: User
        """
        return self._current_user

    @current_user.setter
    def current_user(self, current_user):
        """Sets the current_user of this Me.


        :param current_user: The current_user of this Me.  # noqa: E501
        :type: User
        """

        self._current_user = current_user

    @property
    def capabilities(self):
        """Gets the capabilities of this Me.  # noqa: E501


        :return: The capabilities of this Me.  # noqa: E501
        :rtype: Capabilities
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this Me.


        :param capabilities: The capabilities of this Me.  # noqa: E501
        :type: Capabilities
        """

        self._capabilities = capabilities

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
        if not isinstance(other, Me):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other