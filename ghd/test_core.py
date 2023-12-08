from .core import query_release


def test_():
    r = query_release('neovim/neovim')
    assert r is not None
    assert type(r) is list
    assert len(r) > 0
    assert type(r[0]['assets']) is list
