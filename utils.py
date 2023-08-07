import json

PATH_BOOKMARKS = 'data/bookmarks.json'
PATH_COMMENTS = 'data/comments.json'
PATH_POSTS = 'data/posts.json'


def get_posts_all():
    """ возвращает посты"""
    with open(PATH_POSTS, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    """ возвращает посты определенного пользователя"""
    posts = get_posts_all()
    post_by_user = []
    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            post_by_user.append(post)
    if len(post_by_user) > 0:
        return post_by_user
    raise ValueError("Пост по имени пользователя не найден!")


def get_comments_by_post_id(post_id):
    """ возвращает комментарии определенного поста"""
    with open(PATH_COMMENTS, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    comments_by_post_id = []
    for comment in comments:
        if post_id == comment['post_id']:
            comments_by_post_id.append(comment)
    if len(comments_by_post_id) > 0:
        return comments_by_post_id
    raise ValueError("Пост не найден!")


def search_for_posts(query):
    """ возвращает спиок постов по ключевому слову """
    posts = get_posts_all()
    list_posts_by_key_word = []
    for post in posts:
        if query.lower() in post['content'].lower():
            list_posts_by_key_word.append(post)
    return list_posts_by_key_word

def get_post_by_pk(pk):
    """ возыращает пост по его идентификатору  """
    post_all = get_posts_all()
    post = []
    for pos in post_all:
        if pk == pos['pk']:
            post.append(pos)
    return post

