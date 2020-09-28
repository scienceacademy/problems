import check50

@check50.check()
def exists():
    """scrabble.py exists"""
    check50.exists("scrabble.py")

@check50.check(exists)
def tie_letter_case():
    """handles letter cases correctly"""
    check50.run("python3 scrabble.py").stdin("LETTERCASE").stdin("lettercase").stdout("Tie!").exit(0)

@check50.check(exists)
def tie_punctuation():
    """handles punctuation correctly"""
    check50.run("python3 scrabble.py").stdin("Punctuation!?!?").stdin("punctuation").stdout("Tie!").exit(0)

@check50.check(exists)
def test1():
    """correctly identifies 'Question?' and 'Question!' as a tie"""
    check50.run("python3 scrabble.py").stdin("Question?").stdin("Question!").stdout("Tie!").exit(0)

@check50.check(exists)
def test2():
    """correctly identifies 'hai!' as winner over 'Oh,'"""
    check50.run("python3 scrabble.py").stdin("Oh,").stdin("hai!").stdout("Player 2 wins!").exit(0)

@check50.check(exists)
def test3():
    """correctly identifies 'COMPUTER' as winner over 'science'"""
    check50.run("python3 scrabble.py").stdin("COMPUTER").stdin("science").stdout("Player 1 wins!").exit(0)

@check50.check(exists)
def test4():
    """correctly identifies 'Scrabble' as winner over 'wiNNeR'"""
    check50.run("python3 scrabble.py").stdin("Scrabble").stdin("wiNNeR").stdout("Player 1 wins!").exit(0)

@check50.check(exists)
def complex_case():
    """correctly identifies 'Skating!' as winner over 'figure?'"""
    check50.run("python3 scrabble.py").stdin("figure?").stdin("Skating!").stdout("Player 2 wins!").exit(0)

