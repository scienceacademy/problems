import check50
import check50.c


@check50.check()
def exists():
    """anagram.c exists"""
    check50.exists("anagram.c")


@check50.check(exists)
def compiles():
    """anagram.c compiles"""
    check50.c.compile("anagram.c", lcs50=True)


@check50.check(compiles)
def test0():
    """Check for anagram"""
    check50.run("./anagram").stdin("earth").stdin("heart").stdout("ANAGRAM").exit(0)


@check50.check(compiles)
def test1():
    """Check for not anagram"""
    check50.run("./anagram").stdin("jellyfish").stdin("example").stdout("NOT ANAGRAM").exit(0)


@check50.check(compiles)
def test2():
    """Check for not match"""
    check50.run("./anagram").stdin("service").stdin("service").stdout("EXACT MATCH").exit(0)


@check50.check(compiles)
def test3():
    """Check for not non alphabetoc"""
    check50.run("./anagram").stdin("apple").stdin("color8").stdout("Alphabetic characters only.").exit(0)
