from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICES_TYPES = ["MainService", "SecondaryService"]
    VALID_ROBOTS_TYPES = ["MaleRobot", "FemaleRobot"]

    def __init__(self):
        self.robots = []  # will contain all robots (objects) that are created
        self.services = []  # will contain all services (objects) that are created

    @staticmethod
    def __find_object_in_collection_by_property_name(property_name, collection):
        for obj in collection:
            if obj.name == property_name:
                return obj

    @staticmethod
    def __is_suitable_service(robot, service):
        if (isinstance(robot, FemaleRobot) and isinstance(service, SecondaryService)) or \
                (isinstance(robot, MaleRobot) and isinstance(service, MainService)):
            return True
        else:
            return False

    def add_service(self, service_type: str, name: str):
        # The method creates a service of the given type and adds it to the services' collection.
        if service_type not in self.VALID_SERVICES_TYPES:
            raise Exception("Invalid service type!")
        if service_type == "MainService":
            self.services.append(MainService(name))
        elif service_type == "SecondaryService":
            self.services.append(SecondaryService(name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        # The method creates a robot of the given type and adds it to the robots' collection.
        if robot_type not in self.VALID_ROBOTS_TYPES:
            raise Exception("Invalid robot type!")
        if robot_type == "MaleRobot":
            self.robots.append(MaleRobot(name, kind, price))
        elif robot_type == "FemaleRobot":
            self.robots.append(FemaleRobot(name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        # The method adds the robot with the given name to the service if there is a capacity for that.
        # Both robot and service with the given names will always exist.
        robot = self.__find_object_in_collection_by_property_name(robot_name, self.robots)
        service = self.__find_object_in_collection_by_property_name(service_name, self.services)

        # if not (isinstance(robot, FemaleRobot) and isinstance(service, SecondaryService)) or \
        #         not (isinstance(robot, MaleRobot) and isinstance(service, MainService)):
        if not self.__is_suitable_service(robot, service):
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        # The method removes the robot with the given name from the service.
        service = self.__find_object_in_collection_by_property_name(service_name, self.services)
        robot = self.__find_object_in_collection_by_property_name(robot_name, service.robots)

        if robot not in service.robots:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        # The method feeds all robots from the service.
        service = self.__find_object_in_collection_by_property_name(service_name, self.services)

        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        # The method calculates the price of all robots that are in the service.
        service = self.__find_object_in_collection_by_property_name(service_name, self.services)

        total_price = 0
        for robot in service.robots:
            total_price += robot.price
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        # Returns information about each service.
        result = []
        for service in self.services:
            result.append(service.details())
        return "\n".join(result)
