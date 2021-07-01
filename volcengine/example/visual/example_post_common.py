# coding:utf-8
from __future__ import print_function

from volcengine.visual.VisualService import VisualService

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you dont set ak and sk in $HOME/.volc/config
    visual_service.set_ak('ak')
    visual_service.set_sk('sk')
    # visual_service.set_host('host')

    # below shows some common sdk using examples
    # you could find other examples in example/visual directory
    form = dict()
    form["image_base64"] = "image_base64_str"

    # 车牌检测
    # resp = visual_service.car_plate_detection(form)

    # 人像畸变矫正
    # resp = visual_service.distortion_free(form)

    # 图片拉伸修复
    # resp = visual_service.stretch_recovery(form)

    # 图片流动
    # form["motion_ratio"] = 2
    # resp = visual_service.image_flow(form)

    # 图片评分
    # resp = visual_service.image_score(form)

    # 图片配文
    # resp = visual_service.poem_material(form)

    # 表情编辑
    # form["service_choice"] = 0
    # resp = visual_service.emoticon_edit(form)

    # 闭眼转睁眼
    # resp = visual_service.eye_close2open(form)

    # 车辆分割
    # resp = visual_service.car_segment(form)

    # 车辆检测
    # resp = visual_service.car_detection(form)

    # 天空分割
    # resp = visual_service.sky_segment(form)

    # 老照片修复
    # resp = visual_service.convert_photo(form)

    # 图像增强
    # resp = visual_service.enhance_photo(form)

    # 通用分割
    # resp = visual_service.general_segment(form)

    # 人体分割
    # form["refine"] = 0
    # form["return_foreground_image"] = 0
    # resp = visual_service.human_segment(form)

    # 图像漫画风
    # form["rotation"] = 0
    # resp = visual_service.jpcartoon_cut(form)

    # 人脸融合
    # form["template_base64"] = "template_base64_str"
    # form["action_id"] = "faceswap"
    # resp = visual_service.face_swap(form)

    print(resp)
