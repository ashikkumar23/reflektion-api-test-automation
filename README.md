# reflektion-api-test-automation
Automated API's to verify response, schema, etc.,

# Prerequisites:
1. requests
2. pytest
3. pytest-html
4. jsonschema

Above packages are mentioned as part of requirements.txt, run the command: pip install -r requirements.txt

# Project contents:
1. `api` directory contains `api.py`, `__init__.py` files which consists of api methods required for api testing
2. `tests` directory contains `test_api.py`, `__init__.py` files which verifies api's response, schema, etc.,

# Steps to execute the tests:
1. Pull the code to your local repository
2. Open Pycharm -> File -> Open -> Open the project where the repository is located
3. Open terminal and navigate to the directory where the project resides
4. Or instead of step 2 & 3, open command prompt and navigate to the directory where project resides
5. Run the command: pytest -v --html=test_report.html tests\test_api.py

# Output:
Test results along with HTML test report will be generated

# Sample Test Result:
(venv) C:\Users\ABC\PycharmProjects\Reflektion\APITestAutomation>pytest -v --html=test_report.html tests\test_api.py
=========================== test session starts ===============================

platform win32 -- Python 3.7.3, pytest-5.0.0, py-1.8.0, pluggy-0.12.0 -- c:\users\abc\downloads\reflektion\venv\scripts\python.exe

cachedir: .pytest_cache

metadata: {'Python': '3.7.3', 'Platform': 'Windows-8.1-6.3.9600-SP0', 'Packages': {'pytest': '5.0.0', 'py': '1.8.0', 'pluggy': '0.12.0'}, 'Plugins': {'html': '1.21.1', 'metadata': '1.8.0'}}

rootdir: C:\Users\ABC\PycharmProjects\Reflektion\APITestAutomation

plugins: html-1.21.1, metadata-1.8.0

collected 6 items

tests/test_api.py::test_get_request_1 PASSED                                                                                                                                      [ 16%]

tests/test_api.py::test_get_request_2 PASSED                                                                                                                                      [ 33%]

tests/test_api.py::test_get_response_3 PASSED                                                                                                                                     [ 50%]

tests/test_api.py::test_post_request PASSED                                                                                                                                       [ 66%]

tests/test_api.py::test_put_request PASSED                                                                                                                                        [ 83%]

tests/test_api.py::test_delete_request PASSED                                                                                                                                     [100%]

-------- generated html file: file://C:\Users\ABC\PycharmProjects\Reflektion\APITestAutomation\test_report.html ---------

======================== 6 passed in 13.82 seconds ==============================
