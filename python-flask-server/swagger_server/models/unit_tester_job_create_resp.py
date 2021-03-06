# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UnitTesterJobCreateResp(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, job_id: str=None, created_at: str=None):  # noqa: E501
        """UnitTesterJobCreateResp - a model defined in Swagger

        :param job_id: The job_id of this UnitTesterJobCreateResp.  # noqa: E501
        :type job_id: str
        :param created_at: The created_at of this UnitTesterJobCreateResp.  # noqa: E501
        :type created_at: str
        """
        self.swagger_types = {
            'job_id': str,
            'created_at': str
        }

        self.attribute_map = {
            'job_id': 'job_id',
            'created_at': 'created_at'
        }

        self._job_id = job_id
        self._created_at = created_at

    @classmethod
    def from_dict(cls, dikt) -> 'UnitTesterJobCreateResp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The unit_testerJobCreateResp of this UnitTesterJobCreateResp.  # noqa: E501
        :rtype: UnitTesterJobCreateResp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self) -> str:
        """Gets the job_id of this UnitTesterJobCreateResp.

        A unique ID to track the job created.  # noqa: E501

        :return: The job_id of this UnitTesterJobCreateResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id: str):
        """Sets the job_id of this UnitTesterJobCreateResp.

        A unique ID to track the job created.  # noqa: E501

        :param job_id: The job_id of this UnitTesterJobCreateResp.
        :type job_id: str
        """

        self._job_id = job_id

    @property
    def created_at(self) -> str:
        """Gets the created_at of this UnitTesterJobCreateResp.

        Time at which job got created.  # noqa: E501

        :return: The created_at of this UnitTesterJobCreateResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str):
        """Sets the created_at of this UnitTesterJobCreateResp.

        Time at which job got created.  # noqa: E501

        :param created_at: The created_at of this UnitTesterJobCreateResp.
        :type created_at: str
        """

        self._created_at = created_at
