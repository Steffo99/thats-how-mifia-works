import typing
if typing.TYPE_CHECKING:
    from mifia.player import Player


class Event:
    """An abstract game event.

    Attributes:
        to: A list of players that should be notified of this event."""

    def __init__(self, to: typing.Union[None, "Player", typing.List["Player"]]):
        """Create the event.

        Args:
             to: The players that should receive this event. Can be :py:const:`None`, a single
                 :py:class:`mifia.Player` or a :py:class:`list` of :py:class:`mifia.Player`s.
        """
        if to is None:
            self.to = []
        elif isinstance(to, list):
            self.to: typing.List["Player"] = to
        else:
            self.to = [to]

    def __repr__(self):
        len_to = len(self.to)
        if len_to == 1:
            return f"<{self.__class__.__name__} -> {self.to[0].name}>"
        return f"<{self.__class__.__name__} -> {len_to} players>"


class GameStarted(Event):
    """The game has advanced from the :py:const:`mifia.GameState.WAITING_FOR_PLAYERS` to the
    :py:const:`mifia.GameState.IN_PROGRESS`.

    Attributes:
        to: A list of players that should be notified of this event."""


class GameEnded(Event):
    """The game has advanced from the :py:const:`mifia.GameState.IN_PROGRESS` to the
    :py:const:`mifia.GameState.ENDED`.

    Attributes:
        to: A list of players that should be notified of this event.
        results: A dict that maps players to a value that is either :py:const:`None` (null result), :py:const:`True`
         (win) or :py:const:`False` (loss)."""

    def __init__(self,
                 to: typing.Union[None, "Player", typing.List["Player"]],
                 results: typing.Dict["Player", typing.Optional[bool]]):
        super().__init__(to)
        self.results: typing.Dict["Player", typing.Optional[bool]] = results


class PlayerJoined(Event):
    """A new player has joined the game during the :py:const:`mifia.GameState.WAITING_FOR_PLAYERS`.

    Attributes:
        to: A list of players that should be notified of this event.
        joiner: The :py:class:`mifia.Player` that has joined the game."""

    def __init__(self, to: typing.Union[None, "Player", typing.List["Player"]], joiner: "Player"):
        super().__init__(to)
        self.joiner = joiner


class PlayerLeft(Event):
    """A player has left the game during the :py:const:`mifia.GameState.WAITING_FOR_PLAYERS`.

    Attributes:
        to: A list of players that should be notified of this event.
        leaver: The :py:class:`mifia.Player` that left the game."""
    
    def __init__(self, to: typing.Union[None, "Player", typing.List["Player"]], leaver: "Player"):
        super().__init__(to)
        self.leaver = leaver
