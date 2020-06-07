import connexion
import six

from swagger_server.models.unit_tester_error500 import UnitTesterError500  # noqa: E501
from swagger_server.models.unit_tester_job_create_req import UnitTesterJobCreateReq  # noqa: E501
from swagger_server.models.unit_tester_job_create_resp import UnitTesterJobCreateResp  # noqa: E501
from swagger_server.models.unit_tester_job_log_export_resp import UnitTesterJobLogExportResp  # noqa: E501
from swagger_server.models.unit_tester_job_read_resp import UnitTesterJobReadResp  # noqa: E501
from swagger_server import util


def get_job(id):  # noqa: E501
    """Get the status of a job.

     # noqa: E501

    :param id: A unique ID to identify a job.
    :type id: str

    :rtype: UnitTesterJobReadResp
    """
    return 'do some magic!'


def post_job(body):  # noqa: E501
    """Start running the UT for a given application

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: UnitTesterJobCreateResp
    """
    if connexion.request.is_json:
        body = UnitTesterJobCreateReq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_job_log_export(job_id):  # noqa: E501
    """Export a tar.gz archive with log files for the job

     # noqa: E501

    :param job_id: ID of the job for which logs are to be exported
    :type job_id: str

    :rtype: UnitTesterJobLogExportResp
    """
    return 'do some magic!'
