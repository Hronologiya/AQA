import unittest
from lesson_16.Lesson_16_1.employee import TeamLead


class TestTeamLeadAttributes(unittest.TestCase):

    def test_teamlead_attributes(self):
        teamlead = TeamLead("Alice", 80000, "Development", "Python", 5)

        # Перевірка атрибутів з класу Manager
        self.assertEqual(teamlead.get_name(), "Alice")
        self.assertEqual(teamlead.get_salary(), 80000)
        self.assertEqual(teamlead.get_department(), "Development")
        self.assertEqual(teamlead.get_programming_language(), "Python")
        self.assertEqual(teamlead.get_team_size(), 5)

if __name__ == "__main__":
    unittest.main()