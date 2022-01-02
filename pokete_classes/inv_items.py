"""All classes needed for Item management"""


class Items:
    """Has all items as attributes
    ARGS:
        p_d: p_data module"""

    def __init__(self, p_d):
        for item in p_d.items.items():
            _obj = InvItem(item[0], item[1]["pretty_name"],
                           item[1]["desc"],
                           item[1]["price"], item[1]["fn"])
            setattr(self, item[0], _obj)
        self.ld_bubble_bomb = LearnDisc("bubble_bomb", p_d.attacks)
        self.ld_flying = LearnDisc("flying", p_d.attacks)


class InvItem:
    """Item for the inventory
    ARGS:
        name: The item's generic name (healing_potion)
        pretty_name: The item's pretty name (Healing potion)
        desc: The item's description
        price: The item's price in the shop
        fn: The associated method name in FightItems"""

    def __init__(self, name, pretty_name, desc, price, fn=None):
        self.name = name
        self.pretty_name = pretty_name
        self.desc = desc
        self.price = price
        self.fn = fn


class LearnDisc(InvItem):
    """Learning disc item to teach attacks to Poketes
    ARGS:
        attack_name: The name of the attack being taught
        attacks: p_data.attacks dict"""

    def __init__(self, attack_name, attacks):
        self.attack_name = attack_name
        self.attack_dict = attacks[attack_name]
        pretty_name = f"LD-{self.attack_dict['name']}"
        name = f"ld_{attack_name}"
        desc = f"Teaches a Pokete the attack '{self.attack_dict['name']}'."
        super().__init__(name, pretty_name, desc, 0)


if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
