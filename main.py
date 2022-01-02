import base64
import os
from hashlib import md5

import cv2
import numpy as np
import uvicorn
from fastapi import FastAPI
from pydantic.main import BaseModel

from npu_inference import predict_single_image


class Item(BaseModel):
    appid: str
    base64_file: str
    text_corpus: str
    salt:  str
    sign: str


app = FastAPI()


@app.post("/style-text/")
async def synth(item: Item):
    appid = item.appid
    img_base64 = item.base64_file
    text_corpus = item.text_corpus
    salt = item.salt
    sign = item.sign

    check_sign = make_md5(appid + img_base64 + text_corpus +
                          str(salt) + 'Sy15kMSuph6p9h9MeZWr')

    if check_sign != sign:
        return {'code': 110, 'message': '参数被篡改'}

    img_decode = base64.b64decode(img_base64)
    nparr = np.frombuffer(img_decode, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    style_img_path = os.path.join('tmp', 'i_s.png')
    cv2.imwrite(style_img_path, img_np)

    o_f = predict_single_image(cv2.imread(style_img_path), text_corpus)
    cv2.imwrite('tmp/o_f.jpg', o_f)

    with open(os.path.join('tmp', 'o_f.jpg'), 'rb') as f:
        result_base64 = base64.b64encode(f.read()).decode()

    return {'code': 100, 'message': 'SUCCESS',
            'result_img': result_base64}


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


if __name__ == '__main__':
    uvicorn.run(app, port=8501, host='0.0.0.0')
