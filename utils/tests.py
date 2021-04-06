def are_equal(actual, expected):
    try:
        assert actual == expected
    except:
        print('actual =', actual, 'expected =', expected)
        raise
