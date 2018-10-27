import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from unittest import TestCase
from service import Service

class TestService(TestCase):
    def test_bad_random(self):
        example_file = '''222\n333\n4'''
        with patch('service.open', mock_open( read_data=example_file), create=True):
            result = Service.bad_random()
            # print(result)
            assert 0 <= result < 3

    def test_divide(self):
        service = Service()
        service.bad_random = mock.Mock(return_value=9)
        return_val = service.divide(2)
        # print(return_val)
        assert return_val == 4.5

    def test_abs_plus(self):
        service = Service()
        return_val = service.abs_plus(3)
        assert return_val == 4

    def test_complicated_function(self):
        service = Service()
        service.bad_random = mock.Mock(return_value=8)
        service.divide = mock.Mock(return_value=9)
        return_val = service.complicated_function(2)
        assert return_val[0]==9
        assert return_val[1]==0
