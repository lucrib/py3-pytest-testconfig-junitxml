from time import sleep

import pytest


@pytest.mark.slow
class TestTimeConsuming:

    def test_takes_1_seconds(self):
        sleep(1.0)

    def test_takes_2_seconds(self):
        sleep(2.0)

    def test_takes_3_seconds(self):
        sleep(3.0)

    def test_takes_4_seconds(self):
        sleep(4.0)

    def test_takes_5_seconds(self):
        sleep(5.0)
