#!/usr/bin/env python3

class Viant():
    name = None
    boosts_hp = None
    boosts_strength = None
    boosts_intelligence = None
    boosts_fortitude = None
    boosts_spirit = None

    def __init__(self, data):
        self.name = data["name"]
        self.boosts_hp = data["hp"]
        self.boosts_strength = data["strength"]
        self.boosts_intelligence = data["intelligence"]
        self.boosts_fortitude = data["fortitude"]
        self.boosts_spirit = data["spirit"]

    def __str__(self):
        stat_list = []
        if self.boosts_hp:
            stat_list.append(" HP")
        else:
            stat_list.append("")
        if self.boosts_strength:
            stat_list.append(" Strength")
        else:
            stat_list.append("")
        if self.boosts_intelligence:
            stat_list.append(" Intelligence")
        else:
            stat_list.append("")
        if self.boosts_fortitude:
            stat_list.append(" Fortitude")
        else:
            stat_list.append("")
        if self.boosts_spirit:
            stat_list.append(" Spirit")
        else:
            stat_list.append("")
        return "Viant {}:{}{}{}{}{}".format(self.name, *stat_list)

fafnir_data = {
    "name": "Fafnir",
    "hp": False,
    "strength": True,
    "intelligence": False,
    "fortitude": False,
    "spirit": False
}

class Gemstone():
    name = None
    hp_boost = None
    strength_boost = None
    intelligence_boost = None
    fortitude_boost = None
    spirit_boost = None

class Character():
    name = None
    hp = None
    strength = None
    intelligence = None
    fortitude = None
    spirit = None

    weapon_viant = None
    armor_viant = None
    accessory_viant = None
    gemstones = None

    def __init__(self, data):
        self.name = data["name"]

fafnir = Viant(fafnir_data)
print(fafnir)

alice_data = {
    "name": "Alice"
}

alice = Character(alice_data)
