from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        result = [f"{self.name} Secondary Service:"]
        if self.robots:
            result.append(f"Robots: {' '.join(robot.name for robot in self.robots)}")
        else:
            result.append("Robots: none")
        return "\n".join(result)
