#!/usr/bin/env python3

hp_id = 0
str_id = 1
int_id = 2
for_id = 3
spr_id = 4

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

    def __init__(self, data):
        self.name = data["name"]
        self.hp_boost = data["hp_boost"]
        self.strength_boost = data["strength_boost"]
        self.intelligence_boost = data["intelligence_boost"]
        self.fortitude_boost = data["fortitude_boost"]
        self.spirit_boost = data["spirit_boost"]

    def __str__(self):
        retfmt = "{} | HP: +{} | Str: +{} | Int: +{} | For: +{} | Spr: +{}"
        gem_values_tuple = (self.name, self.hp_boost, self.strength_boost,
                            self.intelligence_boost, self.fortitude_boost,
                            self.spirit_boost)
        return retfmt.format(*gem_values_tuple)

closed_data = {
    "name": "Closed slot",
    "hp_boost": 0,
    "strength_boost": 0,
    "intelligence_boost": 0,
    "fortitude_boost": 0,
    "spirit_boost": 0,
}

open_data = {
    "name": "Open slot",
    "hp_boost": 0,
    "strength_boost": 0,
    "intelligence_boost": 0,
    "fortitude_boost": 0,
    "spirit_boost": 0,
}

fire_data = {
    "name": "Fire gem",
    "hp_boost": 5,
    "strength_boost": 15,
    "intelligence_boost": 10,
    "fortitude_boost": 4,
    "spirit_boost": 8,
}

closed_slot = Gemstone(closed_data)
open_slot = Gemstone(open_data)
fire_gem = Gemstone(fire_data)

class Character():
    name = None
    hp = None
    strength = None
    intelligence = None
    fortitude = None
    spirit = None

    slots = [None,None,None,None,None]

    weapon_viant = None
    armor_viant = None
    accessory_viant = None
    gemstones = None

    def __init__(self, data):
        self.name = data["name"]
        self.weapon_viant = data["weapon_viant"]
        self.hp = 10
        self.strength = 10
        self.intelligence = 10
        self.fortitude = 10
        self.spirit = 10
        #print(self.weapon_viant)
        if self.weapon_viant.boosts_hp == True:
            self.slots[hp_id] = open_slot
        else:
            self.slots[hp_id] = closed_slot
        if self.weapon_viant.boosts_strength == True:
            self.slots[str_id] = open_slot
        else:
            self.slots[str_id] = closed_slot
        if self.weapon_viant.boosts_intelligence == True:
            self.slots[int_id] = open_slot
        else:
            self.slots[int_id] = closed_slot
        if self.weapon_viant.boosts_fortitude == True:
            self.slots[for_id] = open_slot
        else:
            self.slots[for_id] = closed_slot
        if self.weapon_viant.boosts_spirit == True:
            self.slots[spr_id] = open_slot
        else:
            self.slots[spr_id] = closed_slot

    def __str__(self):
        retfmt = "{} | HP: {} | Str: {} | Int: {} | For: {} | Spr: {}"
        #print(self.slots[str_id])
        char_values_tuple = (self.name, self.hp, self.strength,
                             self.intelligence, self.fortitude, self.spirit)
        return retfmt.format(*char_values_tuple)

    def equip(self, slot_id, gem):
        #print(gem)
        if(self.slots[slot_id] == closed_slot):
            return False
        else:
            self.slots[slot_id] = gem
        return True

fafnir = Viant(fafnir_data)
#print(fafnir)
#print(open_slot)

alice_data = {
    "name": "Alice",
    "weapon_viant": fafnir
}

alice = Character(alice_data)
alice.equip(str_id, fire_gem)
print(alice)
