import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import __init__ # imports all the piece classes
pieces = __init__.Pieces() # declares the class pieces locally as 'pieces'

# This function plots the image data for the sprites
def board():
    def getImage(path):
        return OffsetImage(plt.imread(path))
# This gets sprites images and puts it in a list
    paths = [pieces.WhitePawn1.paths, pieces.WhitePawn2.paths, pieces.WhitePawn3.paths, pieces.WhitePawn4.paths, pieces.WhitePawn5.paths, pieces.WhitePawn6.paths,
             pieces.WhitePawn7.paths, pieces.WhitePawn1.paths, pieces.WhiteBishop1.paths, pieces.WhiteBishop2.paths, pieces.BlackBishop1.paths, pieces.BlackBishop2.paths,
             pieces.WhiteRook1.paths,
             pieces.WhiteRook2.paths,
             pieces.WhiteKnight1.paths,
             pieces.WhiteKnight2.paths,
             pieces.WhiteQueen.paths,
             pieces.WhiteKing.paths,
             pieces.BlackPawn1.paths,
             pieces.BlackPawn2.paths,
             pieces.BlackPawn3.paths,
             pieces.BlackPawn4.paths,
             pieces.BlackPawn5.paths,
             pieces.BlackPawn6.paths,
             pieces.BlackPawn7.paths,
             pieces.BlackPawn8.paths,
             pieces.BlackRook1.paths,
             pieces.BlackRook2.paths,
             pieces.BlackKnight1.paths,
             pieces.BlackKnight2.paths,
             pieces.BlackQueen.paths,
             pieces.BlackKing.paths]
# This get's each sprites x position
    x = [pieces.WhitePawn1.Position.get("x"), pieces.WhitePawn2.Position.get("x"), pieces.WhitePawn3.Position.get("x"), pieces.WhitePawn4.Position.get("x"), pieces.WhitePawn5.Position.get("x"), pieces.WhitePawn6.Position.get(
        "x"), pieces.WhitePawn7.Position.get("x"), pieces.WhitePawn8.Position.get("x"), pieces.WhiteBishop1.Position.get("x"), pieces.WhiteBishop2.Position.get("x"), pieces.BlackBishop1.Position.get("x"), pieces.BlackBishop2.Position.get("x"),
        pieces.WhiteRook1.Position.get("x"),
        pieces.WhiteRook2.Position.get("x"),
        pieces.WhiteKnight1.Position.get("x"),
        pieces.WhiteKnight2.Position.get("x"),
        pieces.WhiteQueen.Position.get("x"),
        pieces.WhiteKing.Position.get("x"),
        pieces.BlackPawn1.Position.get("x"),
        pieces.BlackPawn2.Position.get("x"),
        pieces.BlackPawn3.Position.get("x"),
        pieces.BlackPawn4.Position.get("x"),
        pieces.BlackPawn5.Position.get("x"),
        pieces.BlackPawn6.Position.get("x"),
        pieces.BlackPawn7.Position.get("x"),
        pieces.BlackPawn8.Position.get("x"),
        pieces.BlackRook1.Position.get("x"),
        pieces.BlackRook2.Position.get("x"),
        pieces.BlackKnight1.Position.get("x"),
        pieces.BlackKnight2.Position.get("x"),
        pieces.BlackQueen.Position.get("x"),
        pieces.BlackKing.Position.get("x")]
# This gets the pieces y position
    y = [pieces.WhitePawn1.Position.get("y"), pieces.WhitePawn2.Position.get(
        "y"), pieces.WhitePawn3.Position.get("y"), pieces.WhitePawn4.Position.get("y"), pieces.WhitePawn5.Position.get("y"), pieces.WhitePawn6.Position.get("y"), pieces.WhitePawn7.Position.get("y"), pieces.WhitePawn8.Position.get("y"), pieces.WhiteBishop1.Position.get("y"), pieces.WhiteBishop2.Position.get("y"), pieces.BlackBishop1.Position.get("y"), pieces.BlackBishop2.Position.get("y"),
        pieces.WhiteRook1.Position.get("y"),
        pieces.WhiteRook2.Position.get("y"),
        pieces.WhiteKnight1.Position.get("y"),
        pieces.WhiteKnight2.Position.get("y"),
        pieces.WhiteQueen.Position.get('y'),
        pieces.WhiteKing.Position.get("y"),
        pieces.BlackPawn1.Position.get("y"),
        pieces.BlackPawn2.Position.get("y"),
        pieces.BlackPawn3.Position.get("y"),
        pieces.BlackPawn4.Position.get("y"),
        pieces.BlackPawn5.Position.get("y"),
        pieces.BlackPawn6.Position.get("y"),
        pieces.BlackPawn7.Position.get("y"),
        pieces.BlackPawn8.Position.get("y"),
        pieces.BlackRook1.Position.get("y"),
        pieces.BlackRook2.Position.get("y"),
        pieces.BlackKnight1.Position.get("y"),
        pieces.BlackKnight2.Position.get("y"),
        pieces.BlackQueen.Position.get("y"),
        pieces.BlackKing.Position.get("y")]
    fig, ax = plt.subplots() # declares that the graph will be shown as a subplot (for asthetics and to declare a variable for the subplot)
    # This declares that the plot is a scatter_plot
    ax.scatter(x, y)
    ### for development we show these tick marks to help visualize each square on the board
    plt.xticks([100,240,380,520,650,780,910,1040,1180])
    plt.yticks([100,240,370,500,630,760,890,1020,1150])
    plt.xticks([])  ## Uncomment this when in deployment
    plt.yticks([])  ## Uncomment this when in deployment
    # plt.grid(which='both',axis='both') # Comment this in deployment it shows the grid on the plot
    img = mpimg.imread('Sprites/chessBoard.png') ## Creates the background image in this case the chess board
    imgplot = plt.imshow(img) ## shows the board
    for x0, y0, path in zip(x, y, paths): ## Loops through the lists and uses zip to make a set for each peice containing the path to the image and it's respective x & y coordinate
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False) ## reads the sprites
        ax.add_artist(ab) ### Shows the sprites
    plt.savefig("theBoard/chessBoard.png") ### Displays the subplot


board()
