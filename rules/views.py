from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Node
from django.shortcuts import render

# Helper function to create AST from rule string
def create_rule(rule_string):
    # Example: rule_string = "age > 30 AND income < 50000 OR department = 'Sales'"
    # Supported operators: AND, OR
    operators = ["AND", "OR"]
    
    # Handle compound rules with AND, OR
    for operator in operators:
        if operator in rule_string:
            parts = rule_string.split(operator)  # Split rule into parts
            left_operand = parts[0].strip()  # Example: "age > 30"
            right_operand = parts[1].strip()  # Example: "income < 50000"

            # Create the left and right operand nodes
            left = Node.objects.create(node_type="operand", value=left_operand)
            right = Node.objects.create(node_type="operand", value=right_operand)

            # Create the operator node (AND/OR)
            operator_node = Node.objects.create(node_type="operator", left=left, right=right, value=operator)
            return operator_node

    # Handle simple rules without AND/OR
    return Node.objects.create(node_type="operand", value=rule_string)

# Function to traverse and represent AST
def traverse_ast(node):
    if node.node_type == "operator":
        left_ast = traverse_ast(node.left)
        right_ast = traverse_ast(node.right)
        return f"({left_ast} {node.value} {right_ast})"
    return node.value  # Return operand value

# API to create a rule and return its AST
@csrf_exempt
def create_rule_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        rule_string = data.get("rule")
        if rule_string:
            ast_root = create_rule(rule_string)  # Create AST
            if ast_root:
                ast_representation = traverse_ast(ast_root)  # Get full AST string
                return JsonResponse({
                    "status": "success",
                    "ast": ast_representation,
                    "rule_id": ast_root.id  # Include rule ID in the response
                }, status=200)
            return JsonResponse({"status": "error", "message": "Failed to generate AST"}, status=400)
        return JsonResponse({"status": "error", "message": "Invalid rule string"}, status=400)

# Function to evaluate the AST based on user data
# Function to evaluate the AST based on user data (example: "age > 30")
def evaluate_ast(ast_node, user_data):
    if ast_node.node_type == "operand":
        # Extract the key, operator, and value from the operand string
        operand = ast_node.value.split()
        key = operand[0]  # e.g., "age"
        operator = operand[1]  # e.g., ">"
        comparison_value = int(operand[2])  # e.g., 30 (convert to integer)
        
        # Get the actual value from user_data for the key
        actual_value = user_data.get(key, 0)

        # Perform comparison based on the operator
        if operator == ">":
            return actual_value > comparison_value
        elif operator == "<":
            return actual_value < comparison_value
        elif operator == ">=":
            return actual_value >= comparison_value
        elif operator == "<=":
            return actual_value <= comparison_value
        elif operator == "==":
            return actual_value == comparison_value
        elif operator == "!=":
            return actual_value != comparison_value
        return False
    elif ast_node.node_type == "operator":
        left_result = evaluate_ast(ast_node.left, user_data)
        right_result = evaluate_ast(ast_node.right, user_data)

        # Evaluate "AND" operator
        if ast_node.value == "AND":
            return left_result and right_result
        # You can add more operators like "OR" here
    return False

@csrf_exempt
def evaluate_rule(request):
    if request.method == "POST":
        data = json.loads(request.body)
        rule_id = data.get("rule_id")
        user_data_list = data.get("user_data", [])

        # Retrieve the rule (AST) from the database using the rule_id
        rule_ast = Node.objects.get(id=rule_id)

        # Store results for each user data entry
        results = []

        for user_data in user_data_list:
            result = evaluate_ast(rule_ast, user_data)
            results.append({
                "user_data": user_data,
                "result": result
            })

        return JsonResponse({"status": "success", "results": results}, status=200)

# Render index page
def index(request):
    return render(request, "rules/index.html")
