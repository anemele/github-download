from .core import get_release_info, query_release


def test_query_release():
    r = query_release('neovim/neovim')
    assert r is not None
    assert type(r) is list
    assert len(r) > 0
    assert type(r[0]['assets']) is list


def test_get_release_info():
    r = query_release('neovim/neovim')
    assert r is not None
    info = get_release_info(r)
    assert len(info) > 1
