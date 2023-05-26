# Tagging Module
A lightweight rule based tech content tagging module for Python

## Class Overview
The `TaggingService` class is designed to provide a tagging service. It uses the `tagging_system` module to assign tags to content based on predefined rules. The tagging rules are specified in a YAML file.

You may directly use it from this repo or install via Pip.
```
pip install tagging-module
```

## Constructor
### `__init__(self, rules_path: str = None)`
The constructor initializes a `TaggingService` object.

#### Parameters
- `rules_path` (optional): A string representing the path to the YAML file containing the tagging rules. If not provided, the default rules file path (`tagging_module/config/rules.yml`) is used.

#### Exceptions
- `FileNotFoundError`: Raised if the provided `rules_path` is not a valid file path.

### Example
```python
from tagging_module.tagging_service import TaggingService

# Using the default rules file path
service = TaggingService()

# Providing a custom rules file path
service = TaggingService(rules_path="path/to/custom_rules.yml")
```

## Methods
### assign_tags(self, content: str) -> List[str]
This method assigns tags to the provided content based on the defined tagging rules.

#### Parameters
- content: A string representing the content to be tagged.
#### Returns
A list of strings representing the assigned tags for the content.

### Example
```python
from tagging_module.tagging_service import TaggingService

# Assuming the rules file contains rules for tagging different types of content
service = TaggingService()

content = "This is a sample content."
tags = service.assign_tags(content)
print(tags)
# Output: ['sample', 'content']
```

Note: The output tags may vary based on the specific tagging rules defined in the rules file.