from .parser import parse_download_link


def test_parse_download_link():
    assert (
        parse_download_link('https://github.com/JuliaLang/juliaup/releases/tag/v1.12.5')
        == 'https://github.com/JuliaLang/juliaup/releases/download/v1.12.5'
    )
