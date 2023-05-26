from typing import List
import os

from tagging_module.tagging_system import TaggingSystem

class TaggingService:
    """
    A class for providing a tagging service.
    """

    package_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the package directory
    rules_path = os.path.join(package_dir, 'config', 'rules.yml')

    def __init__(self, rules_path: str = None):
        if rules_path is None:
            rules_path = TaggingService.rules_path
        if not os.path.isfile(rules_path):
            raise FileNotFoundError(f"Rules file not found: {rules_path}")
        self.rules_path = rules_path


    def assign_tags(self, content: str) -> List[str]:
        return TaggingSystem.assign_tags(content, self.rules_path)