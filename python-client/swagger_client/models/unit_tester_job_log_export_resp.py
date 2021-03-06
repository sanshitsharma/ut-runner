# coding: utf-8

"""
    REST APIs for UT runner

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UnitTesterJobLogExportResp(object):
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
        'export': 'str'
    }

    attribute_map = {
        'export': 'export'
    }

    def __init__(self, export=None):  # noqa: E501
        """UnitTesterJobLogExportResp - a model defined in Swagger"""  # noqa: E501

        self._export = None
        self.discriminator = None

        if export is not None:
            self.export = export

    @property
    def export(self):
        """Gets the export of this UnitTesterJobLogExportResp.  # noqa: E501

        Base64 encoded string representing the exported gunzip arhieve  # noqa: E501

        :return: The export of this UnitTesterJobLogExportResp.  # noqa: E501
        :rtype: str
        """
        return self._export

    @export.setter
    def export(self, export):
        """Sets the export of this UnitTesterJobLogExportResp.

        Base64 encoded string representing the exported gunzip arhieve  # noqa: E501

        :param export: The export of this UnitTesterJobLogExportResp.  # noqa: E501
        :type: str
        """

        self._export = export

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
        if issubclass(UnitTesterJobLogExportResp, dict):
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
        if not isinstance(other, UnitTesterJobLogExportResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
