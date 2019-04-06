[![Build Status](https://travis-ci.org/dorokhin/pyleo.svg?branch=master)](https://travis-ci.org/dorokhin/pyleo)
[![PyPI version](https://badge.fury.io/py/pyleo.svg)](https://badge.fury.io/py/pyleo)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyleo.svg?color=light-green)

# PyLeo - Unofficial Lingualeo API python library

## Installation

```bash
pip install pyleo
```

## Example usage

### CLI tool for upload dictionary (ororo.tv_dict*.csv) from Ororo.tv to LinguaLeo
```bash

pyleo upload -f ororo.tv_dict.csv -u your@email.mail -p Your_password
```
Where:
- `-f` - Ororo.tv  dictionary filename
- `-u` - LinguaLeo username
- `-p` - LinguaLeo password 
 

### Import as Python module
```python
import json
from pyleo.api import LeoApi

api_instance = LeoApi('your@ema.il', 'password')

if api_instance.need_auth:
    api_instance.auth()  # Authorize user

# add word to LinguaLeo user dictionary
api_instance.add_word('placebo', 'Имитация лекарства')

# get word translation from LinguaLeo
translation = json.loads(api_instance.get_translations('fake').decode('utf-8'))

print(json.dumps(translation, indent=4, sort_keys=True, ensure_ascii=False))
```

## sample API response

```json

{
    "_hash": "0000.0",
    "error_msg": "",
    "experienceSkills": null,
    "meatballs": 55,
    "notify_count": 2,
    "questData": {
        "leoClothing": 0,
        "meatballs": 55,
        "task_actions_finished": [
            [
                1,
                1
            ]
        ],
        "task_num": 1,
        "task_num_prev": 0,
        "task_state": 2
    },
    "userdict3": {
        "is_user": false,
        "lang": {
            "current": "ru",
            "target": "en"
        },
        "lemmas": [
            {
                "lemma_id": 15421,
                "lemma_value": "FAKE",
                "speech_part": {
                    "code": "Noun",
                    "name": "существительное",
                    "short_name": "сущ."
                },
                "speech_part_id": 7
            },
            {
                "lemma_id": 15421,
                "lemma_value": "FAKE",
                "speech_part": {
                    "code": "Verb",
                    "name": "глагол",
                    "short_name": "глаг."
                },
                "speech_part_id": 12
            }
        ],
        "sound_url": "https://audiocdn.lingualeo.com/v2/1/15421-631152008.mp3",
        "transcription": "feɪk",
        "translations": [
            {
                "is_blame": 0,
                "is_owner": false,
                "is_user": 0,
                "rating": 1,
                "rating_avg": 0.206543,
                "rating_user_vote": 0,
                "source": "",
                "speech_part_id": 0,
                "star": 1,
                "translate_id": 29600,
                "translate_value": "подделка",
                "translate_votes": 56991
            },
            {
                "is_blame": 0,
                "is_owner": false,
                "is_user": 0,
                "rating": 0,
                "rating_avg": 0.2,
                "rating_user_vote": 0,
                "source": "",
                "speech_part_id": 0,
                "star": 3,
                "translate_id": 29604,
                "translate_value": "прикидываться",
                "translate_votes": 14627
            },
            {
                "is_blame": 0,
                "is_owner": false,
                "is_user": 0,
                "rating": 0,
                "rating_avg": 0.2,
                "rating_user_vote": 0,
                "source": "",
                "speech_part_id": 0,
                "star": 3,
                "translate_id": 2630670,
                "translate_value": "мошенничать",
                "translate_votes": 9581
            },
            {
                "is_blame": 0,
                "is_owner": false,
                "is_user": 0,
                "rating": 0,
                "rating_avg": 0.2,
                "rating_user_vote": 0,
                "source": "",
                "speech_part_id": 0,
                "star": 3,
                "translate_id": 135960,
                "translate_value": "фальшивый",
                "translate_votes": 4921
            },
            {
                "is_blame": 0,
                "is_owner": false,
                "is_user": 0,
                "rating": 0,
                "rating_avg": 0.2,
                "rating_user_vote": 0,
                "source": "",
                "speech_part_id": 7,
                "star": 3,
                "translate_id": 4021671,
                "translate_value": "подделка",
                "translate_votes": 3951
            }
        ],
        "word_count": 44926,
        "word_id": 15421,
        "word_speech_parts": {
            "12": {
                "code": "Verb",
                "name": "глагол",
                "short_name": "глаг."
            },
            "7": {
                "code": "Noun",
                "name": "существительное",
                "short_name": "сущ."
            }
        },
        "word_top": 3,
        "word_type": 1,
        "word_value": "fake"
    },
    "utcServerTime": 1551600000
}

```
