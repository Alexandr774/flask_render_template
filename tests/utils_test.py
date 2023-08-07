import pytest
import utils


@pytest.fixture()
def posts():
    return utils.get_posts_all()


class TestMine:
    def test_get_posts_all(self, posts):
        assert type(posts) == list
        assert len(posts) > 0

    def test_get_posts_by_user(self):
        param = {
            "poster_name", "poster_avatar", "pic",
            "content", "views_count", "likes_count", "pk"}
        posts_by_user = utils.get_posts_by_user('johnny')[0]
        posts = set(posts_by_user)
        assert posts == param

    def test_get_posts_by_user_value_error(self):
        with pytest.raises(ValueError):
            utils.get_posts_by_user('johnn')

    def test_get_comments_by_post_id(self):
        assert type(utils.get_comments_by_post_id(1)) == list

    def test_get_comments_by_post_id_value_error(self):
        with pytest.raises(ValueError):
            utils.get_comments_by_post_id(-1)

    def test_search_for_posts(self):
        assert type(utils.search_for_posts('вышел')) == list
        assert len(utils.search_for_posts('вышел')) > 0

    def test_get_post_by_pk(self):
        assert len(utils.get_post_by_pk(1)) != 0

