from .parser import parse_download_link, parse_gh_release_view


def test_parse_download_link():
    assert (
        parse_download_link('https://github.com/JuliaLang/juliaup/releases/tag/v1.12.5')
        == 'https://github.com/JuliaLang/juliaup/releases/download/v1.12.5'
    )


def test_parse_gh_release_view():
    assert (
        parse_gh_release_view(
            '''title:	GitHub CLI 2.39.2
tag:	v2.39.2
draft:	false
prerelease:	false
author:	github-actions[bot]
created:	2023-11-27T17:50:31Z
published:	2023-11-27T18:04:17Z
url:	https://github.com/cli/cli/releases/tag/v2.39.2
asset:	gh_2.39.2_checksums.txt
asset:	gh_2.39.2_linux_386.deb
asset:	gh_2.39.2_linux_386.rpm
asset:	gh_2.39.2_linux_386.tar.gz
asset:	gh_2.39.2_linux_amd64.deb
asset:	gh_2.39.2_linux_amd64.rpm
asset:	gh_2.39.2_linux_amd64.tar.gz
asset:	gh_2.39.2_linux_arm64.deb
asset:	gh_2.39.2_linux_arm64.rpm
asset:	gh_2.39.2_linux_arm64.tar.gz
asset:	gh_2.39.2_linux_armv6.deb
asset:	gh_2.39.2_linux_armv6.rpm
asset:	gh_2.39.2_linux_armv6.tar.gz
asset:	gh_2.39.2_macOS_amd64.zip
asset:	gh_2.39.2_macOS_arm64.zip
asset:	gh_2.39.2_windows_386.msi
asset:	gh_2.39.2_windows_386.zip
asset:	gh_2.39.2_windows_amd64.msi
asset:	gh_2.39.2_windows_amd64.zip
asset:	gh_2.39.2_windows_arm64.zip
--
## What's Changed
* build(deps): bump github.com/creack/pty from 1.1.20 to 1.1.21 by @dependabot in https://github.com/cli/cli/pull/8345
* `gh repo sync` should be able to sync a local branch with an upstream remote by @benebsiny in https://github.com/cli/cli/pull/8229
* Update to latest go-gh by @samcoe in https://github.com/cli/cli/pull/8359
* Fix project status unmarshaling by @williammartin in https://github.com/cli/cli/pull/8384


**Full Changelog**: https://github.com/cli/cli/compare/v2.39.1...v2.39.2
'''
        )
        == (
            'https://github.com/cli/cli/releases/tag/v2.39.2',
            (
                'gh_2.39.2_checksums.txt',
                'gh_2.39.2_linux_386.deb',
                'gh_2.39.2_linux_386.rpm',
                'gh_2.39.2_linux_386.tar.gz',
                'gh_2.39.2_linux_amd64.deb',
                'gh_2.39.2_linux_amd64.rpm',
                'gh_2.39.2_linux_amd64.tar.gz',
                'gh_2.39.2_linux_arm64.deb',
                'gh_2.39.2_linux_arm64.rpm',
                'gh_2.39.2_linux_arm64.tar.gz',
                'gh_2.39.2_linux_armv6.deb',
                'gh_2.39.2_linux_armv6.rpm',
                'gh_2.39.2_linux_armv6.tar.gz',
                'gh_2.39.2_macOS_amd64.zip',
                'gh_2.39.2_macOS_arm64.zip',
                'gh_2.39.2_windows_386.msi',
                'gh_2.39.2_windows_386.zip',
                'gh_2.39.2_windows_amd64.msi',
                'gh_2.39.2_windows_amd64.zip',
                'gh_2.39.2_windows_arm64.zip',
            ),
        )
    )
