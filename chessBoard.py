import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import __init__
pieces = __init__.pieces()


def board():
    def getImage(path):
        return OffsetImage(plt.imread(path))
# This gets the points and stuffs to plot the pieces
    paths = [pieces.whitePawn1.paths, pieces.whitePawn2.paths, pieces.whitePawn3.paths, pieces.whitePawn4.paths, pieces.whitePawn5.paths, pieces.whitePawn6.paths,
             pieces.whitePawn7.paths, pieces.whitePawn1.paths, pieces.whiteBishop1.paths, pieces.whiteBishop2.paths, pieces.blackBishop1.paths, pieces.blackBishop2.paths,
             pieces.whiteRook1.paths,
             pieces.whiteRook2.paths,
             pieces.whiteKnight1.paths,
             pieces.whiteKnight2.paths,
             pieces.whiteQueen.paths,
             pieces.whiteKing.paths,
             pieces.blackPawn1.paths,
             pieces.blackPawn2.paths,
             pieces.blackPawn3.paths,
             pieces.blackPawn4.paths]

    x = [pieces.whitePawn1.Position.get("x"), pieces.whitePawn2.Position.get("x"), pieces.whitePawn3.Position.get("x"), pieces.whitePawn4.Position.get("x"), pieces.whitePawn5.Position.get("x"), pieces.whitePawn6.Position.get(
        "x"), pieces.whitePawn7.Position.get("x"), pieces.whitePawn8.Position.get("x"), pieces.whiteBishop1.Position.get("x"), pieces.whiteBishop2.Position.get("x"), pieces.blackBishop1.Position.get("x"), pieces.blackBishop2.Position.get("x"),
        pieces.whiteRook1.Position.get("x"),
        pieces.whiteRook2.Position.get("x"),
        pieces.whiteKnight1.Position.get("x"),
        pieces.whiteKnight2.Position.get("x"),
        pieces.whiteQueen.Position.get("x"),
        pieces.whiteKing.Position.get("x"),
        pieces.blackPawn1.Position.get("x"),
        pieces.blackPawn2.Position.get("x"),
        pieces.blackPawn3.Position.get("x"),
        pieces.blackPawn4.Position.get("x")]

    y = [pieces.whitePawn1.Position.get("y"), pieces.whitePawn2.Position.get(
        "y"), pieces.whitePawn3.Position.get("y"), pieces.whitePawn4.Position.get("y"), pieces.whitePawn5.Position.get("y"), pieces.whitePawn6.Position.get("y"), pieces.whitePawn7.Position.get("y"), pieces.whitePawn8.Position.get("y"), pieces.whiteBishop1.Position.get("y"), pieces.whiteBishop2.Position.get("y"), pieces.blackBishop1.Position.get("y"), pieces.blackBishop2.Position.get("y"),
        pieces.whiteRook1.Position.get("y"),
        pieces.whiteRook2.Position.get("y"),
        pieces.whiteKnight1.Position.get("y"),
        pieces.whiteKnight2.Position.get("y"),
        pieces.whiteQueen.Position.get('y'),
        pieces.whiteKing.Position.get("y"),
        pieces.blackPawn1.Position.get("y"),
        pieces.blackPawn2.Position.get("y"),
        pieces.blackPawn3.Position.get("y"),
        pieces.blackPawn4.Position.get("y")]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.xticks([])
    plt.yticks([])
    img = mpimg.imread('chessBoard.png')
    imgplot = plt.imshow(img)
    for x0, y0, path in zip(x, y, paths):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)
    plt.show()


board()