from unittest import TestCase
from applocker.rules import RuleCollection
from applocker.policy import AppLockerPolicy


class TestRuleCollection(TestCase):
    def test_default_version(self):
        policy = AppLockerPolicy()
        self.assertEqual(policy.version, "1")

    def test_valid_version(self):
        policy = AppLockerPolicy(version="1")
        self.assertEqual(policy.version, "1")

    def test_invalid_version_type(self):
        with self.assertRaises(TypeError):
            AppLockerPolicy(version=False)

    def test_default_rule_collections(self):
        policy = AppLockerPolicy()
        self.assertEqual(policy.rule_collections, [])

    def test_valid_rule_collections(self):
        policy = AppLockerPolicy(rule_collections=[])
        self.assertEqual(policy.rule_collections, [])

    def test_invalid_rule_collections_type(self):
        with self.assertRaises(TypeError):
            AppLockerPolicy(rule_collections=False)

    def test_valid_rule_collections_element(self):
        collection = RuleCollection(type="", enforcement_mode="")
        policy = AppLockerPolicy(rule_collections=[collection])
        self.assertIsInstance(policy, AppLockerPolicy)

    def test_invalid_rule_collections_element_type(self):
        with self.assertRaises(TypeError):
            AppLockerPolicy(rule_collections=[False])
