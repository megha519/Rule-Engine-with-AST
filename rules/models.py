

from django.db import models

class Node(models.Model):
    # Type of node: operator or operand
    node_type = models.CharField(max_length=50)  # "operator" or "operand"
    
    # For operand nodes: value like 'age > 30', 'income < 50000', etc.
    value = models.CharField(max_length=255, null=True, blank=True)  
    
    # For operator nodes: left and right children
    left = models.ForeignKey('self', related_name='left_child', on_delete=models.CASCADE, null=True, blank=True)
    right = models.ForeignKey('self', related_name='right_child', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Node(type={self.node_type}, value={self.value})"
