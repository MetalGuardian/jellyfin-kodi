# -*- coding: utf-8 -*-

#################################################################################################

import logging
import os
import sys

import xbmc
import xbmcaddon

#################################################################################################

__addon__ = xbmcaddon.Addon(id='plugin.video.jellyfin')
__base__ = xbmc.translatePath(os.path.join(__addon__.getAddonInfo('path'), 'resources', 'lib')).decode('utf-8')
__libraries__ = xbmc.translatePath(os.path.join(__addon__.getAddonInfo('path'), 'libraries')).decode('utf-8')

sys.path.insert(0, __libraries__)
sys.path.append(__base__)

#################################################################################################

from entrypoint import Events

#################################################################################################

LOG = logging.getLogger("JELLYFIN.default")

#################################################################################################


if __name__ == "__main__":

    LOG.debug("--->[ default ]")

    try:
        Events()
    except Exception as error:
        LOG.exception(error)

    LOG.info("---<[ default ]")
