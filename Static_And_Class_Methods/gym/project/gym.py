from project.subscription import Subscription
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.trainer import Trainer
from project.customer import Customer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        customer = self.__get_object_by_id(self.customers,subscription.customer_id)
        trainer = self.__get_object_by_id(self.trainers,subscription.trainer_id)
        plan = self.__get_object_by_id(self.plans,subscription.exercise_id)
        equipment = self.__get_object_by_id(self.equipment,plan.equipment_id)

        result = [subscription.__repr__(),
                  customer.__repr__(),
                  trainer.__repr__(),
                  equipment.__repr__(),
                  plan.__repr__()]
        # print(result)
        return "\n".join(result)

    def __get_object_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity
