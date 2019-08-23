import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def board():
    img = mpimg.imread('chessBoard.png')
    imgplot = plt.imshow(img)
board()
