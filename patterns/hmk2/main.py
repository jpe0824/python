class WeaponBehavior:
    def use_weapon(self, weapon: str) -> None:
        print(weapon)

class Character:
    def __init__(self):
        self.weapon_behavior = None

    def fight(self) -> None:
        # Abstract method
        pass

    def set_weapon_behavior(self, weapon_behavior: WeaponBehavior) -> None:
        self.weapon_behavior = weapon_behavior

class King(Character):
    def fight(self) -> None:
        print("King is fighting")
        self.weapon_behavior.use_weapon()

class Queen(Character):
    def fight(self) -> None:
        print("Queen is fighting")
        self.weapon_behavior.use_weapon()

class Knight(Character):
    def fight(self) -> None:
        print("Knight is fighting")
        self.weapon_behavior.use_weapon()

class Troll(Character):
    def fight(self) -> None:
        print("Troll is fighting")
        self.weapon_behavior.use_weapon()

class SwordBehavior(WeaponBehavior):
    def use_weapon(self) -> WeaponBehavior:
        return super().use_weapon("Swinging a sword")

class AxeBehavior(WeaponBehavior):
    def use_weapon(self) -> WeaponBehavior:
        return super().use_weapon("Chopping with an axe")

class KnifeBehavior(WeaponBehavior):
    def use_weapon(self) -> WeaponBehavior:
        return super().use_weapon("Cutting with a knife")

class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self) -> WeaponBehavior:
        return super().use_weapon("Shooting an arrow with a bow")

if __name__ == "__main__":
    king = King()
    king.set_weapon_behavior(SwordBehavior())
    king.fight()

    queen = Queen()
    queen.set_weapon_behavior(AxeBehavior())
    queen.fight()

    knight = Knight()
    knight.set_weapon_behavior(KnifeBehavior())
    knight.fight()

    troll = Troll()
    troll.set_weapon_behavior(BowAndArrowBehavior())
    troll.fight()