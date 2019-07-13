import abc
import warnings

from .. import utils
from ..tl import TLObject, types
from ..tl.custom.chatgetter import ChatGetter


async def _into_id_set(client, chats):
    """Helper util to turn the input chat or chats into a set of IDs."""
    if chats is None:
        return None

    if not utils.is_list_like(chats):
        chats = (chats,)

    result = set()
    for chat in chats:
        if isinstance(chat, int):
            if chat < 0:
                result.add(chat)  # Explicitly marked IDs are negative
            else:
                result.update({  # Support all valid types of peers
                    utils.get_peer_id(types.PeerUser(chat)),
                    utils.get_peer_id(types.PeerChat(chat)),
                    utils.get_peer_id(types.PeerChannel(chat)),
                })
        elif isinstance(chat, TLObject) and chat.SUBCLASS_OF_ID == 0x2d45687:
            # 0x2d45687 == crc32(b'Peer')
            result.add(utils.get_peer_id(chat))
        else:
            chat = await client.get_input_entity(chat)
            if isinstance(chat, types.InputPeerSelf):
                chat = await client.get_me(input_peer=True)
            result.add(utils.get_peer_id(chat))

    return result


class EventBuilder(abc.ABC):
    """
    The common event builder, with builtin support to filter per chat.

    Args:
        chats (`entity`, optional):
            May be one or more entities (username/peer/etc.), preferably IDs.
            By default, only matching chats will be handled.

        blacklist_chats (`bool`, optional):
            Whether to treat the chats as a blacklist instead of
            as a whitelist (default). This means that every chat
            will be handled *except* those specified in ``chats``
            which will be ignored if ``blacklist_chats=True``.
    """
    self_id = None

    def __init__(self, chats=None, blacklist_chats=False):
        self.chats = chats
        self.blacklist_chats = blacklist_chats
        self._self_id = None

    @classmethod
    @abc.abstractmethod
    def build(cls, update):
        """Builds an event for the given update if possible, or returns None"""

    async def resolve(self, client):
        """Helper method to allow event builders to be resolved before usage"""
        self.chats = await _into_id_set(client, self.chats)
        if not EventBuilder.self_id:
            EventBuilder.self_id = await client.get_peer_id('me')

    def filter(self, event):
        """
        If the ID of ``event._chat_peer`` isn't in the chats set (or it is
        but the set is a blacklist) returns ``None``, otherwise the event.
        """
        if self.chats is not None:
            inside = utils.get_peer_id(event._chat_peer) in self.chats
            if inside == self.blacklist_chats:
                # If this chat matches but it's a blacklist ignore.
                # If it doesn't match but it's a whitelist ignore.
                return None
        return event


class EventCommon(ChatGetter, abc.ABC):
    """
    Intermediate class with common things to all events.

    Remember that this class implements `ChatGetter
    <telethon.tl.custom.chatgetter.ChatGetter>` which
    means you have access to all chat properties and methods.

    In addition, you can access the `original_update`
    field which contains the original :tl:`Update`.
    """
    _event_name = 'Event'

    def __init__(self, chat_peer=None, msg_id=None, broadcast=False):
        self._entities = {}
        self._client = None
        self._chat_peer = chat_peer
        self._message_id = msg_id
        self._input_chat = None
        self._chat = None
        self._broadcast = broadcast
        self.original_update = None

    def _set_client(self, client):
        """
        Setter so subclasses can act accordingly when the client is set.
        """
        self._client = client
        self._chat = self._entities.get(self.chat_id)
        if not self._chat:
            return

        self._input_chat = utils.get_input_peer(self._chat)
        if not getattr(self._input_chat, 'access_hash', True):
            # getattr with True to handle the InputPeerSelf() case
            try:
                self._input_chat = self._client.session.get_input_entity(
                    self._chat_peer
                )
            except ValueError:
                self._input_chat = None

    @property
    def client(self):
        """
        The `telethon.TelegramClient` that created this event.
        """
        return self._client

    def __str__(self):
        return TLObject.pretty_format(self.to_dict())

    def stringify(self):
        return TLObject.pretty_format(self.to_dict(), indent=0)

    def to_dict(self):
        d = {k: v for k, v in self.__dict__.items() if k[0] != '_'}
        d['_'] = self._event_name
        return d


def name_inner_event(cls):
    """Decorator to rename cls.Event 'Event' as 'cls.Event'"""
    if hasattr(cls, 'Event'):
        cls.Event._event_name = '{}.Event'.format(cls.__name__)
    else:
        warnings.warn('Class {} does not have a inner Event'.format(cls))
    return cls
