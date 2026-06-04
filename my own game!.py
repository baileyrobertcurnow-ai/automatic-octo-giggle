import os
import random
import json
import time

print("--- taken 1 seconds ---")
time.sleep(1)
print("--- taken 2 seconds ---")
time.sleep(1)
print("--- taken 3 seconds ---")
time.sleep(1)
print("--- RPG COMPLETELY INTEGRATED SYSTEM ---")
time.sleep(1)

# 1. VISUAL TERMINAL COLORS
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

#ask for name
name = input("enter your name here").upper()
#Tutorial for players
while True:
    print("Hi! welcome to my game in beta")
    time.sleep(2)
    print("this is the tutorial press C to continue the tutorial and S to skip")
    tutorial = input("Choose action: ").upper()
    if tutorial == "S":
        print("thank you for playing before or being impatient")
        time.sleep(6)
        break

    if tutorial == "C":
        print("thank you for choosing the tutorial")
        time.sleep(5)
        print("this is how the console is laid out")
        time.sleep(3)
        print("1.==========================================")
        print(f"2.HERO: {CYAN},player_name{RESET} the {YELLOW},chosen_class {RESET} | Level ,player_level")
        print("3.==========================================")
        time.sleep(6)
        print("=========================================")
        print(f"4.  YOUR HP: ,get_health_bar(,current_health, ,max_health) (,current_health/,max_health) | {BLUE}🛡️ DEF: ,defence_stat{RESET}")
        print(f"5. YOUR MP: {BLUE},current_mana/,max_mana{RESET} | ,CYAN🍀 LUCK: ,luck_stat{RESET}")
        print(f"6. {MAGENTA},current_enemy['name']{RESET}: ,get_health_bar(current_enemy['hp'] ,current_enemy['max_hp']) (,current_enemy['hp']/,current_enemy['max_hp'])")
        print("7. ==========================================")
        time.sleep(9)
        print("8. A = Strike | F = Fire | W = Water | V = Wind | M = Heal | R = Rest")
        print("9. I = View Inventory & Inspect Items | S = Save | C = Clear Screen | Q = Quit")
        time.sleep(5)
        print("some enemies have resistances and weaknesses, that is your job to find out")
        time.sleep(3)
        print("just a pointer, if you can't use spells or anything")
        print("like that it's because of your mp so you'll have to rest to continue")
        time.sleep(5)
        print("time to send you to the real world!")
        time.sleep(5)
        break
# -------------------------------------------------------
# SAVE & LOAD FUNCTIONS (added here, before anything else)
# -------------------------------------------------------
def save_game(filename="savegame.json"):
    filename = f"save_{name.lower()}.json"
    data = {
        "player_name": player_name,
        "chosen_class": chosen_class,
        "equipped_weapon": equipped_weapon,
        "weapon_multiplier": weapon_multiplier,
        "phys_mult": phys_mult,
        "spell_mult": spell_mult,
        "max_health": max_health,
        "max_mana": max_mana,
        "current_health": current_health,
        "current_mana": current_mana,
        "base_damage": base_damage,
        "luck_stat": luck_stat,
        "defence_stat": defence_stat,
        "player_level": player_level,
        "xp": xp,
        "xp_needed": xp_needed,
        "gold_coins": gold_coins,
        "current_wave": current_wave,
        "inventory": inventory,
        "mage_affinity": mage_affinity,
    }
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"{GREEN} Game saved!{RESET}")

def load_game(name):
    filename = f"save_{name.lower()}.json"
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as f:
        return json.load(f)
    
# -------------------------------------------------------
# CHECK FOR SAVE FILE FIRST — before class selection
# -------------------------------------------------------
save_data = load_game()

if save_data:
    print(f"\n{GREEN} Save file found!{RESET}")
    print(f"Found save: {save_data['player_name']} the {save_data['chosen_class']}, Level {save_data['player_level']}")
    load_choice = input("Load save? (Y/N): ").upper()

    if load_choice == "Y":
        player_name       = save_data["player_name"]
        chosen_class      = save_data["chosen_class"]
        equipped_weapon   = save_data["equipped_weapon"]
        weapon_multiplier = save_data["weapon_multiplier"]
        phys_mult         = save_data["phys_mult"]
        spell_mult        = save_data["spell_mult"]
        max_health        = save_data["max_health"]
        max_mana          = save_data["max_mana"]
        current_health    = save_data["current_health"]
        current_mana      = save_data["current_mana"]
        base_damage       = save_data["base_damage"]
        luck_stat         = save_data["luck_stat"]
        defence_stat      = save_data["defence_stat"]
        player_level      = save_data["player_level"]
        xp                = save_data["xp"]
        xp_needed         = save_data["xp_needed"]
        gold_coins        = save_data["gold_coins"]
        current_wave      = save_data["current_wave"]
        inventory         = save_data["inventory"]
        mage_affinity     = save_data["mage_affinity"]
        print(f" Welcome back, {YELLOW}{player_name}{RESET}!")
    else:
        save_data = None  # Fall through to new game below

# -------------------------------------------------------
# 2. CHARACTER SELECTION PHASE
# -------------------------------------------------------
print(f"\n{CYAN}=========================================={RESET}")
print(f"--- CHOOSE YOUR RECONSTRUCTED HERO ---")
print(f"{CYAN}=========================================={RESET}")
time.sleep(3)
print(f"1) {RED}WARRIOR{RESET}      - Weapon: Iron Broadsword (x1.3 DMG) | High HP (150)")
time.sleep(2)
print(f"2) {BLUE}MAGE{RESET}         - Weapon: Enchanted Wand (x1.4 Spell DMG) | Huge MP (80)")
time.sleep(2)
print(f"3) {CYAN}ARCHER{RESET}       - Weapon: Recurve Bow (x1.2 DMG) | Normal Archer (20)")
time.sleep(2)
print(f"4) {YELLOW}ALL-ROUNDER{RESET}  - Weapon: Training Sword (x1.1 DMG) | Perfectly Balanced")
time.sleep(2)
print(f"5) {MAGENTA}GUARDIAN{RESET}     - Weapon: Spiked Shield (x1.0 DMG) | Huge HP & DEF (15)")
time.sleep(2)
print(f"6) {GREEN}LEPRECHAUN{RESET}     - Weapon: coin (x1.25 DMG) | Extreme LUCK (40)")
time.sleep(2)

# Only runs if there was no save file, or the player chose N
if save_data is None:
    while True:
        class_choice = input("\nEnter your choice number (1-6): ")
        if class_choice == "1":
            chosen_class = "Warrior"
            max_health, max_mana, base_damage, luck_stat, defence_stat = 150, 10, 30, 3, 5
            equipped_weapon, weapon_multiplier = "Iron Broadsword", 1.3
            phys_mult = 2.0
            spell_mult = 0.5
            mage_affinity = None
            break
        elif class_choice == "2":
            chosen_class = "Mage"
            max_health, max_mana, base_damage, luck_stat, defence_stat = 70, 80, 10, 5, 1
            equipped_weapon, weapon_multiplier = "Enchanted Wand", 1.4
            phys_mult = 0.5
            spell_mult = 2.0
            mage_affinity = random.choice(["Fire", "Water", "Wind", "Earth"])
            print(f"{BLUE}Your magical affinity is: {mage_affinity}{RESET}")
            break
        elif class_choice == "3":
            chosen_class = "Archer"
            max_health, max_mana, base_damage, luck_stat, defence_stat = 90, 30, 20, 20, 3
            equipped_weapon, weapon_multiplier = "Recurve Bow", 1.2
            phys_mult = 1.0
            spell_mult = 0.8
            mage_affinity = None
            break
        elif class_choice == "4":
            chosen_class = "All-Rounder"
            max_health, max_mana, base_damage, luck_stat, defence_stat = 100, 40, 20, 5, 4
            equipped_weapon, weapon_multiplier = "Training Sword", 1.1
            phys_mult = 1.0
            spell_mult = 1.0
            mage_affinity = None
            break
        elif class_choice == "5":
            chosen_class = "Guardian"
            max_health, max_mana, base_damage, luck_stat, defence_stat = 160, 15, 15, -15, 15
            equipped_weapon, weapon_multiplier = "Spiked Shield", 1.0
            phys_mult = 0.75
            spell_mult = 0.75
            mage_affinity = None
            break
        elif class_choice == "6":
            chosen_class = "LEPRECHAUN"
            max_health, max_mana, base_damage, luck_stat, defence_stat = 50, 50, 25, 40, 5
            equipped_weapon, weapon_multiplier = "coin", 1.25
            phys_mult = 1.0
            spell_mult = 1.0
            mage_affinity = None
            break
        else:
            print(" Invalid input! Please enter a number between 1 and 6.")

    # Initialize tracking variables (only for new game)
    current_health = max_health
    current_mana = max_mana
    player_level = 1
    xp = 0
    xp_needed = int(100 * (1.25 ** (player_level - 1)))
    gold_coins = 50
    current_wave = 1
    inventory = ["Common Potion"]

    print(f"\n You spawn into the world as a {YELLOW}{chosen_class}{RESET} wielding a {YELLOW}{equipped_weapon}{RESET}!")
    player_name = input("Enter your character's name: ")

# -------------------------------------------------------
# 3. MASTER LOOT TABLES
# -------------------------------------------------------
loot_table = [
    {"name": "Godly Greatsword", "mult": 2.5, "rarity": "Legendary", "roll_needed": 95, "description": "A massive golden blade vibrating with celestial energy. It obliterates foes."},
    {"name": "Sharp Cutlass", "mult": 1.6, "rarity": "Rare", "roll_needed": 70, "description": "A curved pirate blade built for swift, slicing slashes."},
    {"name": "Iron Sword", "mult": 1.3, "rarity": "Common", "roll_needed": 40, "description": "A heavy, reliable standard-issue sword forged by village blacksmiths."},
    {"name": "Common potion", "rarity": "Medium-Rare", "roll_needed": 50, "desription": "A reliable potion"}
]

# -------------------------------------------------------
# 4. ENEMY DATABASE
# -------------------------------------------------------
enemies_pool = [
    {"name": "Dragon", "hp": 95, "max_hp": 95, "dodge": 20, "weakness": "Earth", "resist": "Fire", "dmg_mult": 1.0},
    {"name": "Phoenix (The Mythic Bird)", "hp": 90, "max_hp": 90, "dodge": 35, "weakness": "Water", "resist": "Wind/Fire", "dmg_mult": 1.0},
    {"name": "Fin (The Mighty Shark)", "hp": 100, "max_hp": 100, "dodge": 15, "weakness": "Wind/Fire", "resist": "Water", "dmg_mult": 1.0},
    {"name": "Goblin", "hp": 110, "max_hp": 110, "dodge": 10, "weakness": "fire", "resist": "wind", "dmg_mult": 1.0},
    {"name": "ant", "hp": 60, "max_hp": 60, "dodge": 75, "weakness": "water", "resist": "wind/Earth", "dmg_mult": 1.0},
    {"name": "skeleton", "hp": 80, "max_hp": 80, "dodge": 20, "weakness": "Physical", "resist": "None", "dmg_mult": 1.0}
]
elder_dragon_boss = {"name": "Elder Dragon (The Endgame Myth)", "hp":150, "max_hp": 150, "dodge": 25, "weakness": "Water", "resist": "Fire/Wind/Physical/Earth", "dmg_mult": 1.50}

#enemy health * level  
def spawn_enemy():
    enemy = random.choice(enemies_pool).copy()
    scale = 1 + (player_level * 0.10)
    enemy['hp'] = int(enemy['max_hp'] * scale)
    enemy['max_hp'] = enemy['hp']
    return enemy

current_enemy = spawn_enemy() 


def get_health_bar(curr, maximum):
    percentage = curr / maximum
    blocks = max(0, min(10, int(percentage * 10)))
    color = GREEN if percentage > 0.5 else (YELLOW if percentage > 0.2 else RED)
    return color + "█" * blocks + "░" * (10 - blocks) + RESET

# -------------------------------------------------------
# 5. MAIN INTERACTIVE GAMEPLAY LOOP
# -------------------------------------------------------
while True:
    # --- HUD DISPLAY ---
    print(f"\n==========================================")
    print(f"HERO: {CYAN}{player_name}{RESET} the {YELLOW}{chosen_class}{RESET} | Level {player_level}")
    print(f"XP: {xp}/{xp_needed} | {YELLOW} GOLD: {gold_coins}{RESET} | {MAGENTA}⚔️ WAVE: {current_wave}{RESET}")
    print(f"==========================================")
    print(f"  YOUR HP: {get_health_bar(current_health, max_health)} ({current_health}/{max_health}) | {BLUE} DEF: {defence_stat}{RESET}")
    print(f"  YOUR MP: {BLUE}{current_mana}/{max_mana}{RESET} | {CYAN} LUCK: {luck_stat}{RESET}")
    print(f" {MAGENTA}{current_enemy['name']}{RESET}: {get_health_bar(current_enemy['hp'], current_enemy['max_hp'])} ({current_enemy['hp']}/{current_enemy['max_hp']})")
    print(f"==========================================")
    print("A = Strike | F = Fire | W = Water | V = Wind | E = Earth | M = Heal | R = Rest")
    print("I = View Inventory & Inspect Items | S = Save | C = Clear Screen | Q = Quit")

    action = input("Choose action: ").upper()

    if action == "Q":
        print("\nThanks for playing! Goodbye!")
        break

    elif action == "S":
        save_game(name)
        continue

    elif action == "C":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n---- screen cleared! ----")
        continue

    elif action == "R":
        print(f"\n You take a long rest...")
        current_mana = min(max_mana, current_mana + 20 + (player_level * 2))
        print(f" MP Restored!")
        continue

    elif action == "M":
        if current_mana >= 15:
            current_mana -= 15
            current_health = min(max_health, current_health + 30 + (player_level * 5))
            print(f" Restored health using magic!")
        else:
            print(f"{MAGENTA} Out of Mana!{RESET}")
        continue

    elif action == "I":
        print(f"\n--- YOUR INVENTORY ---")
        if not inventory:
            print("[Bag is Empty]")
        for index, item in enumerate(inventory):
            print(f"{index + 1}: {item}")
        print("B = Back to fight")
        item_choice = input("Select an item number to inspect/use, or B to go back: ").upper()
        if item_choice == "B":
            continue
    
        try:
            chosen_index = int(item_choice) - 1
            selected_item = inventory[chosen_index]
            if "Potion" in selected_item:
                print(f"\n[INSPECT: {selected_item}] -> Restores 50 HP when drank.")
                confirm = input("Type 'USE' to drink it, or press Enter to go back: ").upper()
                if confirm == "USE":
                    current_health = min(max_health, current_health + 50)
                    inventory.pop(chosen_index)
                    print(f" Drank {selected_item}! Restored 50 HP.")
            else:
                for weapon in loot_table:
                    if weapon["name"] == selected_item:
                        print(f"\n[INSPECT: {YELLOW}{weapon['name']}{RESET}] ({weapon['rarity']})")
                        print(f" Description: {CYAN}{weapon['description']}{RESET}")
                        print(f"⚡ Damage Multiplier: {GREEN}x{weapon['mult']}{RESET}")
                        confirm = input("\nType 'EQUIP' to wield this weapon, or press Enter to go back: ").upper()
                        if confirm == "EQUIP":
                            inventory.append(equipped_weapon)
                            equipped_weapon = weapon["name"]
                            weapon_multiplier = weapon["mult"]
                            inventory.pop(chosen_index)
                            print(f" Equipped {YELLOW}{equipped_weapon}{RESET}!")
                        break
        except:
            print(" Invalid selection!")
        continue

    # --- ACTION RESOLUTION ENGINE ---
    spell_element, spell_cost, damage_multiplier = "Physical", 0, 1.0
    if action == "F":
        spell_element, spell_cost = "Fire", 15
    elif action == "W":
        spell_element, spell_cost = "Water", 15
    elif action == "V":
        spell_element, spell_cost = "Wind", 15
    elif action != "A":
        continue
    elif action == "E":
        spell_element, spell_cost = "Earth", 15

    if current_mana < spell_cost:
        print(f"{MAGENTA} Not enough mana!{RESET}")
        continue
    current_mana -= spell_cost

    # Dodge Check
    enemy_dodge_chance = max(5, current_enemy['dodge'] - luck_stat)
    if random.randint(1, 100) <= enemy_dodge_chance and spell_element == "Physical":
        print(f"{MAGENTA} The enemy DODGED your attack! (Dodge rate was {enemy_dodge_chance}%){RESET}")
        raw_boss_damage = random.randint(15, 30)
        final_boss_damage = max(1, raw_boss_damage - defence_stat)
        current_health -= final_boss_damage
        print(f"{RED} Struck back! Took {final_boss_damage} damage.{RESET}")
    else:
        # Damage Calculation
        if spell_element in ["Fire", "Water", "Wind", "Earth"]:
            if chosen_class == "mage" and spell_element == mage_affinity:
                affinity_cost = 8
                affinity_bonus = 1.5
            if current_mana < affinity_cost:
                print(f"{MAGENTA} Not enough mana!{RESET}")
                continue
            current_mana -= affinity_cost
            calculated_hit = int(base_damage * damage_multiplier * weapon_multiplier * spell_mult * affinity_bonus)
            print(f"{CYAN} Affinity spell! {RESET}")
        else:
            calculated_hit = int(base_damage * damage_multiplier * weapon_multiplier * spell_mult)
            
            if spell_element in current_enemy['resist']:
                damage_multiplier = 0.5
            elif spell_element == current_enemy['weakness']:
                damage_multiplier = 2.0
            calculated_hit = int(base_damage * damage_multiplier * weapon_multiplier * phys_mult)

        if random.randint(1, 100) >= max(50, 90 - luck_stat):
            calculated_hit *= 2
            print(f"{YELLOW} CRITICAL STRIKE!{RESET}")

        current_enemy['hp'] -= calculated_hit
        print(f" You dealt {YELLOW}{calculated_hit} damage{RESET} to {current_enemy['name']}!")

        if current_enemy['hp'] > 0:
            raw_boss_damage = int(random.randint(15, 30) * current_enemy['dmg_mult'])
            final_boss_damage = max(1, raw_boss_damage - defence_stat)
            current_health -= final_boss_damage
            print(f"{RED} {current_enemy['name']} counter-attacked! Dealt {raw_boss_damage} - {defence_stat} DEF = {final_boss_damage} damage.{RESET}")

    # --- GAME OVER CHECK ---
    if current_health <= 0:
        print(f"\n{RED}--- YOU FAINTED! ---{RESET}")
        if gold_coins > 0:
            gold_lost = max(1, int(gold_coins * 0.05))
            gold_coins -= gold_lost
            print(f" The revival clinic charged you a {RED}5% gold fee{RESET}.")
            print(f" Lost {YELLOW}{gold_lost} Gold Coins{RESET}. Remaining balance: {gold_coins}")
        else:
            xp_lost = random.randint(10, 20)
            xp = max(0, xp - xp_lost)
            print(f" You have 0 Gold! The revival machine drained your memories instead...")
            print(f" Lost {RED}{xp_lost} XP{RESET}. Remaining XP: {xp}/{xp_needed}")
        current_health, current_mana = max_health, max_mana
        current_enemy = spawn_enemy()
        current_enemy['hp'] = current_enemy['max_hp']
        continue

    # --- VICTORY CHECK ---
    if current_enemy['hp'] <= 0:
        print(f"\n{GREEN} You defeated {current_enemy['name']}!{RESET}")
        current_wave += 1

        earned_xp = random.randint(40, 70)
        earned_gold = random.randint(15, 30)
        xp += earned_xp
        gold_coins += earned_gold
        print(f" Gained {GREEN}{earned_xp} XP{RESET} and {YELLOW} {earned_gold} Gold Coins{RESET}!")
        
        # Boss gate
        if player_level >= 4 and current_wave >= 10:
            print(f"\n{RED} WARNING: WAVE 10 BOSS ENCOUNTER! ⚠️⚡{RESET}")
            print(f"{RED}THE GROUND TREMORS AS THE SKY SPLITS OPEN...{RESET}")
            current_enemy = elder_dragon_boss.copy()
            print(f"The legendary {RED}{current_enemy['name']}{RESET} has arrived to end your run!")
            time.sleep(2)

        else:
            current_enemy = spawn_enemy()
            print(f" A wild {MAGENTA}{current_enemy['name']}{RESET} appeared!")

        if current_wave >= 10:
            current_wave = 1
        # Loot drop
        luck_roll = random.randint(1, 100) + luck_stat
        item_found = False
        for reward in loot_table:
            if luck_roll >= reward["roll_needed"]:
                print(f"{GREEN}LOOT DROP!{RESET} Found a [{reward['rarity']}] {YELLOW}{reward['name']}{RESET}!")
                inventory.append(reward["name"])
                item_found = True
                break
        if not item_found:
            print(f"Loot drop: Found a {BLUE}Common Potion{RESET}!")
            inventory.append("Common Potion")

        # Level up check
        if xp >= xp_needed:
            player_level += 1
            xp -= xp_needed
            xp_needed = int(100 * (1.25 ** (player_level - 1)))
            print(f"\n{GREEN} LEVEL UP! You are now Level {player_level}!{RESET}")
            print(f"Next level requires {GREEN}{xp_needed} XP{RESET}!")
            print("Choose upgrade: 1 = HP (+20) | 2 = MP (+20) | 3 = DMG (+5) | 4 = LUCK (+5) | 5 = DEF (+5)")
            sc = input("Enter choice: ")
            if sc == "1": max_health += 20; current_health = max_health
            elif sc == "2": max_mana += 20; current_mana = max_mana
            elif sc == "3": base_damage += 5
            elif sc == "4": luck_stat += 5
            elif sc == "5": defence_stat += 5
            current_enemy = spawn_enemy()
            continue
            