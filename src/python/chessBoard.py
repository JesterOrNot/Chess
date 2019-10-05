import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import __init__ # imports all the piece classes
pieces = __init__.pieces() # declares the class pieces locally as 'pieces'

# This function plots the image data for the sprites
def board():
    def getImage(path):
        return OffsetImage(plt.imread(path))
# This gets sprites images and puts it in a list
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
             pieces.blackPawn4.paths,
             pieces.blackPawn5.paths,
             pieces.blackPawn6.paths,
             pieces.blackPawn7.paths,
             pieces.blackPawn8.paths,
             pieces.blackRook1.paths,
             pieces.blackRook2.paths,
             pieces.blackKnight1.paths,
             pieces.blackKnight2.paths,
             pieces.blackQueen.paths,
             pieces.blackKing.paths]
# This get's each sprites x position
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
        pieces.blackPawn4.Position.get("x"),
        pieces.blackPawn5.Position.get("x"),
        pieces.blackPawn6.Position.get("x"),
        pieces.blackPawn7.Position.get("x"),
        pieces.blackPawn8.Position.get("x"),
        pieces.blackRook1.Position.get("x"),
        pieces.blackRook2.Position.get("x"),
        pieces.blackKnight1.Position.get("x"),
        pieces.blackKnight2.Position.get("x"),
        pieces.blackQueen.Position.get("x"),
        pieces.blackKing.Position.get("x")]
# This gets the pieces y position
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
        pieces.blackPawn4.Position.get("y"),
        pieces.blackPawn5.Position.get("y"),
        pieces.blackPawn6.Position.get("y"),
        pieces.blackPawn7.Position.get("y"),
        pieces.blackPawn8.Position.get("y"),
        pieces.blackRook1.Position.get("y"),
        pieces.blackRook2.Position.get("y"),
        pieces.blackKnight1.Position.get("y"),
        pieces.blackKnight2.Position.get("y"),
        pieces.blackQueen.Position.get("y"),
        pieces.blackKing.Position.get("y")]
    fig, ax = plt.subplots() # declares that the graph will be shown as a subplot (for asthetics and to declare a variable for the subplot)
    # This declares that the plot is a scatter_plot
    ax.scatter(x, y)
    ### for development we show these tick marks to help visualize each square on the board
    plt.xticks([100,240,380,520,650,780,910,1040,1180])
    plt.yticks([100,240,370,500,630,760,890,1020,1150])
    # plt.xticks([])  ## Uncomment this when in deployment
    # plt.yticks([])  ## Uncomment this when in deployment
    plt.grid(which='both',axis='both') # Comment this in deployment it shows the grid on the plot
    img = mpimg.imread('chessBoard.png') ## Creates the background image in this case the chess board
    imgplot = plt.imshow(img) ## shows the board
    for x0, y0, path in zip(x, y, paths): ## Loops through the lists and uses zip to make a set for each peice containing the path to the image and it's respective x & y coordinate
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False) ## reads the sprites
        ax.add_artist(ab) ### Shows the sprites
    plt.show() ### Displays the subplot


board()
