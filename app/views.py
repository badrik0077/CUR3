from flask import Blueprint, render_template, abort

from app.DAO.post_dao import PostDAO
from app.DAO.comments_dao import CommentsDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS, DATA_PATH_BOOKMARKS


post_blueprint = Blueprint('blueprint_post', __name__, template_folder='../templates')
posts_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentsDAO(DATA_PATH_COMMENTS)


@post_blueprint.get('/')
def all_posts_page():
    all_posts = posts_dao.get_all()
    return render_template('index.html', posts=all_posts)


@post_blueprint.get('/post/<int:pk>')
def one_posts_page(pk):
    one_post = posts_dao.get_by_pk(pk)
    comments = comments_dao.get_comments_by_post_id(post_id=pk)
    if one_post is None:
        abort(404)
    return render_template('post.html', post=one_post, comments=comments, len_comments=len(comments))


@post_blueprint.get('/user/<user_name>')
def page_by_user_name(user_name):
    posts = posts_dao.get_by_poster(user_name)
    return render_template('user-feed.html', posts=posts, user_name=user_name)
