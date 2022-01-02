from photo_translation import PhotoTranslation
import streamlit as st
from PIL import Image
import cv2

# Specify canvas parameters in application
st.sidebar.title("测试")
bg_image = st.sidebar.file_uploader("选择图片:",
                                    type=["png", "jpg"])

# language = st.sidebar.radio("选择语言:", ['zh', 'en'], key="1")

get_result = st.sidebar.button("运行")
realtime_update = st.sidebar.checkbox("Update in realtime", True)


def get_content(file_uploader):
    max_width = 700

    content = Image.open(file_uploader)
    bg_width, bg_height = content.size

    if bg_width > max_width:
        resize_height = int(max_width / bg_width * bg_height)
        content = content.resize((max_width, resize_height), Image.BILINEAR)
        bg_width, bg_height = max_width, resize_height
    return content, bg_width, bg_height


if bg_image is not None:

    # Get size of bg_image
    content, bg_width, bg_height = get_content(bg_image)
    st.markdown("## 原图:")
    st.image(content)

    style_img_path = 'result/i_s.png'
    fake_fusion_path = 'result/fake_fusion.png'

    content.save(style_img_path)

    if get_result:
        result = PhotoTranslation().get_result(style_img_path)
        cv2.imwrite(fake_fusion_path, result['fake_fusion'])
        st.markdown("## 文本检测、识别、翻译结果:")
        st.markdown("boxes: {}".format(result['boxes']))
        st.markdown("source: {}".format(result['source']))
        st.markdown("target: {}".format(result['target']))
        st.markdown("## 结果回填:")
        fake_fusion = Image.open(fake_fusion_path)
        st.image(fake_fusion)


