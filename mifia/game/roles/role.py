import typing
from ...utils.limitedlist import LimitedList
if typing.TYPE_CHECKING:
    from ..player import Player


class Role:
    name: str = NotImplemented

    def __init__(self, player: Player):
        self.player: Player = player

    def on_dusk(self):
        pass

    def on_dawn(self):
        pass

    def before_death(self):
        pass

    def after_death(self):
        pass


class SingleTargetRole(Role):
    def __init__(self, player: Player):
        super().__init__(player)
        self.target: Player = None


class MultipleTargetRole(Role):
    max_targets = NotImplemented

    def __init__(self, player: Player):
        super().__init__(player)
        self.targets: LimitedList = LimitedList(max_length=self.max_targets)
