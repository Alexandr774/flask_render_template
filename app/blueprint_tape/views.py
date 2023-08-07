from flask import Blueprint, render_template, request
import utils
import os

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/',  methods=['GET'])
def page_index():
    # if len(request.args['s']) > 0:
    #     word = request.args['s']
    #     key_post = utils.search_for_posts(word)
    #     return render_template('search.html')
    # else:
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)

@main_blueprint.route('/posts/<int:post_id>')
def page_post(post_id):
    comments = utils.get_comments_by_post_id(post_id)
    post = utils.get_post_by_pk(post_id)
    return render_template('post.html', post=post[0], comments=comments)


@main_blueprint.route('/search')
def search_post():
    word = request.args['s']
    post = utils.search_for_posts(word)
    return render_template('search.html', posts=post)

@main_blueprint.route('/users/<user_name>')
def user_page(user_name):
    post = utils.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=post)

