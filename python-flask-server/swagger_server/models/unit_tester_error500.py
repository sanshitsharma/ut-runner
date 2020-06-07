# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UnitTesterError500(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, severity: str=None, message: str=None, data: str=None):  # noqa: E501
        """UnitTesterError500 - a model defined in Swagger

        :param code: The code of this UnitTesterError500.  # noqa: E501
        :type code: str
        :param severity: The severity of this UnitTesterError500.  # noqa: E501
        :type severity: str
        :param message: The message of this UnitTesterError500.  # noqa: E501
        :type message: str
        :param data: The data of this UnitTesterError500.  # noqa: E501
        :type data: str
        """
        self.swagger_types = {
            'code': str,
            'severity': str,
            'message': str,
            'data': str
        }

        self.attribute_map = {
            'code': 'code',
            'severity': 'severity',
            'message': 'message',
            'data': 'data'
        }

        self._code = code
        self._severity = severity
        self._message = message
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'UnitTesterError500':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The unit_testerError500 of this UnitTesterError500.  # noqa: E501
        :rtype: UnitTesterError500
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this UnitTesterError500.

        HTTP return code  # noqa: E501

        :return: The code of this UnitTesterError500.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this UnitTesterError500.

        HTTP return code  # noqa: E501

        :param code: The code of this UnitTesterError500.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def severity(self) -> str:
        """Gets the severity of this UnitTesterError500.

        Error severity level  # noqa: E501

        :return: The severity of this UnitTesterError500.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity: str):
        """Sets the severity of this UnitTesterError500.

        Error severity level  # noqa: E501

        :param severity: The severity of this UnitTesterError500.
        :type severity: str
        """
        allowed_values = ["Critical", "Warning", "Fatal"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def message(self) -> str:
        """Gets the message of this UnitTesterError500.

        Error message  # noqa: E501

        :return: The message of this UnitTesterError500.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this UnitTesterError500.

        Error message  # noqa: E501

        :param message: The message of this UnitTesterError500.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def data(self) -> str:
        """Gets the data of this UnitTesterError500.

        Details of the error  # noqa: E501

        :return: The data of this UnitTesterError500.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data: str):
        """Sets the data of this UnitTesterError500.

        Details of the error  # noqa: E501

        :param data: The data of this UnitTesterError500.
        :type data: str
        """

        self._data = data