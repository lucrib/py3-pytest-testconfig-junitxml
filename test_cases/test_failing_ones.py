from pytest import skip


class TestCaseFailing:

    def test_fail_one(self):
        assert 1 == 0

    def test_error_one(self):
        raise Exception('A errored test')

    def test_skipped(self):
        skip('Skipped test')
