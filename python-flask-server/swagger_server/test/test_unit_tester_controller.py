# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.unit_tester_error500 import UnitTesterError500  # noqa: E501
from swagger_server.models.unit_tester_job_create_req import UnitTesterJobCreateReq  # noqa: E501
from swagger_server.models.unit_tester_job_create_resp import UnitTesterJobCreateResp  # noqa: E501
from swagger_server.models.unit_tester_job_log_export_resp import UnitTesterJobLogExportResp  # noqa: E501
from swagger_server.models.unit_tester_job_read_resp import UnitTesterJobReadResp  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUnitTesterController(BaseTestCase):
    """UnitTesterController integration test stubs"""

    def test_get_job(self):
        """Test case for get_job

        Get the status of a job.
        """
        response = self.client.open(
            '/v1/job/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_job(self):
        """Test case for post_job

        Start running the UT for a given application
        """
        body = UnitTesterJobCreateReq()
        response = self.client.open(
            '/v1/job',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_job_log_export(self):
        """Test case for post_job_log_export

        Export a tar.gz archive with log files for the job
        """
        job_id = 'job_id_example'
        response = self.client.open(
            '/v1/job/logs',
            method='POST',
            data=json.dumps(job_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
