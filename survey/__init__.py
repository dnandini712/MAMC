import json

from otree.api import *

doc = """
survey
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.StringField(choices=['Female', 'Male', 'Other'], widget=widgets.RadioSelectHorizontal, label="1. What is your gender?", blank=True)
    age = models.IntegerField(min=18, max=100, label="2. What is your age?", blank=True)
    race_h_l = models.StringField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal, label="3. Are you Hispanic or Latino?", blank=True)
    race = models.StringField(choices=['American Indian or Alaska Native', 'Asian', 'Black or African American', 'Native Hawaiian or Other Pacific Islander', 'White', 'Caucasian', 'Other', 'Prefer not to say'], widget=widgets.RadioSelectHorizontal, label="4. How would you describe yourself?", blank=True)
    college = models.IntegerField(label="5. How many years have you been at university/college?", blank=True)
    job = models.StringField(
        choices=["work at a full-time job?", "work at a part time job?", "not have a job?"], widget=widgets.RadioSelect, label="6. Do you", blank=True)
    major = models.StringField(choices=['Economics', 'Statistics', 'Mathematics', 'Business', 'Health', 'Social Sciences and History', 'Biological and Biomedical Sciences', 'Psychology', 'Computer and Information Sciences', ' Visual and Performing Arts', 'Communication and Journalism', 'Education', 'Architecture and Urban Studies', 'Agriculture and Life Studies', 'Engineering', 'Liberal Arts and Human Sciences', 'Natural Resources and Environment', 'Other'], widget=widgets.RadioSelectHorizontal, label='7. If applicable, what was/is your Major? (if more than one pick what you consider to be your primary Major)', blank=True)
    stat_experience = models.StringField(choices=['None', '1', '2', '3', '4 or more'], widget=widgets.RadioSelect, label='8. How many Statistics classes have you taken at the University level?', blank=True)
    risk = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], label='9. How willing or unwilling you are to take risks, using a scale from 0 to 10, where 0 means you are “completely unwilling to take risks” and 10 means you are “very willing to take risks”?', blank=True
    )
    discount = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='10. How willing are you to give up something that is beneficial for you today to benefit more from that in the future? Please again indicate your answer on a scale from 0 to 10. A 0 means “completely unwilling to do so,” and a 10 means “very willing to do so.”?', blank=True
    )
    goodatmath = models.IntegerField(
        widget=widgets.RadioSelectHorizontal,
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label='11. How well does the following statement describe you as a person? “I am good at math.” Please indicate your answer on a scale from 0 to 10. A 0 means “does not describe me at all,” and a 10 means “describes me perfectly.”', blank=True
    )

    mathq1 = models.IntegerField(min=1, max=100, label="12. A bat and a ball cost 44 dollars in total. The bat costs 40 dollars more than the ball. How many dollars does the ball cost?", blank=True)
    mathq2 = models.IntegerField(min=1, max=100,
                                 label="13. If it takes 6 machines 6 minutes to make 6 widgets, how many minutes would it take 200 machines to make 200 widgets?", blank=True)
    mathq3 = models.IntegerField(min=1, max=100,
                                 label="14. In a lake there is a patch of lily pads. Every day the patch doubles in size. If it takes 58 days for the patch to cover the entire lake, how many days would it take for the patch to cover half of the lake?", blank=True)

    bisbas1 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="15. A person's family is the most important thing in life.", blank=True
    )


    bisbas2 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="16. Even if something bad is about to happen to me, I rarely experience fear or nervousness.", blank=True
    )

    bisbas3 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="17. I go out of my way to get things I want.", blank=True
    )

    bisbas4 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="18. When I am doing well at something I love to keep at it.", blank=True
    )

    bisbas5 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="19. I am always willing to try something new if I think it will be fun.", blank=True
    )

    bisbas6 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="20. How I dress is important to me.", blank=True
    )
    bisbas7 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="21. When I get something I want, I feel excited and energized.", blank=True
    )

    bisbas8 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="22. Criticism or scolding hurts me quite a bit.", blank=True
    )

    bisbas9 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="23. When I want something I usually go all-out to get it.", blank=True
    )

    bisbas10 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="24. I will often do things for no other reason than that they might be fun.", blank=True
    )

    bisbas11 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="25. It is hard for me to find the time to do things such as get a haircut.", blank=True
    )

    bisbas12 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="26. If I see a chance to get something I want I move on it right away.", blank=True
    )

    bisbas13 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="27. I feel pretty worried or upset when I think or know somebody is angry at me.", blank=True
    )

    bisbas14 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="28. When I see an opportunity for something I like I get excited right away.", blank=True
    )

    bisbas15 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="29. I often act on the spur of the moment.", blank=True
    )

    bisbas16 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="30. If I think something unpleasant is going to happen I usually get pretty 'worked up.'", blank=True
    )

    bisbas17 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="31. I often wonder why people act the way they do.", blank=True
    )

    bisbas18 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="32. When good things happen to me, it affects me strongly.", blank=True
    )

    bisbas19 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="33. I feel worried when I think I have done poorly at something important.", blank=True
    )

    bisbas20 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="34. I crave excitement and new sensations.", blank=True
    )

    bisbas21 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="35. When I go after something I use a 'no holds barred' approach.", blank=True
    )

    bisbas22 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="36. I have very few fears compared to my friends.", blank=True
    )

    bisbas23 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="37. It would excite me to win a contest.", blank=True
    )

    bisbas24 = models.StringField(
        widget=widgets.RadioSelectHorizontal,
        choices=["Very true for me", "Somewhat true for me", "Somewhat false for me", "Very false for me"],
        label="38. I worry about making mistakes.", blank=True
    )

    bonus_round = models.IntegerField(initial=-1)


# PAGES
class survey1(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'race_h_l', 'race', 'college', 'job',
                   'major', 'stat_experience', 'risk', 'discount', 'goodatmath', 'mathq1', 'mathq2', 'mathq3']

class survey2(Page):
    form_model = 'player'
    form_fields = ['bisbas1', 'bisbas2', 'bisbas3', 'bisbas4', 'bisbas5', 'bisbas6', 'bisbas7', 'bisbas8','bisbas9', 'bisbas10',
                       'bisbas11',
                       'bisbas12',
                       'bisbas13',
                       'bisbas14',
                       'bisbas15',
                       'bisbas16',
                       'bisbas17',
                       'bisbas18',
                       'bisbas19',
                       'bisbas20',
                       'bisbas21',
                       'bisbas22',
                       'bisbas23',
                       'bisbas24']


class finalpage(Page):
    pass


class PaymentPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        try:
            labels = participant.vars['BONUS_LABELS']
            numbers_raw = participant.vars['BONUS_NUMBERS']
            round_number = participant.vars['BONUS_ROUND']

            # Set the bonus round on the player
            player.bonus_round = int(round_number)
        except:
            labels=None
            numbers_raw=None
            round_number=None

        numbers = None
        show_table = False


        if numbers_raw and labels:
            show_table = True
            numbers = json.loads(numbers_raw)

            #copy labels to prevent contaminating the original
            labels = labels.copy()
            labels.append('Total')

            # Add the totals to the end of the rows
            for k, v in numbers.items():
                total = sum(v)
                v.append(total)


        # get the bonus payment
        session = player.session
        bonus = participant.payoff.to_real_world_currency(session)

        return dict(
            numbers = numbers,
            column_names = labels,
            bonus = bonus,
            showup = player.session.config['participation_fee'],
            show_table = show_table,
            r = round_number,
        )

    @staticmethod
    def js_vars(player: Player):
        try:
            c =  player.participant.vars['BONUS_CHOICE']
        except:
            c='na'

        return dict(c=c)


page_sequence = [survey1, survey2, PaymentPage]