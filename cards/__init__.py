import check50


@check50.check()
def exists():
    """cash exists"""
    check50.exists("cash.c")


@check50.check(exists)
def compiles():
    """cash compiles"""
    check50.c.compile("cash.c", lcs50=True)
