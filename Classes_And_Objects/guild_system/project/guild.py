from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.guild_name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.guild_name
            return f"Welcome player {player.player_name} to the guild {self.guild_name}"
        if player.guild == self.guild_name:
            return f"Player {player.player_name} is already in the guild."
        return f"Player {player.player_name} is in another guild."

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.player_name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.guild_name}"]
        for player in self.players:
            result.append(player.player_info())
        return "\n".join(result)
