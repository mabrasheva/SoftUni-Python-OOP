class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.player_name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.player_name}"
        return "Skill already added"

    def player_info(self):
        result = [f"Name: {self.player_name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for skill_name, skill_mana_cost in self.skills.items():
            result.append(f"==={skill_name} - {skill_mana_cost}")
        return "\n".join(result)
