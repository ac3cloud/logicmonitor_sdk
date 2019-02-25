# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.ops_note_scope import OpsNoteScope  # noqa: F401,E501


class OpsNoteDeviceGroupScope(OpsNoteScope):
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
        'type': 'str',
        'full_path': 'str',
        'group_id': 'int'
    }

    attribute_map = {
        'type': 'type',
        'full_path': 'fullPath',
        'group_id': 'groupId'
    }

    def __init__(self, type=None, full_path=None, group_id=None):  # noqa: E501
        """OpsNoteDeviceGroupScope - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._full_path = None
        self._group_id = None
        self.discriminator = None

        self.type = type
        if full_path is not None:
            self.full_path = full_path
        if group_id is not None:
            self.group_id = group_id

    @property
    def type(self):
        """Gets the type of this OpsNoteDeviceGroupScope.  # noqa: E501


        :return: The type of this OpsNoteDeviceGroupScope.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpsNoteDeviceGroupScope.


        :param type: The type of this OpsNoteDeviceGroupScope.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def full_path(self):
        """Gets the full_path of this OpsNoteDeviceGroupScope.  # noqa: E501


        :return: The full_path of this OpsNoteDeviceGroupScope.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this OpsNoteDeviceGroupScope.


        :param full_path: The full_path of this OpsNoteDeviceGroupScope.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def group_id(self):
        """Gets the group_id of this OpsNoteDeviceGroupScope.  # noqa: E501


        :return: The group_id of this OpsNoteDeviceGroupScope.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this OpsNoteDeviceGroupScope.


        :param group_id: The group_id of this OpsNoteDeviceGroupScope.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

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
        if issubclass(OpsNoteDeviceGroupScope, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OpsNoteDeviceGroupScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other