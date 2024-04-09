"""
TODO
"""
from spoiler_alert_keep_out.rules_spec import RulesSpec, display_the_rules
from spoiler_alert_keep_out.boss_email_general import BossEmailTemplating
from spoiler_alert_keep_out.boss_emails import boss_emails
from spoiler_alert_keep_out.poker_rules import poker_rules

poker_boss = BossEmailTemplating("Poker", "the-bawss@instapoker.com")

def display_boss_email(level):
    """
    the boss's email at current level
    """
    poker_boss.print_email_headers(level)
    if level >= len(boss_emails):
        level = len(boss_emails) - 1
    print(boss_emails[level])

def display_test_level_info(level : int, submit):
    """
    TODO
    """
    if not submit:
        print("(Running your local tests only)")
    if level == 0:
        print("(Test Level 0: Not running incremental tests)")
    elif level == 1:
        print("(Running Incremental Tests for level 1)")
    elif level > 1:
        print(f"(Running Incremental Tests for levels 1 - {level})")

parsed_poker_rules = list(map(lambda raw: RulesSpec.parse(raw,len(boss_emails)),poker_rules))

def display_poker_rules(level : int):
    """
    display the rules text at current level
    """
    print()
    print(display_the_rules(parsed_poker_rules,level))
    print()
