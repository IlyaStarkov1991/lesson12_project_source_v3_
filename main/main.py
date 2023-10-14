import logging
from flask import Blueprint, render_template, request
import json
import functions

main_page = Blueprint('main', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO, encoding="UTF-8")


@main_page.route('/')
def page_index():
    return render_template('index.html')


@main_page.route('/search/', methods=['GET'])
def page_post_list():
    kay = request.args.get('s')
    try:
        posts = functions.loaded_from_json()
    except FileNotFoundError as err:
        return render_template('post_list.html',
                               isinstance=False,
                               err=err
                               )
    except json.JSONDecodeError as err:
        return render_template('post_list.html',
                               isinstance=False,
                               err=err
                               )
    else:
        logging.info(f'Поиск идет нормально, ключ- {kay}')
        final_post_list = []
        for item in posts:
            split_str = functions.split_str(item['content'])
            if kay in split_str:
                final_post_list.append(item)
        return render_template('post_list.html',
                               kay=kay,
                               final_post_list=final_post_list,
                               isinstance=True
                               )
