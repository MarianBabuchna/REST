# Flask RESTful API project

This small project shows how to create RESTful API by using Flask.


## Prerequisites:

* Created "Virtual environment" (contains Python 3 and all dependencies)
* Activated "Virtual environmet"
* Installed Flask
* Installed flask-restful



## Installation:

Create "Virtual environment" (Win version) 
```bash
    py -3 -m venv venv
```   
Activate "Virtual environment"
```
    venv\Scripts\activate       
```
Install Flask
```    
    pip install Flask
```
All step you can find [here](http://flask.pocoo.org/docs/1.0/installation/#install-flask):
```
    http://flask.pocoo.org/docs/1.0/installation/#install-flask
```

Install Flask REST 
```
    pip install flask-restful
```


## Task description:


For the following JSON structure:
``` 
{   “recordId”: uuid,   
    “info”: { 
       “recordStatus”: enum - “NEW”, “UPDATED”, “DELETED”,
       “created”: datetime when the record was created,
       “updated”: list of datetimes when the record was updated,     
       “deleted”: datetime when the record was marked as deleted,     
       “recordData”: base64 encoded binary payload   
     } 
} 
```
 
Implement REST service which provides following endpoint:
* _/record (POST) – creates new record and sets the “recordStatus” to “NEW”_ 
* _/record/<uuid> (PATCH) – updates the record using JSON patch (see http://jsonpatch.com) and sets the “recordStatus” to “UPDATED”_ 
* _/record/<uuid> (DELETE) – sets the “recordStatus” to “DELETED”_ 
* _/record/<uuid> (GET) – finds the JSON record by UUID and returns it in the response body_ 
* _Every method updates related datetime properties_ 
* _Datetime is stored in RFC 3339 format_ 
* _The records are stored on disk as a text file and separated by new line (\n)._
 

## PROJECT hierarchy:

--REST  
&nbsp; &nbsp;--PROJECT  
&nbsp; &nbsp; &nbsp; &nbsp;--Flask_script.py  
&nbsp; &nbsp; &nbsp; &nbsp;--record_func.py  
&nbsp; &nbsp; &nbsp; &nbsp;--record_obj.py  
&nbsp; &nbsp;--TESTS  
&nbsp; &nbsp; &nbsp; &nbsp;--test_DELETE.py  
&nbsp; &nbsp; &nbsp; &nbsp;--test_GET.py  
&nbsp; &nbsp; &nbsp; &nbsp;--test_PATCH.py  
&nbsp; &nbsp; &nbsp; &nbsp;--test_POST.py  
&nbsp; &nbsp;--stored_records.json  

 
## TEST:

**A:Test GET method**  
For testing "GET" method serve test "test_GET.py" stored in "TESTS":  
Before unit test execution copy following record to "stored_records.json" file.  
```    
{"recordId": "c2bd3384-5a66-4a28-a8bf-9eda7ca26583", "info": {"recordStatus": "NEW", "created": "2019-05-14T19:52:37.715824+02:00", "updated": "", "deleted": "", "recordData": ""}}
```   
Result: _Test function compare record with defined uuid from file and expected result.
If records are equal test PASSED._ 
  

**B:Test DELETE method**   
For testing "DELETE" method serve test "test_DELETE.py" stored in "TESTS":  
Before unit test execution copy following record to "stored_records.json" file.
```
{"recordId": "a2bd3384-5a66-4a28-a8bf-9eda7ca26583", "info": {"recordStatus": "NEW", "created": "2019-05-14T19:52:37.715824+02:00", "updated": "", "deleted": "", "recordData": ""}}
```
Test function check:  
* if "recordStatus" was changed from "NEW" --> "DELETED"  
* if "deleted" variable contains date record  
* if variables "recordID","created","updated" are NOT changed

Result: _If all conditions are accomplished, test PASSED._ 

  

**C:Test PATCH method**  
For testing "PATCH" method serve test "test_PATCH.py" stored in "TESTS":  
Before unit test execution copy following record to "stored_records.json" file.  
``` 
{"recordId": "b2bd3384-5a66-4a28-a8bf-9eda7ca26583", "info": {"recordStatus": "NEW", "created": "2019-05-14T19:52:37.715824+02:00", "updated": "", "deleted": "", "recordData": ""}}
```

Test function check:
* if "recordStatus" was changed from "NEW" --> "UPDATED"  
* if variable "updated" contains date record (or list of date records)  
* if variables "recordID","created","deleted" are NOT changed    

Result: _If all conditions are accomplished, test PASSED._  
 
 
**D:Test POST method**  
For testing "POST" method serve test "test_POST()" stored in "TESTS":  
Following record type with "actual time" will be created in "stored_records.json" file.  
```
{"recordId": "d2bd3384-5a66-4a28-a8bf-9eda7ca26583", "info": {"recordStatus": "NEW", "created": "2019-05-15T16:55:16.059913+02:00", "updated": "", "deleted": "", "recordData": ""}}
```  
Result: _Test function compare created record with expected result.
If records are equal test PASSED._
 
 
## Versions:
Version: v1   
Created: 2019_05_15 
 
 
## Author:  
Marian Babuchna
  
  





