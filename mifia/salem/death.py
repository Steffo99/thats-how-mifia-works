from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .moment import Moment


class Death:
    def __init__(self, moment: "Moment"):
        self.moment = moment
