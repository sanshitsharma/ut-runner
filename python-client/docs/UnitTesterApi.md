# swagger_client.UnitTesterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](UnitTesterApi.md#get_job) | **GET** /v1/job/{id} | Get the status of a job.
[**post_job**](UnitTesterApi.md#post_job) | **POST** /v1/job | Start running the UT for a given application
[**post_job_log_export**](UnitTesterApi.md#post_job_log_export) | **POST** /v1/job/logs | Export a tar.gz archive with log files for the job


# **get_job**
> UnitTesterJobReadResp get_job(id)

Get the status of a job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitTesterApi()
id = 'id_example' # str | A unique ID to identify a job.

try:
    # Get the status of a job.
    api_response = api_instance.get_job(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitTesterApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique ID to identify a job. | 

### Return type

[**UnitTesterJobReadResp**](UnitTesterJobReadResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job**
> UnitTesterJobCreateResp post_job(body)

Start running the UT for a given application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitTesterApi()
body = swagger_client.UnitTesterJobCreateReq() # UnitTesterJobCreateReq | 

try:
    # Start running the UT for a given application
    api_response = api_instance.post_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitTesterApi->post_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitTesterJobCreateReq**](UnitTesterJobCreateReq.md)|  | 

### Return type

[**UnitTesterJobCreateResp**](UnitTesterJobCreateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_job_log_export**
> UnitTesterJobLogExportResp post_job_log_export(job_id)

Export a tar.gz archive with log files for the job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UnitTesterApi()
job_id = 'job_id_example' # str | ID of the job for which logs are to be exported

try:
    # Export a tar.gz archive with log files for the job
    api_response = api_instance.post_job_log_export(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitTesterApi->post_job_log_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of the job for which logs are to be exported | 

### Return type

[**UnitTesterJobLogExportResp**](UnitTesterJobLogExportResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

