import check50

@check50.check()
def exists():
    """blackjack_score.py exists."""
    check50.exists("blackjack_score.py")

@check50.check(exists)
def hand1():
    """single card with value < 10"""
    check50.run("python blackjack_score.py 2H").stdout("2")
