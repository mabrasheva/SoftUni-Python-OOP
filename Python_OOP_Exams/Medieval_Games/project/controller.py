from project.player import Player


#                 break
#
#         if found:
#             self.supplies.pop(index)
#
#         return found
#
#     def add_player(self, *players):
#
#         added_players = []
#
#         for player in players:
#             if player not in self.players:
#                 self.players.append(player)
#                 added_players.append(player.name)
#
#         return f'Successfully added: {", ".join(added_players)}'
#
#     def add_supply(self, *supplies):
#
#         for supply in supplies:
#             self.supplies.append(supply)
#
#     def sustain(self, player_name: str, sustenance_type: str):
#
#         player = next(filter(lambda x: x.name == player_name, self.players), None)
#
#         if not player.need_sustenance:
#             return f"{player_name} have enough stamina."
#
#         if sustenance_type in ["Food", "Drink"]:
#
#             sustenance = self.find_sustenance(sustenance_type)
#
#             if not sustenance:
#                 raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
#
#             player.stamina = 100 if player.stamina + sustenance.energy > 100 else player.stamina + sustenance.energy
class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]

    def __init__(self):
        self.players: list = []  # will contain all the players (objects)
        self.supplies: list = []  # will contain all the supplies (objects)

    def __find_player_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def add_player(self, *args):
        successfully_added_players = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                successfully_added_players.append(player.name)
        return f"Successfully added: {', '.join(successfully_added_players)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)

        if not player:
            return

        if sustenance_type not in self.VALID_SUSTENANCE_TYPES:
            return

        if player.stamina == player.MAX_STAMINA:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                supply = self.supplies.pop(i)

                if player.stamina + supply.energy > Player.MAX_STAMINA:
                    player.stamina = Player.MAX_STAMINA
                else:
                    player.stamina += supply.energy

                return f"{player_name} sustained successfully with {supply.name}."
        raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):

        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        stamina_result = []
        for player in [first_player, second_player]:
            if player.stamina == 0:
                stamina_result.append(f"Player {player.name} does not have enough stamina.")

        if stamina_result:
            return "\n".join(stamina_result)

        if first_player.stamina > second_player.stamina:
            first_player, second_player = second_player, first_player

        if second_player.stamina - (first_player.stamina / 2) <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"
        else:
            second_player.stamina -= first_player.stamina / 2

        if first_player.stamina - (second_player.stamina / 2) <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"
        else:
            first_player.stamina -= second_player.stamina / 2

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(player.__str__())
        for supply in self.supplies:
            result.append(supply.details())
        return "\n".join(result)
