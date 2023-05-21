from typing import List
import os

from tagging_module.tagging_module import tagging_system

class TaggingService:
    """
    A class for providing a tagging service.
    """

    rules_path = "tagging_module/config/rules.yml"

    def __init__(self, rules_path: str = None):
        if rules_path is None:
            rules_path = TaggingService.rules_path
        if not os.path.isfile(rules_path):
            raise FileNotFoundError(f"Rules file not found: {rules_path}")
        self.rules_path = rules_path


    def assign_tags(self, content: str) -> List[str]:
        return tagging_system.assign_tags(content, self.rules_path)