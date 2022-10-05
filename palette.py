import numpy as np
from sklearn.cluster import KMeans
import cv2


class PaletteGenerator():
    def __init__(self, img):
        self.img = cv2.imread(img)
        img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, (300,300), interpolation = cv2.INTER_AREA)
        self.img_array = img_resized.reshape(-1,3)

    def palette(self):
        self.cluster =  KMeans(n_clusters=5)
        x = self.cluster.fit(self.img_array)
        p = np.zeros(shape=(50,300, 3), dtype=np.uint8)
        step = 300 / x.cluster_centers_.shape[0]
        lst = enumerate(x.cluster_centers_)
        for i, center in lst:
            p[:, int(i * step):int((i + 1) * step), :] = center
        return p



