# -*- coding: utf-8 -*-

from module.network.RequestFactory import getURL
from module.plugins.internal.MultiHook import MultiHook


class OverLoadMe(MultiHook):
    __name__    = "OverLoadMe"
    __type__    = "hook"
    __version__ = "0.02"

    __config__ = [("https", "bool", "Enable HTTPS", True),
                  ("hosterListMode", "all;listed;unlisted", "Use for hosters (if supported):", "all"),
                  ("hosterList", "str", "Hoster list (comma separated)", ""),
                  ("unloadFailing", "bool", "Revert to standard download if download fails", False),
                  ("interval", "int", "Reload interval in hours (0 to disable)", 12)]

    __description__ = """Over-Load.me hook plugin"""
    __license__     = "GPLv3"
    __authors__     = [("marley", "marley@over-load.me")]


    def getHoster(self):
        https = "https" if self.getConfig("https") else "http"
        page = getURL(https + "://api.over-load.me/hoster.php",
                      get={'auth': "0001-cb1f24dadb3aa487bda5afd3b76298935329be7700cd7-5329be77-00cf-1ca0135f"}).replace("\"", "").strip()
        self.logDebug("Hosterlist", page)

        return [x.strip() for x in page.split(",") if x.strip()]
