import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path):
    return OffsetImage(plt.imread(path))

paths = ['Pawn.png']

x = [170]
y = [960]
fig, ax = plt.subplots()
ax.scatter(x, y)
img = mpimg.imread('chessBoard.png')
imgplot = plt.imshow(img)
for x0, y0, path in zip(x, y,paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)
