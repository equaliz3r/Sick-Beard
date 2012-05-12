# Newshost provider for Sick Beard (v0.2.3)
# Provider Author: Yngvi (WooKi - http://wooki.za.net/)
# Sick Beard Author: Nic Wolfe <nic@wolfeden.ca>
# URL: http://code.google.com/p/sickbeard/
#
# This file is part of Sick Beard.
#
# Sick Beard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sick Beard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sick Beard.  If not, see <http://www.gnu.org/licenses/>. 

import sickbeard
from sickbeard import logger
from sickbeard import tvcache
import generic

class NewshostProvider(generic.NZBProvider):

    def __init__(self):

        generic.NZBProvider.__init__(self, "Newshost")

        self.cache = NewshostCache(self)

        self.url = 'http://www.newshost.za.net/'

    def imageName(self):
        return 'newshost.gif'

    def isEnabled(self):
        return sickbeard.NEWSHOST

class NewshostCache(tvcache.TVCache):

    def __init__(self, provider):

        tvcache.TVCache.__init__(self, provider)

        self.minTime = 5

    def _getRSSData(self):

        #SD: cat=7 | HD: cat=8 | RSS item display amount: n=50 (Change cat to your liking but leave n=50 alone!)
        url = 'http://www.newshost.za.net/rss.php?id='+ sickbeard.NEWSHOST_USERID +'&pass='+ sickbeard.NEWSHOST_AUTHKEY +'&cat='+ sickbeard.NEWSHOST_CAT +'&n=50'
        logger.log(u"Newshost cache update URL: "+ url, logger.DEBUG)

        data = self.provider.getURL(url)

        return data

    def _parseItem(self, item):

        (title, url) = self.provider._get_title_and_url(item)

        if not title or not url:
            logger.log(u"The XML returned from the Newshost RSS feed is incomplete, this result is unusable", logger.DEBUG)
            return

        logger.log(u"Adding item from RSS to cache: "+title, logger.DEBUG)

        self._addCacheEntry(title, url)

provider = NewshostProvider()
    
