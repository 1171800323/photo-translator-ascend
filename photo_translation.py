import cv2
import numpy as np

from npu_inference import predict_single_image
from ocr import baidu_ocr
from translator import BaiduTranslator


class PhotoTranslation():
    def __init__(self, trans_appid='20210805000908153',
                 trans_appkey='bZsXXG7UDiWN0OSJwpG7',
                 synth_font_path={'zh': 'fonts/ch_standard.ttc',
                                  'en': 'fonts/en_standard.ttf'}):
        self.translator = BaiduTranslator(trans_appid, trans_appkey)

        self.font_path = synth_font_path

    def get_result(self, image_path, from_lang='en', to_lang='zh'):
        ocr_result = baidu_ocr(image_path)
        boxes = ocr_result["boxes"]
        txts = ocr_result["txts"]

        translator_result = self.translator.get_result(
            txts, from_lang=from_lang, to_lang=to_lang)

        img = cv2.imread(image_path)
        global_h, global_w = img.shape[:2]

        for i in range(len(boxes)):
            origin_text = txts[i]
            text_corpus = translator_result[i]

            if origin_text.lower() == text_corpus.lower():
                continue

            box = boxes[i]

            new_box = np.array(box, dtype=np.int64)
            point_x = new_box[:, 0]
            point_y = new_box[:, 1]
            min_x, max_x = np.min(point_x), np.max(point_x)
            min_y, max_y = np.min(point_y), np.max(point_y)

            h, w = max_y - min_y, max_x - min_x
            padding = 0.1
            border = int(min(h, w) * padding)
            min_x = max(min_x - 3 * border, 0)
            min_y = max(min_y - border, 0)
            max_x = min(max_x + 3 * border, global_w)
            max_y = min(max_y + border, global_h)

            style_img = img[min_y:max_y, min_x:max_x]
            synth_result = predict_single_image(style_img, text_corpus)

            img[min_y:max_y, min_x:max_x] = synth_result

        return {
            'fake_fusion': img,
            'boxes': boxes,
            'source': txts,
            'target': translator_result
        }


if __name__ == '__main__':
    result = PhotoTranslation().get_result('result/i_s.png')
    cv2.imwrite('fake_fusion.jpg', result['fake_fusion'])
    print(result['boxes'])
    print(result['source'])
    print(result['target'])
