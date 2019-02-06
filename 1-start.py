from nose.tools import assert_true
import requests

def test_request_response():
    res = requests.get('http://jsonplaceholder.typicode.com/todos')
    print(res)
    assert_true(res.ok)
    print(res.ok)


test_request_response()
# to run the test ( nosetests --verbosity=2 proj )