import logging
from flask import Blueprint, render_template, request
import functions

load_post = Blueprint('load_post', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO, encoding="UTF-8")

ALLOWED_EXTENSION = {'jpeg', 'png', 'jpg'}


@load_post.route('/post/', methods=['GET', 'POST'])
def loaded_post_form():
    not_err = True
    return render_template('post_form.html', not_err=not_err)


@load_post.route('/uploads/', methods=['POST'])
def loaded_post_uploads():
    picture = request.files.get('picture')
    content = request.form.get('content')
    split_filename = picture.filename.split('.')[-1]

    if split_filename in ALLOWED_EXTENSION:
        try:
            functions.safe_post_in_json(picture.filename, content)
            picture.save(f'./uploads/images/{picture.filename}')
            posts = functions.loaded_from_json()
            return render_template(
                                    'post_uploaded.html',
                                    pic=posts[-1]['pic'],
                                    content=posts[-1]['content']
                                  )
        except OSError as errors:
            logging.error(f'Ошибка при загрузке файла: {errors}')
            err_message = 'Ошибка при загрузке файла'
            not_err = False
            return render_template(
                                    'post_form.html',
                                    err_message=err_message,
                                    not_err=not_err
                                  )
    else:
        logging.info('Расширение файла не соответсвует требованиям, загрузите фай формата: jpeg, jpg, png')
        err_message = 'Расширение файла не соответсвует требованиям, загрузите фай формата: jpeg, jpg, png'
        not_err = False
        return render_template(
                                'post_form.html',
                                err_message=err_message,
                                not_err=not_err
                               )
