import check50


@check50.check()
def exists():
    """comp1-2.py exist."""
    check50.exists("comp1.py")
    check50.exists("comp2.py")


@check50.check(exists)
def test_p1():
    """comp1.py produces the correct output."""
    check50.run("python3 comp1.py").stdin("hello world").stdout("10 letter(s)\n").exit(0)


@check50.check(exists)
def test_p2():
    """comp2.py produces the correct output."""
    check50.run("python3 comp2.py").stdout("[2, 1.0, 6, 2.0, 10, 3.0, 14, 4.0, 18, 5.0, 22, 6.0, 26, 7.0, 30, 8.0, 34, 9.0, 38, 10.0, 42, 11.0, 46, 12.0, 50, 13.0, 54, 14.0, 58, 15.0, 62, 16.0, 66, 17.0, 70, 18.0, 74, 19.0, 78, 20.0, 82, 21.0, 86, 22.0, 90, 23.0, 94, 24.0, 98, 25.0, 102, 26.0, 106, 27.0, 110, 28.0, 114, 29.0, 118, 30.0, 122, 31.0, 126, 32.0, 130, 33.0, 134, 34.0, 138, 35.0, 142, 36.0, 146, 37.0, 150, 38.0, 154, 39.0, 158, 40.0, 162, 41.0, 166, 42.0, 170, 43.0, 174, 44.0, 178, 45.0, 182, 46.0, 186, 47.0, 190, 48.0, 194, 49.0, 198, 50.0]").exit(0)
