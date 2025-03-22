from xml.etree.ElementTree import Element
from applocker.rules import RuleCollection


class AppLockerPolicy(Element):
    def __init__(self, *, version="1", rule_collections=[]):
        super(AppLockerPolicy, self).__init__("AppLockerPolicy")
        self.version = version
        self.rule_collections = rule_collections

    @property
    def version(self):
        return self.get("Version")

    @version.setter
    def version(self, version):
        if isinstance(version, str):
            self.set("Version", version)
        else:
            raise TypeError(f"invalid type for version: {type(version)}")

    @property
    def rule_collections(self):
        return self.findall("RuleCollection")

    @rule_collections.setter
    def rule_collections(self, rule_collections):
        if isinstance(rule_collections, list):
            for rule_collection in rule_collections:
                if isinstance(rule_collection, RuleCollection):
                    self.append(rule_collection)
                elif isinstance(rule_collection, Element):
                    self.append(RuleCollection.from_element(rule_collection))
                else:
                    raise TypeError(
                        f"invalid type for rule_collections element: {type(rule_collection)}"
                    )
        else:
            raise TypeError(
                f"invalid type for rule_collections: {type(rule_collections)}"
            )

    @classmethod
    def from_element(cls, element):
        return cls(
            version=element.get("Version"),
            rule_collections=element.findall("RuleCollection"),
        )
