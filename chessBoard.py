import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import __init__
pieces = __init__.pieces()

def board():
  def getImage(path):
      return OffsetImage(plt.imread(path))

  paths = [pieces.whitePawn1.paths ,pieces.whitePawn2.paths,pieces.whitePawn3.paths,pieces.whitePawn4.paths,pieces.whitePawn5.paths,pieces.whitePawn6.paths,pieces.whitePawn7.paths,pieces.whitePawn1.paths,pieces.whiteBishop1.paths,pieces.whiteBishop2.paths,pieces.blackBishop1.paths,pieces.blackBishop2.paths]

  x = [170,320,440,590,710,830,980,1100,440,830,440,830]
  y = [960,960,960,960,960,960,960,960,1100,1100,180,180]
  fig, ax = plt.subplots()
  ax.scatter(x, y)
  plt.xticks([])
  plt.yticks([])
  img = mpimg.imread('chessBoard.png')
  imgplot = plt.imshow(img)
  for x0, y0, path in zip(x, y,paths):
      ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
      ax.add_artist(ab)
  plt.show()
board()
