import pytest


@pytest.fixture(scope='session')
def setup_session(request):
    print('>>> setup_session')

    def fin():
        print('>>> teardown_session')

    request.addfinalizer(fin)


def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = extract_name_or_doc(par)
    suf = extract_name_or_doc(node)
    if pref or suf:
        item._nodeid = ' - '.join((pref, suf))


def extract_name_or_doc(x):
    if getattr(x, '__doc__', None):
        return x.__doc__.splitlines()[0].strip()
    if getattr(x, '__name__', None):
        return x.__name__
    return x.__class__.__name__
