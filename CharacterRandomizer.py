import random

smart_random = False
force_best_fit = False
drop_lowest_stat_roll = False
show_extras = True
extras_list = []
rand_character_class = ""
rand_race = ""
rand_stats = True
rand_skills = True
rand_feats = True
rand_languages = True
rand_magic = True


def add_array(array1, array2):
    array3 = []
    for _ in range(len(array1)):
        array3.append(array1[_] + array2[_])
    return array3


def roll_random(sides, num_dice, drop_lowest):
    if drop_lowest:
        num_dice += 1
    roll_list = []
    for _ in range(num_dice):
        roll_list.append(random.randrange(1, sides + 1))
    roll_list.sort()
    if drop_lowest:
        roll_list.remove(roll_list[0])
    value = 0
    for _ in range(len(roll_list)):
        value += roll_list[_]
    return value


def randomize_class():
    classes = ["Barbarian", "Bard", "Fighter", "Monk", "Paladin", "Rogue", "Scout", "Warlock", "Wizard"]
    dwarf_classes = ["Barbarian", "Fighter", "Monk", "Paladin", "Warlock"]
    high_elf_classes = ["Bard", "Fighter", "Rogue", "Scout", "Warlock", "Wizard"]
    gnome_classes = ["Bard", "Paladin", "Wizard"]
    half_orc_classes = ["Fighter", "Monk", "Scout"]
    halfling_classes = ["Bard", "Fighter", "Monk", "Rogue", "Scout", "Warlock", "Wizard"]
    best_fit_classes = []
    if rand_race == "":
        return classes[random.randrange(0, len(classes))]
    elif rand_race == "Dwarf":
        if force_best_fit:
            best_fit_classes.append("Barbarian")
            best_fit_classes.append("Fighter")
            best_fit_classes.append("Monk")
            return best_fit_classes[random.randrange(0, len(best_fit_classes))]
        else:
            return dwarf_classes[random.randrange(0, len(dwarf_classes))]
    elif rand_race == "High Elf":
        if force_best_fit:
            return "Scout"
        else:
            return high_elf_classes[random.randrange(0, len(high_elf_classes))]
    elif rand_race == "Gray Elf":
        return "Wizard"
    elif rand_race == "Gnome":
        if force_best_fit:
            return "Bard"
        else:
            return gnome_classes[random.randrange(0, len(gnome_classes))]
    elif rand_race == "Half-Orc":
        if force_best_fit:
            return "Monk"
        else:
            return half_orc_classes[random.randrange(0, len(half_orc_classes))]
    elif rand_race == "Halfling":
        if force_best_fit:
            return "Rogue"
        else:
            return halfling_classes[random.randrange(0, len(halfling_classes))]
    elif rand_race == "Human":
        best_fit_classes.append("Paladin")
        best_fit_classes.append("Warlock")
        return best_fit_classes[random.randrange(0, len(best_fit_classes))]


def randomize_race(character_class):
    all_races = ["Dwarf", "High Elf", "Gray Elf", "Gnome", "Half-Orc", "Halfling", "Human"]
    barbarian_races = ["Dwarf", "Human"]
    bard_races = ["Gnome", "High Elf", "Human", "Halfling"]
    fighter_races = ["Dwarf", "High Elf", "Half-Orc", "Halfling", "Human"]
    monk_races = ["Dwarf", "Half-Orc", "Halfling", "Human"]
    paladin_races = ["Dwarf", "Gnome", "Human"]
    rogue_races = ["High Elf", "Halfling", "Human"]
    scout_races = ["High Elf", "Half-Orc", "Halfling", "Human"]
    warlock_races = ["Dwarf", "High Elf", "Halfling", "Human"]
    wizard_races = ["High Elf", "Gnome", "Halfling", "Human", "Gray Elf"]
    if smart_random:
        if character_class == "Barbarian":
            if force_best_fit:
                return "Dwarf"
            else:
                return barbarian_races[random.randrange(0, len(barbarian_races))]
        elif character_class == "Bard":
            if force_best_fit:
                return "Gnome"
            else:
                return bard_races[random.randrange(0, len(bard_races))]
        elif character_class == "Fighter":
            if force_best_fit:
                return "Dwarf"
            else:
                return fighter_races[random.randrange(0, len(fighter_races))]
        elif character_class == "Monk":
            if force_best_fit:
                return "Dwarf"
            else:
                return monk_races[random.randrange(0, len(monk_races))]
        elif character_class == "Paladin":
            if force_best_fit:
                return "Human"
            else:
                return paladin_races[random.randrange(0, len(paladin_races))]
        elif character_class == "Rogue":
            if force_best_fit:
                return "Halfling"
            else:
                return rogue_races[random.randrange(0, len(rogue_races))]
        elif character_class == "Scout":
            if force_best_fit:
                return "High Elf"
            else:
                return scout_races[random.randrange(0, len(scout_races))]
        elif character_class == "Warlock":
            if force_best_fit:
                return "Human"
            else:
                return warlock_races[random.randrange(0, len(warlock_races))]
        elif character_class == "Wizard":
            if force_best_fit:
                return "Gray Elf"
            else:
                return wizard_races[random.randrange(0, len(wizard_races))]
    else:
        return all_races[random.randrange(0, len(all_races))]


def randomize_stat_points(character_class, race):
    val1 = roll_random(6, 3, drop_lowest_stat_roll)
    val2 = roll_random(6, 3, drop_lowest_stat_roll)
    val3 = roll_random(6, 3, drop_lowest_stat_roll)
    val4 = roll_random(6, 3, drop_lowest_stat_roll)
    val5 = roll_random(6, 3, drop_lowest_stat_roll)
    val6 = roll_random(6, 3, drop_lowest_stat_roll)
    random_stats = [val1, val2, val3, val4, val5, val6]
    stats_reordered = []
    racial_bonus = []
    if race == "Dwarf":
        racial_bonus = [0, 0, 2, 0, 0, -2]
    elif race == "High Elf":
        racial_bonus = [0, 2, -2, 0, 0, 0]
    elif race == "Gray Elf":
        racial_bonus = [-2, 2, -2, 2, 0, 0]
    elif race == "Gnome":
        racial_bonus = [-2, 0, 2, 0, 0, 0]
    elif race == "Half-Orc":
        racial_bonus = [2, 0, 0, -2, 0, -2]
    elif race == "Halfling":
        racial_bonus = [-2, 2, 0, 0, 0, 0]
    elif race == "Human":
        racial_bonus = [0, 0, 0, 0, 0, 0]
    extras_list.append(racial_bonus)
    if smart_random:
        random_stats.sort(reverse=True)
        if character_class == "Barbarian":
            stats_reordered = add_array([random_stats[0], random_stats[2], random_stats[1], random_stats[4], random_stats[3], random_stats[5]], racial_bonus)
        elif character_class == "Bard":
            stats_reordered = add_array([random_stats[4], random_stats[3], random_stats[2], random_stats[1], random_stats[5], random_stats[0]], racial_bonus)
        elif character_class == "Fighter":
            stats_reordered = add_array([random_stats[0], random_stats[2], random_stats[1], random_stats[3], random_stats[4], random_stats[5]], racial_bonus)
        elif character_class == "Monk":
            stats_reordered = add_array([random_stats[0], random_stats[2], random_stats[1], random_stats[4], random_stats[3], random_stats[5]], racial_bonus)
        elif character_class == "Paladin":
            stats_reordered = add_array([random_stats[1], random_stats[4], random_stats[2], random_stats[5], random_stats[3], random_stats[0]], racial_bonus)
        elif character_class == "Rogue":
            stats_reordered = add_array([random_stats[5], random_stats[0], random_stats[2], random_stats[1], random_stats[3], random_stats[4]], racial_bonus)
        elif character_class == "Scout":
            stats_reordered = add_array([random_stats[3], random_stats[0], random_stats[1], random_stats[2], random_stats[4], random_stats[5]], racial_bonus)
        elif character_class == "Warlock":
            stats_reordered = add_array([random_stats[5], random_stats[1], random_stats[2], random_stats[3], random_stats[3], random_stats[0]], racial_bonus)
        elif character_class == "Wizard":
            stats_reordered = add_array([random_stats[4], random_stats[3], random_stats[1], random_stats[0], random_stats[2], random_stats[5]], racial_bonus)
    else:
        stats_reordered = add_array([random_stats[0], random_stats[1], random_stats[2], random_stats[3], random_stats[4], random_stats[5]], racial_bonus)
    return stats_reordered


def randomize_language(race, intelligence_modifier):
    all_languages = ["Abyssal", "Aquan", "Auran", "Celestial", "Common", "Draconic", "Dwarven", "Druidic", "Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "Sylvan", "Terran", "Undercommon"]
    dwarf_bonus_languages = ["Giant", "Gnome", "Goblin", "Orc", "Terran", "Undercommon"]
    elf_bonus_languages = ["Draconic", "Gnoll", "Gnome", "Goblin", "Orc", "Sylvan"]
    gnome_bonus_languages = ["Draconic", "Dwarven", "Elven", "Giant", "Goblin", "Orc"]
    half_orc_bonus_languages = ["Draconic", "Giant", "Gnoll", "Goblin", "Abyssal"]
    halfling_bonus_languages = ["Dwarven", "Elven", "Gnome", "Goblin", "Orc"]
    bonus_language = []
    if race == "Dwarf":
        if intelligence_modifier > 0:
            for _ in range(intelligence_modifier):
                bonus_language.append(dwarf_bonus_languages[random.randrange(0, len(dwarf_bonus_languages))])
                dwarf_bonus_languages.remove(bonus_language[_])
        return ["Common", "Dwarven"] + bonus_language
    elif race == "High Elf":
        if intelligence_modifier > 0:
            for _ in range(intelligence_modifier):
                bonus_language.append(elf_bonus_languages[random.randrange(0, len(elf_bonus_languages))])
                elf_bonus_languages.remove(bonus_language[_])
        return ["Common", "Elven"] + bonus_language
    elif race == "Gray Elf":
        if intelligence_modifier > 0:
            for _ in range(intelligence_modifier):
                bonus_language.append(elf_bonus_languages[random.randrange(0, len(elf_bonus_languages))])
                elf_bonus_languages.remove(bonus_language[_])
        return ["Common", "Elven"] + bonus_language
    elif race == "Gnome":
        if intelligence_modifier > 0:
            for _ in range(intelligence_modifier):
                bonus_language.append(gnome_bonus_languages[random.randrange(0, len(gnome_bonus_languages))])
                gnome_bonus_languages.remove(bonus_language[_])
        return ["Common", "Gnome"] + bonus_language
    elif race == "Half-Orc":
        if intelligence_modifier > 0:
            for _ in range(intelligence_modifier):
                bonus_language.append(half_orc_bonus_languages[random.randrange(0, len(half_orc_bonus_languages))])
                half_orc_bonus_languages.remove(bonus_language[_])
        return ["Common", "Orc"] + bonus_language
    elif race == "Halfling":
        if intelligence_modifier > 0:
            for _ in range(intelligence_modifier):
                bonus_language.append(halfling_bonus_languages[random.randrange(0, len(halfling_bonus_languages))])
                halfling_bonus_languages.remove(bonus_language[_])
        return ["Common", "Halfling"] + bonus_language
    elif race == "Human":
        if intelligence_modifier > 0:
            all_languages.remove("Druidic")
            all_languages.remove("Common")
            for _ in range(intelligence_modifier):
                bonus_language.append(all_languages[random.randrange(0, len(all_languages))])
                all_languages.remove(bonus_language[_])
        return ["Common"] + bonus_language


def randomize_feats(character_class, strength_modifier, dexterity_modifier, intelligence_modifier, wisdom_modifier):
    all_classless_feats_without_prerequisites = ["Acrobatic", "Agile", "Alertness", "Animal Affinity", "Armor Proficiency (Light)", "Athletic",
                                                 "Blind-Fight", "Combat Reflexes", "Deceitful", "Deft Hands", "Diligent", "Endurance", "Great Fortitude",
                                                 "Improved Counterspell", "Improved Initiative", "Improved Unarmed Strike", "Investigator", "Iron Will",
                                                 "Lightning Reflexes", "Magical Aptitude", "Martial Weapon Proficiency", "Negotiator", "Nimble Fingers",
                                                 "Persuasive", "Point Blank Shot", "Run", "Self-Sufficient", "Shield Proficiency", "Skill Focus",
                                                 "Stealthy", "Toughness", "Track"]
    all_spell_feats_without_prerequisites = ["Combat Casting", "Eschew Materials", "Magical Aptitude", "Spell Focus", "Spell Penetration"]


if rand_character_class == "":
    rand_character_class = randomize_class()
if rand_race == "":
    rand_race = randomize_race(rand_character_class)
print("Race: " + rand_race + ", Class: " + rand_character_class)
rand_stat_modifiers = []
if rand_stats:
    rand_stat_list = randomize_stat_points(rand_character_class, rand_race)
    for i in rand_stat_list:
        if i == 1:
            rand_stat_modifiers.append(-5)
        elif i <= 3:
            rand_stat_modifiers.append(-4)
        elif i <= 5:
            rand_stat_modifiers.append(-3)
        elif i <= 7:
            rand_stat_modifiers.append(-2)
        elif i <= 9:
            rand_stat_modifiers.append(-1)
        elif i <= 11:
            rand_stat_modifiers.append(0)
        elif i <= 13:
            rand_stat_modifiers.append(1)
        elif i <= 15:
            rand_stat_modifiers.append(2)
        elif i <= 17:
            rand_stat_modifiers.append(3)
        elif i <= 19:
            rand_stat_modifiers.append(4)
        elif i <= 21:
            rand_stat_modifiers.append(5)
    strength = rand_stat_list[0]
    dexterity = rand_stat_list[1]
    constitution = rand_stat_list[2]
    intelligence = rand_stat_list[3]
    wisdom = rand_stat_list[4]
    charisma = rand_stat_list[5]
else:
    for i in range(6):
        rand_stat_modifiers.append(0)
    strength = 10
    dexterity = 10
    constitution = 10
    intelligence = 10
    wisdom = 10
    charisma = 10
print("Str: " + str(strength) + ", Dex: " + str(dexterity) + ", Con: " + str(constitution) + ", Int: " + str(intelligence) + ", Wis: " + str(wisdom) + ", Cha: " + str(charisma))
if show_extras:
    print("Racial Bonuses: ", end=" ")
    print(extras_list[0])
    print("Stat Modifiers: ", end=" ")
    print(rand_stat_modifiers)
    print("")
if rand_languages:
    rand_language_list = randomize_language(rand_race, rand_stat_modifiers[3])
    print("Languages: ")
    for i in rand_language_list:
        print(i)
