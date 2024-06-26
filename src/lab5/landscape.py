import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np

def get_elevation(size):
    xpix, ypix = size
    elevation = np.array([])
    noise = PerlinNoise(octaves=10, seed=1)
    noise2 = PerlinNoise(octaves=100, seed=2)
    #noise3 = PerlinNoise(octaves=200, seed=3)


    xpix, ypix = size[0], size[1]
    #elevation = np.array([[noise([i / xpix, j/ypix]) for j in range(xpix)] for i in range (ypix)])

    result = []
    for i in range(xpix):
        row = []
        for j in range(ypix):
            val = noise([i/xpix, j/ypix])
            val += .5 * noise2([i/xpix, j/ypix])
            #val += .25 * noise3([i/xpix, j/ypix])

            row.append(val)
        result.append(row)

    elevation = np.array(result)
    '''Play around with perlin noise to get a better looking landscape (This is required for the lab)'''

    return elevation

def elevation_to_rgba(elevation, cmap='gist_earth'):
    xpix, ypix = np.array(elevation).shape
    colormap = plt.cm.get_cmap(cmap)
    elevation = (elevation - elevation.min())/(elevation.max()-elevation.min())
    ''' You can play around with colormap to get a landscape of your preference if you want '''
    landscape = np.array([colormap(elevation[i, j])[0:3] for i in range(xpix) for j in range(ypix)]).reshape(xpix, ypix, 3)*255
    landscape = landscape.astype('uint8')
    return landscape
 

get_landscape = lambda size: elevation_to_rgba(get_elevation(size))

if __name__ == '__main__':
    size = 640, 480
    pic = elevation_to_rgba(get_elevation(size))
    plt.imshow(pic, cmap='gist_earth')
    plt.show()