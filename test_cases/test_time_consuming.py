from time import sleep


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


def test_has_name():
    """
    Test case with description
    """
    sleep(0.5)
