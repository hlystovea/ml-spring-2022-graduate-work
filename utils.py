import os

import numpy as np
import tensorlayerx as tlx
from PIL import Image

from srgan.srgan import SRGAN_g


weights_dir = 'srgan//models'

SRGANNet = SRGAN_g()
SRGANNet.init_build(tlx.nn.Input(shape=(8, 96, 96, 3)))
SRGANNet.load_weights(
    os.path.join(weights_dir, 'g.npz'),
    format='npz_dict'
)
SRGANNet.set_eval()


def predict_hr_image(model: tlx.nn.Module, image: np.ndarray):
    image_tensor = (image / 127.5) - 1
    image_tensor = tlx.ops.convert_to_tensor(image_tensor, dtype=np.float32)

    out = tlx.ops.convert_to_numpy(model(np.array(image_tensor, ndmin=4)))
    out = np.asarray((out + 1) * 127.5, dtype=np.uint8)

    return Image.fromarray(out[0])


if __name__ == '__main__':
    os.environ['TL_BACKEND'] = 'tensorflow'

    path = input('Вставьте путь до изображения:')
    image = tlx.vision.load_image(path)

    hr_image = predict_hr_image(SRGANNet, image)
    hr_image.show()
