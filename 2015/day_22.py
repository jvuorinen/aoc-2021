import re
from dataclasses import dataclass
from copy import copy
from utils import read, print_answers

OPP_HP, OPP_DMG = map(int, re.findall(r"\d+", read(2015, 22)))


@dataclass
class State:
    my_turn = True
    my_hp = 50
    my_armor = 0
    my_mana = 500
    opp_hp = OPP_HP
    opp_dmg = OPP_DMG
    shield = 0
    poison = 0
    recharge = 0
    total_mana_spent = 0

    def get_token(self):
        return (
            self.my_turn, self.my_hp, self.my_armor,self.my_mana, self.opp_hp,
            self.opp_dmg,self.shield, self.poison, self.recharge
        )
        

def get_actions(state):
    return [
        (spell, cost)
        for spell, cost, cooldown in [
            ("mm", 53, 0),
            ("dr", 73, 0),
            ("sh", 113, state.shield),
            ("ps", 173, state.poison),
            ("rc", 229, state.recharge),
        ]
        if cost <= state.my_mana and not cooldown
    ]


def apply_effects(state):
    _st = copy(state)
    _st.my_armor = 7 if _st.shield else 0
    if _st.poison:
        _st.opp_hp -= 3
    if _st.recharge:
        _st.my_mana += 101
    _st.shield = max(0, _st.shield - 1)
    _st.poison = max(0, _st.poison - 1)
    _st.recharge = max(0, _st.recharge - 1)
    return _st


def step(state, action=None):
    _st = copy(state)
    if _st.my_turn:
        spell, cost = action
        _st.my_mana -= cost
        _st.total_mana_spent += cost
        if spell == "mm":
            _st.opp_hp -= 4
        if spell == "dr":
            _st.my_hp += 2
            _st.opp_hp -= 2
        if spell == "sh":
            _st.shield = 6
        if spell == "ps":
            _st.poison = 6
        if spell == "rc":
            _st.recharge = 5
    else:
        _st.my_hp -= max(1, _st.opp_dmg - _st.my_armor)
    _st.my_turn = not _st.my_turn
    return _st


def fight(state, seen, results, part2):
    if (token := state.get_token()) not in seen:
        seen.add(token)
        if part2 and state.my_turn:
            state.my_hp -= 1
        state = apply_effects(state)
        if state.my_hp <= 0 or state.opp_hp <= 0:
            win = state.my_hp >= 0 and state.opp_hp <= 0
            results.add((win, state.total_mana_spent))
        elif state.my_turn:
            for a in get_actions(state):
                fight(step(state, a), seen, results, part2)
        else:
            fight(step(state), seen, results, part2)


def solve(part2=False):
    state, seen, results = State(), set(), set()
    fight(state, seen, results, part2)
    return min(score for win, score in results if win)

print_answers(solve(), solve(part2=True), day=22)
