# The equation is ROne = R + L(S - E)
# E = Expected Score
# R1 = Final Score
# ROne = initial rating
# S = the score
# K = Max charge(in this case 16)
# Equ for E is 1/10^((rb-ra/400))
# rb = initial rating of the opponent
# ra = initial rating of the player in question
player1 = {
    'elo': 2000
}
player2 = {
    'elo': 2000
}
game = {
    'score': 0
}
def elo():
    # We can feed input to this function
    rb = player2.get("elo")
    ra = player1.get("elo")
    k = 16
    s = game.get("score")
    r = player1.get("elo")
    e = 1/(10**((rb - ra)/400))
    par = s-e
    total = r+(k*par)
    return total
print(elo())
