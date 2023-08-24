import check50
import check50.c


@check50.check()
def exists():
    """sum_digits.c exists"""
    check50.exists("sum_digits.c")


@check50.check(exists)
def compiles():
    """sum_digits compiles"""
    check50.c.compile("sum_digits.c", lcs50=True)


@check50.check(compiles)
def test410():
    """input of 410 yields output of 5"""
    check50.run("./sum_digits").stdin("410").stdout("5\n").exit(0)


@check50.check(compiles)
def test123456789():
    """input of 123456789 yields output of 45"""
    check50.run("./sum_digits").stdin("123456789").stdout("45\n").exit(0)


@check50.check(compiles)
def test_reject_negative():
    """rejects a negative input like -1"""
    check50.run("./sum_digits").stdin("-1").reject()


@check50.check(compiles)
def test_reject_foo():
    """rejects a non-numeric input of "foo" """
    check50.run("./sum_digits").stdin("foo").reject()


@check50.check(compiles)
def test_reject_empty():
    """rejects a non-numeric input of "" """
    check50.run("./sum_digits").stdin("").reject()

