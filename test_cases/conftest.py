import pytest


@pytest.fixture(scope='session')
def setup_session(request):
    print('>>> setup_session')

    def fin():
        print('>>> teardown_session')

    request.addfinalizer(fin)
