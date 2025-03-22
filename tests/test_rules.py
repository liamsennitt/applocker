from unittest import TestCase
from applocker.conditions import FilePathCondition
from applocker.rules import _Rule, FilePathRule, RuleCollection


class TestRule(TestCase):
    def test_default_id(self):
        rule = _Rule(name="", user_or_group_sid="", action="")
        self.assertIsNotNone(rule.id)

    def test_valid_id(self):
        rule = _Rule(id="", name="", user_or_group_sid="", action="")
        self.assertEqual(rule.id, "")

    def test_invalid_id_type(self):
        with self.assertRaises(TypeError):
            _Rule(id=False, name="", user_or_group_sid="", action="")

    def test_valid_name(self):
        rule = _Rule(name="", user_or_group_sid="", action="")
        self.assertEqual(rule.name, "")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            _Rule(name=False, user_or_group_sid="", action="")

    def test_valid_description(self):
        rule = _Rule(name="", description="", user_or_group_sid="", action="")
        self.assertEqual(rule.description, "")

    def test_invalid_description_type(self):
        with self.assertRaises(TypeError):
            _Rule(name="", description=False, user_or_group_sid="", action="")

    def test_valid_user_or_group_sid(self):
        rule = _Rule(name="", user_or_group_sid="", action="")
        self.assertEqual(rule.user_or_group_sid, "")

    def test_invalid_user_or_group_sid_type(self):
        with self.assertRaises(TypeError):
            _Rule(name="", user_or_group_sid=False, action="")

    def test_valid_action(self):
        rule = _Rule(name="", user_or_group_sid="", action="")
        self.assertEqual(rule.action, "")

    def test_invalid_action_type(self):
        with self.assertRaises(TypeError):
            _Rule(name="", user_or_group_sid="", action=False)

    def test_default_conditions(self):
        rule = _Rule(name="", user_or_group_sid="", action="")
        self.assertEqual(rule.conditions, [])

    def test_valid_conditions(self):
        rule = _Rule(name="", user_or_group_sid="", action="", conditions=[])
        self.assertEqual(rule.conditions, [])

    def test_invalid_conditions_type(self):
        with self.assertRaises(TypeError):
            _Rule(name="", user_or_group_sid="", action="", conditions=False)

    def test_valid_conditions_element(self):
        condition = FilePathCondition()
        rule = _Rule(name="", user_or_group_sid="", action="", conditions=[condition])
        self.assertIsInstance(rule, _Rule)

    def test_invalid_conditions_element_type(self):
        with self.assertRaises(TypeError):
            _Rule(name="", user_or_group_sid="", action="", conditions=[False])


class TestRuleCollection(TestCase):
    def test_valid_type(self):
        collection = RuleCollection(type="", enforcement_mode="")
        self.assertEqual(collection.type, "")

    def test_invalid_type_type(self):
        with self.assertRaises(TypeError):
            RuleCollection(type=False, enforcement_mode="")

    def test_valid_enforcement_mode(self):
        collection = RuleCollection(type="", enforcement_mode="")
        self.assertEqual(collection.enforcement_mode, "")

    def test_invalid_enforcement_mode_type(self):
        with self.assertRaises(TypeError):
            RuleCollection(type="", enforcement_mode=False)

    def test_default_rules(self):
        collection = RuleCollection(type="", enforcement_mode="")
        self.assertEqual(collection.rules, [])

    def test_valid_rules(self):
        collection = RuleCollection(type="", enforcement_mode="", rules=[])
        self.assertEqual(collection.rules, [])

    def test_invalid_rules_type(self):
        with self.assertRaises(TypeError):
            RuleCollection(type="", enforcement_mode="", rules=False)

    def test_valid_rules_element(self):
        rule = FilePathRule(name="", user_or_group_sid="", action="")
        collection = RuleCollection(type="", enforcement_mode="", rules=[rule])
        self.assertIsInstance(collection, RuleCollection)

    def test_invalid_rules_element_type(self):
        with self.assertRaises(TypeError):
            RuleCollection(type="", enforcement_mode="", rules=[False])
