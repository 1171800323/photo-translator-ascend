import os

import cv2
import numpy as np

from render_standard_text import make_standard_text

data_h = 64
bin_save_path = 'tmp/bin'
font_path = 'fonts/ch_standard.ttc'


def predict_single_image(style_img, text_corpus):
    h, w = style_img.shape[:2]
    cv2.imwrite('tmp/i_s.png', style_img)
    text_img = make_standard_text(
        font_path, text_corpus, style_img.shape[:2])
    cv2.imwrite('tmp/i_t.png', text_img)
    np_style_img, data_w = preprocess(style_img)
    np_text_img, _ = preprocess(text_img)

    np_style_img.tofile(os.path.join(bin_save_path, 'i_s.bin'))
    np_text_img.tofile(os.path.join(bin_save_path, 'i_t.bin'))

    tools_path = "/home/HwHiAiUser/tools"
    app_path = "/home/HwHiAiUser/photo-translator"

    os.system("rm -rf tmp/output1")

    os.system("{}/msame/out/msame --model {}/model_weights/generator-{}.om --input {}/tmp/bin/i_t.bin,{}/tmp/bin/i_s.bin --output {}/tmp/output1 --outfmt BIN --loop 1".format(
        tools_path, app_path, data_w, app_path, app_path, app_path))

    output_path = os.listdir(os.path.abspath(
        os.path.join(os.getcwd(), "tmp/output1/")))[0]
    o_f = np.fromfile(os.path.join(os.path.abspath(os.path.join(os.getcwd(), ".")),
                                   "tmp/output1/{}/generator-{}_output_2.bin").format(output_path, data_w), dtype='float32')
    o_f = postprocess(o_f, (w, h), data_w)
    return o_f


def preprocess(img):
    h, w = img.shape[:2]
    new_img = img.copy()

    ratio = data_h / h
    predict_h = data_h
    predict_w = round(int(w * ratio) / 8) * 8
    predict_scale = (predict_w, predict_h)  # w first for cv2
    new_img = cv2.resize(img, predict_scale)
    print('resize_shape: ', str(predict_h), str(predict_w))
    if new_img.dtype == np.uint8:
        new_img = new_img.astype(np.float32) / 127.5 - 1
    change_format_img = new_img.transpose(2, 0, 1).copy()
    return change_format_img, predict_w


def postprocess(img, to_shape, data_w):
    img = np.reshape(img, (1, 3, 64, data_w))
    img = np.transpose(img, (0, 2, 3, 1))
    img = (img[0] + 1.) * 127.5
    img = img.astype(np.uint8)
    img = cv2.resize(img, to_shape)
    return img


if __name__ == '__main__':
    i_s = cv2.imread('tmp/002_i_s.png')
    result = predict_single_image(i_s, '江户川柯洁')
    cv2.imwrite('tmp/o_f.jpg', result)
