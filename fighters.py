class Fighter:
  """ This project resembles a 2 player game of fighters in an arena, 2 fighters step forward players input 
  their names, age and are introduced to the arena. Players then select their weapon and armor
  determining their attack and health values. """
  
  def __init__(self, name, age, health , alive = True):
    self.name = name
    self.age = age
    self.health = health
    self.alive = alive

  # players introducing themselves
  def __repr__(self):
    return "My name is {name} and i am {age} years old and i will end my foe!".format(name = self.name, age = self.age)
    
  # attack determined by elements as to whether the attack is super effective or not.
  
  def attack(self, other_fighter, weapon, armor):
    if (other_fighter.alive):
      if weapon.element_attack == "Fire" and armor.element_defence == "Earth":
        attack_damage = weapon.thrust()
      elif weapon.element_attack == "Air" and armor.element_defence == "Water":
        attack_damage = weapon.slash()
      elif weapon.element_attack == "Water" and armor.element_defence == "Fire":
        attack_damage = weapon.slash()
      elif weapon.element_attack == "Earth" and armor.element_defence == "Air":
        attack_damage = weapon.slash()
      elif weapon.element_attack == "Fire" and armor.element_defence == "Water":
        attack_damage = weapon.thrust()
      elif weapon.element_attack == "Air" and armor.element_defence == "Earth":
        attack_damage = weapon.thrust()
      elif weapon.element_attack == "Water" and armor.element_defence == "Air":
        attack_damage = weapon.thrust()
      elif weapon.element_attack == "Earth" and armor.element_defence == "Fire":
        attack_damage = weapon.thrust()
      else:
        attack_damage = weapon.damage  
      return attack_damage
      
  # Blocking determined by elements as to whether the armor is super resistant or not.
  
  def block(self, other_fighter, weapon, armor):
      if weapon.element_attack == "Fire" and armor.element_defence == "Earth":
        armor_multiplier = armor.super_effective()
      elif weapon.element_attack == "Air" and armor.element_defence == "Water":
        armor_multiplier = armor.super_effective()
      elif weapon.element_attack == "Water" and armor.element_defence == "Fire":
        armor_multiplier = armor.super_effective()
      elif weapon.element_attack == "Earth" and armor.element_defence == "Air":
        armor_multiplier = armor.super_effective()
      elif weapon.element_attack == "Fire" and armor.element_defence == "Water":
        armor_multiplier = armor.resistant()
      elif weapon.element_attack == "Air" and armor.element_defence == "Earth":
        armor_multiplier = armor.resistant()
      elif weapon.element_attack == "Water" and armor.element_defence == "Air":
        armor_multiplier = armor.resistant()
      elif weapon.element_attack == "Earth" and armor.element_defence == "Fire":
        armor_multiplier = armor.resistant()
      else:
        armor_multiplier = armor.defence
        print(armor.defence)
      return armor_multiplier
    
  # if players health = 0 player dies and other player is announced the winner
  def dead(self, other_fighter):
    if self.alive == False:
      self.health = 0
    return print(self.name + " is dead " + other_fighter.name + " is the winner!")



class Weapon:
  # actions a weapon can take
  def __init__(self, name, damage, element_attack):
    self.name = name
    self.damage = damage
    self.element_attack = element_attack
    self.is_broken = False
    
  #damage doubled if super effective
  def slash(self):
    return self.damage * 2
  #damage halved if armor is resistant
  def thrust(self):
    return self.damage / 2
      
   

class Armor:
  # actions for armor
  def __init__(self, name, defence, element_defence):
    self.name = name
    self.defence = defence
    self.element_defence = element_defence
  #armor doubled if resistant
  def resistant(self):
    return self.defence * 2
  # armor halved if weapon is super effective
  def super_effective(self):
    return self.defence / 2

# Elements and armor values for armor choice
cloth_armor = Armor("Cloth", 30, "Air")
leather_armor = Armor("Leather", 40, "Water")
chain_armor = Armor("Chain", 50, "Fire")
plate_armor = Armor("Plate", 60, "Earth")

# Elements and damage values for weapon choice
mace = Weapon("Mace", 50, "Fire")
sword = Weapon("Sword", 60, "Earth")
dagger = Weapon("Dagger", 40, "Water")
spear = Weapon("Spear", 70, "Air")

#Introduction of game and player inputs for their fighters
fighter_one_name = input("Hello fighter 1 please input your name ")
fighter_one_age = input ("Please input your age ")
fighter_one = Fighter(fighter_one_name, fighter_one_age, 100, )
fighter_two_name = input("Hello fighter 2 please input your name ")
fighter_two_age = input ("Please input your age ")
fighter_two = Fighter(fighter_two_name, fighter_two_age, 100, )
print("Welcome to the arena fighters! Please introduce yourselves!")
print(fighter_one)
print(fighter_two)

#Initialising fighters health to 100
fighter_one_health = fighter_one.health
fighter_two_health = fighter_one.health


# Player 1 chooses weapon
choose_weapon = input(fighter_one.name + " please choose your weapon being either 'mace', 'sword', 'dagger' or 'spear' ")
if choose_weapon == 'mace':
  fighter_one_weapon = mace
elif choose_weapon == 'sword':
  fighter_one_weapon = sword
elif choose_weapon == 'dagger':
  fighter_one_weapon = dagger
elif choose_weapon == 'spear':
  fighter_one_weapon = spear
print("{fighter} has chosen the {weapon}".format(fighter = fighter_one.name, weapon = fighter_one_weapon.name))

# Player 1 chooses armor
choose_armor = input(fighter_one.name + " please choose your armor being either 'cloth', 'leather', 'chain' or 'plate' ")
if choose_armor == 'cloth':
  fighter_one_armor = cloth_armor
elif choose_armor == 'leather':
  fighter_one_armor = leather_armor
elif choose_armor == 'chain':
  fighter_one_armor = chain_armor
elif choose_armor == 'plate':
  fighter_one_armor = plate_armor
print("{fighter} has chosen their {armor}".format(fighter = fighter_one.name, armor = fighter_one_armor.name))

# Player 2 chooses weapon
choose_weapon = input(fighter_two.name + " please choose your weapon being either 'mace', 'sword', 'dagger' or 'spear' ")
if choose_weapon == 'mace':
  fighter_two_weapon = mace
elif choose_weapon == 'sword':
  fighter_two_weapon = sword
elif choose_weapon == 'dagger':
  fighter_two_weapon = dagger
elif choose_weapon == 'spear':
  fighter_two_weapon = spear
print("{fighter} has chosen the {weapon}".format(fighter = fighter_two.name, weapon = fighter_two_weapon.name))

# Player 2 chooses weapon
choose_armor = input(fighter_two.name + " please choose your armor being either 'cloth', 'leather', 'chain' or 'plate' ")
if choose_armor == 'cloth':
  fighter_two_armor = cloth_armor
elif choose_armor == 'leather':
  fighter_two_armor = leather_armor
elif choose_armor == 'chain':
  fighter_two_armor = chain_armor
elif choose_armor == 'plate':
  fighter_two_armor = plate_armor
print("{fighter} has chosen their {armor} armor".format(fighter = fighter_two.name, armor = fighter_two_armor.name))


# Player 1 fighter's health determined with armor value added
fighter_one_block = fighter_one.block(fighter_two, fighter_two_weapon, fighter_one_armor) 
fighter_one_health += fighter_one_block
print(fighter_one.name + " block value is " + str(fighter_one_block) +" making their total health" + str(fighter_one_health))


# Player 2 fighter's health determined with armor value added
fighter_two_block = fighter_two.block(fighter_one, fighter_one_weapon, fighter_two_armor)  
fighter_two_health += fighter_two_block
print(fighter_two.name + " block value is " + str(fighter_two_block) +" making their total health " + str(fighter_two_health))

# Loop of rounds for each fighter to take a single strike each until a fighter is dead
round_count = 1
while fighter_one_health > 0 and fighter_two_health > 0:
  print("Round: " + str(round_count) + " FIGHT!")
  print(fighter_one.name + "s turn!")
  if fighter_one_health <= 0:
    fighter_one.dead(fighter_two)
    break
  else:
    print(fighter_two.name + "s health is " + str(fighter_two_health))
    fighter_one_attack = fighter_one.attack(fighter_two, fighter_one_weapon, fighter_two_armor)
    print(fighter_one.name + " attacks for " + str(fighter_one_attack))
    fighter_two_health -= fighter_one_attack
    print(fighter_two.name + "s remaining health is " + str(fighter_two_health))
  print(fighter_two.name + "s turn!")
  if fighter_two_health <= 0:
    fighter_two.dead(fighter_one)
    break
  else:
    print(fighter_one.name + "s health is " + str(fighter_one_health))
    fighter_two_attack = fighter_two.attack(fighter_one, fighter_two_weapon, fighter_one_armor)
    print(fighter_two.name + " attacks for " + str(fighter_two_attack))
    fighter_one_health -= fighter_two_attack
    print(fighter_one.name + "s remaining health is " + str(fighter_one_health))
  round_count += 1


