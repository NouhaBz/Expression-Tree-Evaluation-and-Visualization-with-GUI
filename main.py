import sys
from tkinter import *
from tkinter import ttk

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
class tp1:
    def __init__(self):
        self.formal = sys.stdin.readline().strip()
        self.infix = list(self.formal)
        self.stack = []
        self.postfix = []
        

    def InfixToPostfix(self, infix):
        i = 0
        while i < len(infix):
          l = infix[i]
          if l== '( ':
              self.stack.append(infix[i])
          else : 
            if l == '~':
                if i < len(infix) - 1 and infix[i + 1] == '(':
                    self.stack.append(l)
                    self.stack.append(infix[i + 1])
                    i += 1  
                else:
                    
                    if i < len(infix) - 1:
                        self.postfix.append(infix[i + 1])
                        self.postfix.append(l)
                        i += 1  
                    else:
                        
                        self.postfix.append(l)
            else:
                if l == '|' or l == '&':
                    self.stack.append(l)
                elif l == '>' or l == '#':
                    pos = self.stack.index('(') if '(' in self.stack else -1

                    if pos == -1:
                        p = self.stack.index('&') if '&' in self.stack else -1
                        pp = self.stack.index('|') if '|' in self.stack else -1

                        if p == -1 and pp == -1:
                            self.stack.append(l)
                        else:
                            self.postfix.append(self.stack.pop())
                            self.stack.append(l)
                    else:
                        for s in range(pos, len(self.stack)):
                            p = self.stack.index('>') if '>' in self.stack else -1
                            pp = self.stack.index('#') if '#' in self.stack else -1

                            if p == -1 and pp == -1:
                                self.stack.append(l)
                            else:
                                self.postfix.append(self.stack.pop())
                                self.stack.append(l)
                else:
                    if l == ')':
                        pos = self.stack.index('(') if '(' in self.stack else -1

                        if pos == -1:
                            print("the formula is wrong, there's no matching '(' ")
                        else:
                              for s in range(len(self.stack) - 1, pos - 1, -1):
                                self.postfix.append(self.stack.pop())
                              if ((pos+1)== '~'):
                                  self.postfix.append(self.stack.pop())      
                    else:
                        self.postfix.append(l)

            i += 1

        while self.stack:
            self.postfix.append(self.stack.pop())
        
        formul_postfix = ''.join(self.postfix)
        return formul_postfix
    
import tkinter as tk

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def create_tree(self, pfix):
        stack = []
        for symbol in pfix:
            if symbol.isalpha():
                char_node = TreeNode(symbol)
                stack.append(char_node)
            elif symbol == '~':
                operand_node = stack.pop()
                char_node = TreeNode(symbol)
                char_node.right = operand_node
                stack.append(char_node)
            else:
                right = stack.pop()
                left = stack.pop()
                char_node = TreeNode(symbol)
                char_node.right = right
                char_node.left = left
                stack.append(char_node)

        if stack:
         self.root = stack[-1]
        self.print_tree()

    def print_tree(self):
        self.window = tk.Tk()
        self.window.title("Expression Tree Visualization")
        self.canvas = tk.Canvas(self.window, width=800, height=400)
        self.canvas.pack()
        self._draw_tree(self.root, 400, 50, 200)
        self.window.mainloop()

    def _draw_tree(self, node, x, y, spacing):
        if node:
           self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="white")
           self.canvas.create_text(x, y, text=str(node.data))
           if node.left:
                x_left = x - spacing
                y_left = y + 50
                self._draw_tree(node.left, x_left, y_left, spacing / 2)
                self.canvas.create_line(x - 20, y, x_left + 20, y_left - 20, width=2)
           if node.right:
                x_right = x + spacing
                y_right = y + 50
                self._draw_tree(node.right, x_right, y_right, spacing / 2)
                self.canvas.create_line(x + 20, y, x_right - 20, y_right - 20, width=2)
    

# Example usage:
my_instance = tp1()
pfix = my_instance.InfixToPostfix(my_instance.infix)
print(pfix)
tree_instance = ExpressionTree()
tree_instance.create_tree(list(pfix))
