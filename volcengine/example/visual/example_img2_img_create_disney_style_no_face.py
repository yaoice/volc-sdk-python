# coding:utf-8
from __future__ import print_function

from volcengine.visual.VisualService import VisualService

if __name__ == '__main__':
    visual_service = VisualService()

    # call below method if you don't set ak and sk in $HOME/.volc/config
    visual_service.set_ak('AK')
    visual_service.set_sk('SK')

    form = {
        "req_key": "image2image-ai_create-disneyStyle_noface",
        # "binary_data_base64":[],
        "image_urls": [
            "https://"
        ],
        "prompt": "",
        "sub_prompts": [
        ],
        "u_prompt": "embedding:EasyNegative, nsfw, (worst quality:2), (low quality:2)",
        "strength": 0.6,
        "seed": -1,
        "scale": 8,
        "ddim_steps": 20,
        "lora_map": {
            "3Dpet_Disney01": {
                "strength_clip": 0.6,
                "strength_model": 0.6
            }
        },
        "clip_skip": 1,
        "controlnet_weight": 0.4,
        "sampler_name": "dpmpp_2m",
        "scheduler": "karras",
        "long_resolution": 704,
        "cn_mode": 0,
        "id_weight": 1.0,
        "apply_id_layer": "2,3,4,5,6,7,8,9,10,11,12",
        "tagger_settings": {"switch": False},
        "return_url": True,
        "logo_info": {
            "add_logo": False,
            "position": 0,
            "language": 0,
            "opacity": 0.3
        }

    }

    resp = visual_service.img2_img_create_disney_style_no_face(form)
    print(resp)
