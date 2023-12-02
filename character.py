from __future__ import annotations
print("\n")

from dice import Dice

from rich import print

class MessageManager():
    pass



class Character:
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice

    def __str__(self):
        return f"""{self._name} the Character enter the arena with :
    ■ attack: {self._attack_value} 
    ■ defense: {self._defense_value}"""
        
    def get_defense_value(self):
        return self._defense_value
        
    def get_name(self):
        return self._name
        
    def is_alive(self):
        return self._current_hp > 0       

    def show_healthbar(self):
        missing_hp = self._max_hp - self._current_hp
        healthbar = f"[{"♥" * self._current_hp}{"♡" * missing_hp}] {self._current_hp}/{self._max_hp}hp"
        print(healthbar)

    # Dans la classe Character
    def decrease_health(self, amount):
        if amount > 0:
            self._current_hp -= amount
            if self._current_hp < 0:
                self._current_hp = 0
        self.show_healthbar()

        
    def compute_damages(self, roll, target):
        return self._attack_value + roll
        
    def attack(self, target: Character):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        print(f"⚔️ {self._name} attack {target.get_name()} with {damages} damages (attack: {self._attack_value} + roll: {roll})")
        target.defense(damages, self)
    
    def compute_defense(self, damages, roll, attacker):
        return damages - self._defense_value - roll
    
    def defense(self, damages, attacker: Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} (damages: {damages} - defense: {self._defense_value} - roll: {roll})")
        self.decrease_health(wounds)
    
    def is_ready_for_boss_fight(self):
        return self._current_hp > 0 and self._max_hp - self._current_hp < self._max_hp // 2

    

class Warrior(Character):
    def compute_damages(self, roll, target: Character):
        print("🪓 Bonus: Axe in your face (+3 attack)")
        return super().compute_damages(roll, target) + 3 

class Mage(Character):
    def compute_defense(self, damages, roll, attacker: Character):
        print("🧙 Bonus: Magic armor (-3 damages)")
        result = super().compute_defense(damages, roll, attacker) - 3
        return max(result, 0)

class Thief(Character):
    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneacky attack (+{target.get_defense_value()} damages)")
        return super().compute_damages(roll, target) + target.get_defense_value()

class Enemy(Character):
    def compute_damages(self, roll, target: Character):
        print(f"👾 Bonus:Malveillance Max (+1 damages)")
        return super().compute_damages(roll, target) + 1
    
    def compute_defense(self, damages, roll, attacker: Character):
        print(f"👾 Bonus:Malveillance Max (+1 defense)")
        return super().compute_defense(damages, roll, attacker) + 1

class Boss(Character):
    def __init__(self, name, health, attack, defense, dice):
        super().__init__(name, health, attack, defense, dice)

    def special_attack(self, target: Character):
        print(f"{self._name} unleashes a devastating special attack!")
        damage = self.compute_special_damages(target)
        target.receive_damage(damage)

    def boss_special_attack(self, target):
        print(f"{self.name} uses a powerful boss special attack!")
        damage = 2 * (self.attack + self.dice.roll())  # Example: Double damage for the special attack
        target.receive_damage(damage)
        print(f"{target.name} takes {damage} damage from the boss special attack!")
        
    def use_potion(self, potion: Potion):
        remaining_health = self.max_hp - self._current_hp
        actual_healing = min(potion.healing_power, remaining_health)
        
        if actual_healing > 0:
            print(f"🧪 {self._name} uses {potion.get_name()} and restores {actual_healing} health!")
            self.restore_health(actual_healing)
        else:
            print(f"🧪 {self._name} uses {potion.get_name()} but it has no effect!")
        
class Potion:
    def __init__(self, name, healing_power):
        self.name = name
        self.healing_power = healing_power
        
    def __str__(self):
        return self
    
    def apply(self, target: Character):
        if isinstance(target, Character):
            print(f"🧪 {target.get_name()} uses {self._name} and restores {self._healing_power} health!")
            target.restore_health(self._healing_power)
        else:
            print("Invalid target for potion!")
             