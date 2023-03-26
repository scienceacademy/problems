import check50

@check50.check()
def exists():
    """blackjack_score.py exists."""
    check50.exists("blackjack_score.py")

@check50.check(exists)
def hand1():
    """single card with value < 10"""
    check50.run("python blackjack_score.py 2H").stdout("2")

@check50.check(exists)
def hand2():
    """single card with value >= 10"""
    check50.run("python blackjack_score.py 10C").stdout("10")

@check50.check(exists)
def hand3():
    """w cards with a total < 21"""
    check50.run("python blackjack_score.py 4C 5H").stdout("9")

@check50.check(exists)
def hand4()):
    """2 cards with one ace, total > 21 if ace is 11"""
    check50.run("python blackjack_score.py 10S AH").stdout("11")

@check50.check(exists)
def hand5():
    """2 cards with 2 aces, one reduced to 1"""
    check50.run("python blackjack_score.py AC AS 8D").stdout("19")

@check50.check(exists)
def hand6():
    """3 cards with 2 aces, both reduced to 1"""
    check50.run("python blackjack_score.py AC AS 10D").stdout("12")

@check50.check(exists)
def hand7():
    """3 cards with one ace, worth 11"""
    check50.run("python blackjack_score.py AH 5C 2S").stdout("18")

@check50.check(exists)
def hand8()):
    """4 cards with one ace, reduced to 1"""
    check50.run("python blackjack_score.py AS 8D 4C 6D").stdout("19")

@check50.check(exists)
def hand10():
    """5 cards with two aces"""
    check50.run("python blackjack_score.py AS AC 3D 10C 6H").stdout("21")