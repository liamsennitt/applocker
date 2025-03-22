import sys
import uuid

from xml.etree.ElementTree import Element
from applocker.conditions import (
    FilePublisherCondition,
    FilePathCondition,
    FileHashCondition,
)


class _Rule(Element):
    def __init__(
        self, *, id=None, name, description="", user_or_group_sid, action, conditions=[]
    ):
        super(_Rule, self).__init__(self.__class__.__name__)
        self.id = id
        self.name = name
        self.description = description
        self.user_or_group_sid = user_or_group_sid
        self.action = action
        self.conditions = conditions

    @property
    def id(self):
        return self.get("Id")

    @id.setter
    def id(self, id):
        if id is None:
            self.set("Id", str(uuid.uuid4()))
        elif isinstance(id, str):
            self.set("Id", id)
        else:
            raise TypeError(f"invalid type for id: {type(id)}")

    @property
    def name(self):
        return self.get("Name")

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.set("Name", name)
        else:
            raise TypeError(f"invalid type for name: {type(name)}")

    @property
    def description(self):
        return self.get("Description")

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self.set("Description", description)
        else:
            raise TypeError(f"invalid type for description: {type(description)}")

    @property
    def user_or_group_sid(self):
        return self.get("UserOrGroupSid")

    @user_or_group_sid.setter
    def user_or_group_sid(self, user_or_group_sid):
        if isinstance(user_or_group_sid, str):
            self.set("UserOrGroupSid", user_or_group_sid)
        else:
            raise TypeError(
                f"invalid type for user_or_group_sid: {type(user_or_group_sid)}"
            )

    @property
    def action(self):
        return self.get("Action")

    @action.setter
    def action(self, action):
        if isinstance(action, str):
            self.set("Action", action)
        else:
            raise TypeError(f"invalid type for action: {type(action)}")

    class _Conditions(Element):
        def __init__(self):
            super(_Rule._Conditions, self).__init__("Conditions")

    @property
    def conditions(self):
        return list(self.find("Conditions"))

    @conditions.setter
    def conditions(self, conditions):
        if isinstance(conditions, list):
            new_conditions = self._Conditions()

            for condition in conditions:
                if isinstance(
                    condition,
                    (FilePublisherCondition, FilePathCondition, FileHashCondition),
                ):
                    new_conditions.append(condition)
                elif isinstance(condition, Element):
                    new_conditions.append(
                        getattr(sys.modules[__name__], condition.tag).from_element(
                            condition
                        )
                    )
                else:
                    raise TypeError(
                        f"invalid type for conditions element: {type(condition)}"
                    )

            self.append(new_conditions)
        else:
            raise TypeError(f"invalid type for conditions: {type(conditions)}")

    @classmethod
    def from_element(cls, element):
        return cls(
            id=element.get("Id"),
            name=element.get("Name"),
            description=element.get("Description"),
            user_or_group_sid=element.get("UserOrGroupSid"),
            action=element.get("Action"),
            conditions=list(element.find("Conditions")),
        )


class FilePublisherRule(_Rule):
    pass


class FilePathRule(_Rule):
    pass


class FileHashRule(_Rule):
    pass


class RuleCollection(Element):
    def __init__(self, *, type, enforcement_mode, rules=[]):
        super(RuleCollection, self).__init__("RuleCollection")
        self.type = type
        self.enforcement_mode = enforcement_mode
        self.rules = rules

    @property
    def type(self):
        return self.get("Type")

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self.set("Type", type)
        else:
            raise TypeError(f"invalid type for type: {type(type)}")

    @property
    def enforcement_mode(self):
        return self.get("EnforcementMode")

    @enforcement_mode.setter
    def enforcement_mode(self, enforcement_mode):
        if isinstance(enforcement_mode, str):
            self.set("EnforcementMode", enforcement_mode)
        else:
            raise TypeError(
                f"invalid type for enforcement_mode: {type(enforcement_mode)}"
            )

    @property
    def rules(self):
        return list(self)

    @rules.setter
    def rules(self, rules):
        if isinstance(rules, list):
            for rule in rules:
                if isinstance(rule, (FilePublisherRule, FilePathRule, FileHashRule)):
                    self.append(rule)
                elif isinstance(rule, Element):
                    self.append(
                        getattr(sys.modules[__name__], rule.tag).from_element(rule)
                    )
                else:
                    raise TypeError(f"invalid type for rules element: {type(rule)}")
        else:
            raise TypeError(f"invalid type for rules: {type(rules)}")

    @classmethod
    def from_element(cls, element):
        return cls(
            type=element.get("Type"),
            enforcement_mode=element.get("EnforcementMode"),
            rules=list(element),
        )
