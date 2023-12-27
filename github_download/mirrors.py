def mirror_gh_ddlc_top(url: str) -> str:
    site = 'https://gh.ddlc.top/'
    return site + url


def mirror_hub_nuaa_cf(url: str) -> str:
    site = 'hub.nuaa.cf'
    return url.replace('github.com', site, 1)


def mirror_hub_yzuu_cf(url: str) -> str:
    site = 'hub.yzuu.cf'
    return url.replace('github.com', site, 1)


MIRROR_SITE = (mirror_gh_ddlc_top, mirror_hub_nuaa_cf, mirror_hub_yzuu_cf)
