import yaml
from typing import List

class TaggingSystem:
    """
    A class for assigning tags based on a set of rules.
    """
    def assign_tags(content: str, rules_path: str) -> List[str]:
        """
        Assigns tags based on a set of rules specified in a YAML file.

        Args:
            content (str): The content to be tagged.
            rules_path (str): The path to the YAML file containing the rules.

        Returns:
            List[str]: A list of tags assigned to the content.
        """
        if not content or not rules_path:
            raise ValueError("Invalid content or rules_path")

        try:
            # Load rules from YAML file
            with open(rules_path, 'r', encoding='utf-8') as f:
                rule_dict = yaml.safe_load(f)

            # Convert keys to sets and store lowercase content
            rule_dict = {tag: set(keys) for tag, keys in rule_dict.items()}
            content = content.lower()
            tags = []

            # Check each rule for both single and compound words
            for tag, keys in rule_dict.items():
                common_words = keys.intersection(content.split())
                if common_words:
                    tags.append(tag)
            return tags

        except Exception as e:
            raise ValueError(f"Error assigning tags: {str(e)}")
