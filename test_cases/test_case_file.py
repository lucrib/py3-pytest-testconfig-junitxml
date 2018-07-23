import pytest
from pytest_testconfig import config


def setup_module():
    print('>>> setup_module')


def teardown_module():
    print('>>> teardown_module')


class TestCaseClass(object):

    @classmethod
    def setup_class(cls):
        print('>>> setup_class')

    @classmethod
    def teardown_class(cls):
        print('>>> teardown_class')

    def setup(self):
        print('>>> setup')

    def teardown(self):
        print('>>> teardown')

    def test_case_0(self):
        print('>>> test_case_0')
        assert True

    def test_case_1(self):
        print('>>> ' + config['session']['value'])
        assert True


@pytest.mark.usefixtures("setup_session")
class TestOtherClass(object):

    def test_simple(self):
        print('>>> test_simple')


def test_alone():
    print('>>> test_alone')
