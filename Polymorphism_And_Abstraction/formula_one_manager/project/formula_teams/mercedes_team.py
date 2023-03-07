from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = {
        "Petronas": [[1, 1000000], [3, 500000]],
        "TeamViewer": [[5, 100000], [7, 50000]]
    }
    EXPENSES = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        total_earned_money = 0
        for sponsor, value in self.SPONSORS.items():
            for position, earned_money in value:
                if race_pos <= position:
                    total_earned_money += earned_money
                    break
        total_earned_money -= self.EXPENSES
        self.budget += total_earned_money
        return f"The revenue after the race is {total_earned_money}$. Current budget {self.budget}$"
