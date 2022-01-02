# encoding:utf-8
import requests
import base64

def baidu_ocr(img_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = '24.429b8b858b6c20d4b71c862d21be9ef0.2592000.1634035325.282335-24838159'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    result_json = response.json()
    boxes = []
    txts = []
    for item in result_json['words_result']:
        txts.append(item['words'])
        location = item['location']
        top = location['top']
        left = location['left']
        width = location['width']
        height = location['height']
        boxes.append([[left, top],[left+width, top],[left+width, top+height],[left, top+height]])
        break
    return {
        'boxes': boxes,
        'txts': txts
    }

if __name__=='__main__':
    result = baidu_ocr('img_65.jpg')
    print(result)