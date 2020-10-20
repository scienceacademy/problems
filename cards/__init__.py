import check50


@check50.check()
def exists():
    """cards exists"""
    check50.exists("cards.c")


@check50.check(exists)
def compiles():
    """cards compiles"""
    check50.c.compile("cards.c", lcs50=True)
