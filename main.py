# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from osgeo import gdal,gdalconst,osr
import rasterio
import numpy as np
from rasterio.plot import show
from matplotlib import pyplot


def reprojectCoords(src_crs, dst_crs, coords):
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    xs, ys = fiona.transform.transform(src_crs, dst_crs, xs, ys)
    return [[x,y] for x,y in zip(xs, ys)]

 
def changeCoordinate( path ): 
    tif_image = rasterio.open( path )
    path = path
    band1 = tif_image.read(1)
    tif_image2 = rasterio.open( path )
    band1 = tif_image2.read(1)
    bands = tif_image2.read()
    band_1 = (255*(bands[0]/np.max(bands[0]))).astype(np.uint8)
    band_2 = (255*(bands[1]/np.max(bands[1]))).astype(np.uint8)
    band_3 = (255*(bands[2]/np.max(bands[2]))).astype(np.uint8)
    bands_scaled = np.stack([band_1, band_2, band_3])
    norm = (bands * (255 / np.max(bands))).astype(np.uint8)
    bands.shape,bands_scaled.shape
    fig, (axg, axl) = pyplot.subplots(1,2, figsize=(20,10))
    show(norm, ax=axg, title='Max global')
    show(bands_scaled, ax=axl, title='Max x banda')
    affine = np.mat([1, 2, 3])
    affine = affine[:,np.array([1, 2, 0])]

    with rasterio.open( '/content/drive/MyDrive/UNIVERSIDAD/Codefest Ad Astra/PRUEBAS CÓDIGO/img3asadsa.tif', 'w',
        driver='GTiff',
        height=bands_scaled.shape[1], width=bands_scaled.shape[2], count=bands_scaled.shape[0],
        dtype=bands_scaled.dtype, crs=tif_image2.crs, transform=rasterio.Affine(7.313851904760395e-05, 0.0, -73.067697363, 0.0, -7.313851904760395e-05, 5.794556998123805)) as image_transformed:
        
        image_transformed.write(bands_scaled)


rute = '/dbfs/mnt/mount_folder/type2/tif/recorte_1_m120_l4_20181228_rgbnn.tif'
changeCoordinate( rute )



def changeSizeImage( path ):

    PATHIN = path
    PATHOUT = '/content/drive/MyDrive/Codefest Ad Astra/PRUEBAS CÓDIGO/salida.tif'
    translateoptions = gdal.TranslateOptions(creationOptions=['COMPRESS=LZW', 'PREDICTOR=2'])
    outFile = gdal.Translate(PATHOUT, PATHIN, options=translateoptions)

    BAND1 = outFile.GetRasterBand(1) 
    BAND2 = outFile.GetRasterBand(2) 
    BAND3 = outFile.GetRasterBand(3) 
    b1 = BAND1.ReadAsArray() 
    b2 = BAND2.ReadAsArray() 
    b3 = BAND3.ReadAsArray() 
    img = np.dstack((b1, b2, b3)) 
    f = plt.figure() 
    plt.imshow(img) 
    plt.savefig('Tiff.tif') 
    plt.show()

