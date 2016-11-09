import os
import numpy as np
from PIL import Image
import random

#constants
cyan = [0,255,255]
red = [255,0,0]
black = (0,0,0)
white = [255,255,255]
npix = 400
dim = 15

def extendRow(row):
	larger = []
	for x in row:
		for i in range(dim):
			larger.append(x)
	return larger

def increaseDotSize(grid):
	larger = []
	for r in grid:
		for i in range(dim):
			larger.append(extendRow(r))
	return larger


def createPixelStereoGram():
	grid = [[cyan if random.randint(0,10) < 2 else white for x in range(npix)] for r in range(npix)]
	for r in range(npix):
		for c in range(npix):
			if grid[r][c] == cyan:
				if overlay_pixels[c,r] < 100: #== black:
					grid[r][c-1] = red
				elif c<(npix-1):
					grid[r][c+1] = red
	return grid

if __name__ == '__main__':
	filename = raw_input("Black and white overlay file: ")
	overlay = Image.open(filename)
	overlay = overlay.convert('L')
	overlay = overlay.resize((npix,npix))
	overlay_pixels = overlay.load()

	grid = createPixelStereoGram()
	grid = increaseDotSize(grid)

	img = Image.fromarray(np.uint8(grid), 'RGB')
	img.show()
	img.save('Dot_Stereograms/' + os.path.splitext(filename)[0] + '_rds.png')
