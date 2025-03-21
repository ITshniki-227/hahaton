import random


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
#Инициализирует имя урон, дамаг оружия

class Character:
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
# Инициализирует имя урон, здоровье, ману  игрока

    def ia(self):
        return self.health > 0

    def at(self, other, weapon):
        damage = weapon.damage + random.randint(0, 5)  # Урон с небольшим рандомом
        other.health -= damage
        print(f"{self.name} атакует {other.name} с помощью {weapon.name} нанося {damage} урона.")


class Player(Character):
    def __init__(self, name, health, mana, weapon):
        super().__init__(name, health, mana)
        self.weapon = weapon

    def sa(self, other):
        if self.mana >= 5:
            damage = random.randint(15, 25)
            other.health -= damage
            self.mana -= 5
            print(f"{self.name} использует специальную атаку на {other.name} нанося {damage} урона.")
        else:
            print(f"{self.name} нехватает маны.")


class Opponent(Character):
    def sa(self, other):
        if self.mana >= 3:
            damage = random.randint(10, 20)
            other.health -= damage
            self.mana -= 3
            print(f"{self.name} использует специальную атаку на {other.name} нанося {damage} урона.")
        else:
            print(f"{self.name} нехватает маны.")


def bat(player, opponent):
    while player.ia() and opponent.ia():
        print(f"\n{player.name}: Здоровье: {player.health}, Мана: {player.mana}, Оружие: {player.weapon.name}")
        print(f"{opponent.name}: Здоровье: {opponent.health}, Мана: {opponent.mana}")

        action = input("Выберите действие (атака/специальная атака): ").strip().lower()

        if action == "атака":
            player.at(opponent, player.weapon)
        elif action == "специальная атака":
            player.sa(opponent)
        else:
            print("Неверное действие. Попробуйте снова.")
            continue

        if opponent.ia():
            opponent.at(player, Weapon("Удар", random.randint(5, 10)))  # Простой удар противника
        else:
            opponent.sa(player)

    if player.ia():
        print(f"{player.name} победил!")
    else:
        print(f"{opponent.name} победил!")


def main():
    # Определение доступного оружия
    sword = Weapon("Меч", 10)
    axe = Weapon("Лук", 8)

    print("Выберите оружие:")
    print("1. Меч")
    print("2. Лук")
    choice = input("Введите номер оружия: ").strip()

    if choice == "1":
        player_weapon = sword
    elif choice == "2":
        player_weapon = axe
    else:
        print("Неверный выбор. Попробуйте снова.")

    player = Player("Игрок", 100, 10, player_weapon)
    opponents = [Opponent("Горгулья", 60, 5), Opponent("Ведьма", 45, 7)]

    for opponent in opponents:
        print(f"\nСражение с {opponent.name}!")
        bat(player, opponent)
        if not player.ia():
            break


if __name__ == "__main__":
    main()
