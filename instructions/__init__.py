from otree.api import *
import tablemaker

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Instructionspg0(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(num_rounds = tablemaker.C.NUM_ROUNDS)

class Instructionspg1(Page):
    pass

class Instructionspg2(Page):
    pass

class Instructionspg3(Page):
    pass

class Instructionspg4(Page):
    pass



page_sequence = [Instructionspg0, Instructionspg1, Instructionspg2, Instructionspg3, Instructionspg4]
