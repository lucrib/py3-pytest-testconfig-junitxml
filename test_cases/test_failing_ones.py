from datetime import datetime
from unittest import TestCase

import pytest

valid_condition = True
now_is_even = (datetime.utcnow().toordinal() % 2) == 0


class TestCaseFailing(TestCase):

    def test_fail_one(self):
        assert 1 == 0

    def test_error_one(self):
        raise Exception('Sorry. I failed. :(')

    @pytest.mark.skip(reason='Maybe next time.')
    def test_skipped(self):
        pass

    @pytest.mark.skipif(now_is_even, reason='That was an even moment.')
    def test_only_if_moment_is_even(self):
        pytest.skip('That was an even moment.')

    @pytest.mark.skipif(not now_is_even, reason='That was an odd moment.')
    def test_only_if_moment_is_odd(self):
        pytest.skip('That was an odd moment.')
