# Rule Engine with AST

## Overview
The **Rule Engine with AST** is a 3-tier application designed to determine user eligibility based on various attributes such as age, department, income, and experience. It employs an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, and evaluation of these rules.

## Features
- **Dynamic Rule Creation**: Create rules using a simple string format.
- **AST Representation**: Utilizes an AST to manage rules efficiently.
- **Rule Evaluation**: Evaluate user eligibility based on defined rules and user attributes.
- **API Support**: Exposes APIs for rule creation and evaluation.

## Data Structure
The application uses the following data structure to represent the AST:

```python
class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Reference to left child Node
        self.right = right  # Reference to right child Node (if operator)
        self.value = value  # Optional value for operand nodes
Sample Rules
Rule 1:
plaintext
Copy code
((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
Rule 2:
plaintext
Copy code
((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)
API Design
create_rule(rule_string): Takes a rule string and returns a Node object representing the AST.
combine_rules(rules): Combines multiple rule strings into a single AST.
evaluate_rule(data): Evaluates the combined rule's AST against user attributes provided in JSON format.```
Installation
To set up the project, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/rule_engine_project.git
cd rule_engine_project
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Activate the Pipenv shell:

bash
Copy code
pipenv shell
Usage
To run the application, execute the following command:

bash
Copy code
python manage.py runserver
Access the application at http://localhost:8000.

Test Cases
Create individual rules and verify their AST representation.
Combine example rules and ensure the resulting AST reflects the combined logic.
Implement sample JSON data and test the rule evaluation.
Bonus Features
Error handling for invalid rule strings.
Validation for attributes to ensure they are part of a defined catalog.
Modifications of existing rules with functionality for adding/removing expressions.
Support for user-defined functions within the rule language.
Testing
The API endpoints were tested using Postman, allowing for easy verification of the functionality and correctness of the API responses. Sample requests and responses can be provided upon request for further clarity.

