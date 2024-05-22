"""

Copyright (C) 2024 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2024 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

import sys
from disnake.gateway import _log

__all__ = [
    'BotWebSocket',
]

class BotWebSocket:
    
    """
    Presets for DiscordWebSocket
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Usage
    -----
    >>> from disnake.gateway import DiscordWebSocket
    >>> from disnakeBetter.ext import BotWebSocket
    >>> DiscordWebSocket.identify = BotWebSocket.func
    """

    def __init__(self) -> None:
        pass
  
    async def status_mobile(self):
        
        """
        Sets the status on mobile
        ~~~~~~~~~~~~~~~~~~~~~~~~~
        """

        payload = {
            'op': self.IDENTIFY,
            'd': {
                'token': self.token,
                'properties': {
                    '$os': sys.platform,
                    '$browser': 'Discord Android',
                    '$device': 'Discord Android',
                    '$referrer': '',
                    '$referring_domain': ''
                },
                'compress': True,
                'large_threshold': 250,
                'v': 3
            }
        }

        if self.shard_id is not None and self.shard_count is not None:
            payload['d']['shard'] = [self.shard_id, self.shard_count]

        state = self._connection
        if state._activity is not None or state._status is not None:
            payload['d']['presence'] = {
                'status': state._status,
                'game': state._activity,
                'since': 0,
                'afk': False
            }

        if state._intents is not None:
            payload['d']['intents'] = state._intents.value

        await self.call_hooks('before_identify', self.shard_id, initial=self._initial_identify)
        await self.send_as_json(payload)

        _log.info('Shard ID %s has sent the IDENTIFY payload.', self.shard_id)