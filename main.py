
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

# import json

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

# poin_sebelum = int()
# def bertambah()

# F <- move Forward 0
# R <- turn Right 3
# L <- turn Left 2
# T <- Throw 1

# def cek_penyerang(x,y,states):

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    data = request.json

    myURL = data['_links']['self']['href']
    dim = data['arena']['dims']
    x = int(data['arena']['state'][myURL]['x'])
    y = int(data['arena']['state'][myURL]['y'])
    dir = data['arena']['state'][myURL]['direction']
    washit = data['arena']['state'][myURL]['wasHit']
    skor = data['arena']['state'][myURL]['score']
    pemain_lain = data['arena']['state']
    pemain_lain.pop(myURL)

    for pemain in pemain_lain:
        if (dir=='E' and int(pemain_lain[pemain]['x']) in range(x,x-4) and int(pemain_lain[pemain]['y'])==y) or (dir=='W' and int(pemain_lain[pemain]['x'])in range(x,x+4) and int(pemain_lain[pemain]['y'])==y) or (dir=='N' and int(pemain_lain[pemain]['x'])==x and int(pemain_lain[pemain]['y']) in range(y,y-4)) or (dir=='S' and int(pemain_lain[pemain]['x'])==x and int(pemain_lain[pemain]['y']) in range(y,y+4)):
            return moves[1]

    if y==int(dim[0])-1:
        if dir=='S':
            if x==0:
                return moves[2]
            elif x==int(dim[1])-1:
                return moves[3]
            else:
                return moves[random.choice([2,3])]
        elif dir=='E':
            if x==int(dim[1])-1:
                return moves[2]
            else:
                return moves[random.choice([0,1,2])]
        elif dir=='W':
            if x==0:
                return moves[3]
            else:
                return moves[random.choice([0,1,3])]
        else:
            return moves[random.randrange(len(moves))]
    elif y==0:
        if dir=='N':
            if x==0:
                return moves[3]
            elif y==int(dim[1])-1:
                return moves[2]
            else:
                return moves[random.choice([2,3])]
        elif dir=='W':
            if y==0:
                return moves[2]
            else:
                return moves[random.choice([0,1,2])]
        elif dir=='E':
            if y==int(dim[1])-1:
                return moves[3]
            else:
                return moves[random.choice([0,1,3])]
        else:
            return moves[random.randrange(len(moves))]

    # W barat
    # E timur
    # S selatan
    # N atas

    if bool(washit) == True:
        return moves[0]
    
    if int(skor) <= 0:
        return moves[1]
    # logger.info(data)

    return moves[random.choice([0,2,3])]

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
# {
#   "_links": {
#     "self": {
#       "href": "https://foo.com"
#     }
#   },
#   "arena": {
#     "dims": [4,3],
#     "state": {
#       "https://foo.com": {
#         "x": 0,
#         "y": 0,
#         "direction": "N",
#         "wasHit": false,
#         "score": 0
#       }
#     }
#   }
# }'

# {
# '_links': {
#     'self': {
#     'href': 'https://cloud-run-hackathon-python-t6fxfduwiq-uc.a.run.app'
#     }
#     }, 
# 'arena': {
#     'dims': [13, 9], 
#     'state': {
#         'https://go-bot-imrenagi-x2wnjf2lxq-uc.a.run.app/': {
#             'x': 3, 'y': 8, 'direction': 'W', 'wasHit': False, 'score': 23
#             }, 
#         'https://cloud-run-hackathon-java-springboot-tw-ce-tsxbksy6yq-uc.a.run.app': {
#             'x': 2, 'y': 2, 'direction': 'E', 'wasHit': False, 'score': 24
#             },
#         'https://go-bot-day01-01-x2wnjf2lxq-uc.a.run.app': {
#             'x': 9, 'y': 8, 'direction': 'E', 'wasHit': False, 'score': 24
#             },
#         'https://cloud-run-hackathon-python-2hjc2p3bha-uc.a.run.app': {
#             'x': 10, 'y': 1, 'direction': 'W', 'wasHit': False, 'score': 1
#             }, 
#         'https://adipurnamk-4hftndal4a-uc.a.run.app/': {
#             'x': 4, 'y': 1, 'direction': 'S', 'wasHit': True, 'score': -37
#             }, 
#         'https://go-bot-day01-x2wnjf2lxq-uc.a.run.app': {
#             'x': 4, 'y': 4, 'direction': 'N', 'wasHit': False, 'score': 14
#             }, 
#         'https://go-bot-tuanrumah-x2wnjf2lxq-uc.a.run.app': {
#             'x': 11, 'y': 6, 'direction': 'E', 'wasHit': False, 'score': 21
#         }, 
#         'https://cloud-run-hackathon-go-7r7t7po5kq-uc.a.run.app': {
#             'x': 5, 'y': 2, 'direction': 'E', 'wasHit': True, 'score': -4
#         }, 
#         'https://radiation70-zaiqduddka-uc.a.run.app': {
#             'x': 0, 'y': 8, 'direction': 'W', 'wasHit': True, 'score': -23
#         }, 
#         'https://cloud-run-hackathon-python-t6fxfduwiq-uc.a.run.app': {
#             'x': 12, 'y': 7, 'direction': 'S', 'wasHit': True, 'score': -5
#         }, 
#         'https://go-bot-google-x2wnjf2lxq-uc.a.run.app': {
#             'x': 11, 'y': 2, 'direction': 'S', 'wasHit': False, 'score': 15
#         }, 
#         'https://destroyers-khcaftcuka-uc.a.run.app/': {
#             'x': 10, 'y': 8, 'direction': 'E', 'wasHit': True, 'score': -14
#         }, 
#         'https://cloud-run-hackathon-python-i7i2w2dr4q-ue.a.run.app/': {
#             'x': 7, 'y': 4, 'direction': 'W', 'wasHit': False, 'score': -1
#         }, 
#         'https://totos-k6d3xjhhaq-uc.a.run.app': {
#             'x': 3, 'y': 1, 'direction': 'S', 'wasHit': False, 'score': 3
#         }, 
#         'https://supirman-227z7wpt7a-uc.a.run.app': {
#             'x': 10, 'y': 5, 'direction': 'N', 'wasHit': False, 'score': -20
#         }, 
#         'https://cloud-run-hackathon-nodejs-c6uhvn24vq-uc.a.run.app/': {
#             'x': 11, 'y': 5, 'direction': 'S', 'wasHit': True, 'score': -12
#         }, 
#         'https://cloud-run-hackathon-python-m3lbszusoa-uc.a.run.app': {
#             'x': 12, 'y': 0, 'direction': 'S', 'wasHit': False, 'score': -11
#         }, 
#         'https://cloud-run-hackathon-nodejs-4xinxdxl3a-uc.a.run.app/': {
#             'x': 0, 'y': 6, 'direction': 'W', 'wasHit': False, 'score': 0
#         }, 
#         'https://cloud-run-hackathon-ibetubpnga-uc.a.run.app': {
#             'x': 10, 'y': 7, 'direction': 'N', 'wasHit': False, 'score': 2
#         }
#     }
# }
# }