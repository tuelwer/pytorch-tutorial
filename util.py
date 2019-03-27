import matplotlib.pyplot as plt
import numpy as np

def plot_grid(images, grid_size=(8,8), imsize=(28,28), file=None):
    fig = plt.figure(figsize=(10,10))
    imagerow = images[0].reshape(*imsize)
    for i in range(1,grid_size[0]):
            imagerow = np.hstack([imagerow, images[i].reshape(*imsize)])
    image = imagerow.copy()
    for j in range(1,grid_size[1]):
        imagerow = images[(grid_size[0]*j)].reshape(*imsize)
        for i in range(1, grid_size[0]):
            imagerow = np.hstack([imagerow,
                                  images[(grid_size[0]*j)+i].reshape(*imsize)])
        image = np.vstack([image, imagerow])
    plt.imshow(image, cmap = 'gray')
    plt.xticks([])
    plt.yticks([])
    if file is not None:
        plt.imsave(file,image, cmap='gray',dpi=200)
    else:
        plt.show() 
