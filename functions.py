import json
import logging

# logging.basicConfig(filename='basic.log')


def loaded_from_json():
    with open('posts.json', encoding='utf-8') as file:
        data = json.load(file)
        return data


def split_str(str):
    data_list = str.split(' ')
    return data_list


def safe_post_in_json(pic, content):
    data_list = loaded_from_json()
    with open('posts.json', 'w', encoding='utf-8') as file:
        post_dict = {
            "pic": f"{pic}",
            "content": f"{content}"
        }
        data_list.append(post_dict)
        json.dump(data_list, file, ensure_ascii=False)
