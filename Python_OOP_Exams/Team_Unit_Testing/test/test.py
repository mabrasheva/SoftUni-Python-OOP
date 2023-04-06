from unittest import TestCase, main

from project.team import Team


class TeamTests(TestCase):
    NAME = "TestName"

    def setUp(self) -> None:
        self.team = Team(self.NAME)

    def test_init(self):
        self.assertEqual(self.NAME, self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_containing_not_only_letters_raises(self):
        with self.assertRaises(ValueError) as error:
            Team("Name123")
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            Team("!@#")
        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member_successfully(self):
        members_to_add = {"Member1": 18, "Member2": 19}
        more_members_to_add = {"Member3": 20}

        self.assertEqual({}, self.team.members)

        self.assertEqual("Successfully added: Member1, Member2", self.team.add_member(**members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)
        self.assertEqual(18, self.team.members["Member1"])
        self.assertEqual(19, self.team.members["Member2"])

        self.assertEqual("Successfully added: Member3", self.team.add_member(**more_members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19, "Member3": 20}, self.team.members)

    def test_add_member_existing_member_not_added_twice(self):
        members_to_add = {"Member1": 18, "Member2": 19}

        self.assertEqual({}, self.team.members)

        self.assertEqual("Successfully added: Member1, Member2", self.team.add_member(**members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)

        self.assertEqual("Successfully added: ", self.team.add_member(**members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)

    def test_remove_member_successfully(self):
        members_to_add = {"Member1": 18, "Member2": 19}

        self.assertEqual({}, self.team.members)

        self.assertEqual("Successfully added: Member1, Member2", self.team.add_member(**members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)

        self.assertEqual("Member Member1 removed", self.team.remove_member("Member1"))
        self.assertEqual({"Member2": 19}, self.team.members)

    def test_remove_not_existing_member_raises(self):
        members_to_add = {"Member1": 18, "Member2": 19}
        self.assertEqual({}, self.team.members)

        self.assertEqual("Successfully added: Member1, Member2", self.team.add_member(**members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)

        self.assertEqual("Member with name Member3 does not exist", self.team.remove_member("Member3"))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)

    def test_gt(self):
        members_to_add = {"Member1": 18, "Member2": 19}
        self.assertEqual({}, self.team.members)
        self.assertEqual("Successfully added: Member1, Member2", self.team.add_member(**members_to_add))
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)

        self.team2 = Team("OtherTestName")
        self.assertEqual(True, self.team > self.team2)
        self.assertTrue(self.team.__gt__(self.team2))
        self.assertFalse(self.team2.__gt__(self.team))

    def test_len(self):
        members_to_add = {"Member1": 18, "Member2": 19}
        self.team.add_member(**members_to_add)
        self.assertEqual({"Member1": 18, "Member2": 19}, self.team.members)
        self.assertEqual(2, self.team.__len__())

    def test_add_method(self):
        self.team2 = Team("OtherTestName")
        members_to_add = {"Member1": 18, "Member2": 19}
        other_members_to_add = {"Member3": 20}
        self.team.add_member(**members_to_add)
        self.team2.add_member(**other_members_to_add)

        self.new_team = self.team.__add__(self.team2)
        expected = self.new_team
        self.assertEqual(expected,self.new_team)

        self.assertEqual(self.NAME + self.team2.name, self.new_team.name)
        self.assertEqual({"Member1": 18, "Member2": 19, "Member3": 20}, self.new_team.members)
        self.assertEqual(3, self.new_team.__len__())

    def test_str_method(self):
        members_to_add = {"Member1": 18, "Member2": 19}
        self.team.add_member(**members_to_add)
        expected_result = [f"Team name: {self.NAME}"]
        members = list(sorted(self.team.members.items(), key=lambda x: (-x[1], x[0])))
        expected_result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        expected_result = "\n".join(expected_result)
        self.assertEqual(expected_result, self.team.__str__())


if __name__ == "__main__":
    main()
