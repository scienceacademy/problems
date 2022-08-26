import check50
import check50.c


@check50.check()
def exists():
    """count_digits.c exists"""
    check50.exists("count_digits.c")


@check50.check(exists)
def compiles():
    """count_digits compiles"""
    check50.c.compile("count_digits.c", lcs50=True)


@check50.check(compiles)
def test410():
    """input of 410 yields output of 3"""
    check50.run("./count_digits").stdin("410").stdout("3\n").exit(0)


@check50.check(compiles)
def test123456789():
    """input of 123456789 yields output of 9"""
    check50.run("./count_digits").stdin("123456789").stdout("9\n").exit(0)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./count_digits").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./count_digits").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./count_digits").stdin("").reject()

