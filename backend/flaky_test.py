import random, time


def test_login():
    time.sleep(random.uniform(0.1, 0.5))
    assert random.random() > 0.2, "Login failed randomly"


def test_payment():
    assert True


def test_inventory():
    time.sleep(random.uniform(0.1, 0.3))
    assert random.choice([True, False]), "Intermittent inventory issue"


tests = [test_login, test_payment, test_inventory]

if __name__ == "__main__":
    for test in tests:
        try:
            test()
            print(f"{test.__name__}: PASS")
        except AssertionError as e:
            print(f"{test.__name__}: FAIL ({str(e)})")
