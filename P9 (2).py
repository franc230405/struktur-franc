#!/usr/bin/env python
# coding: utf-8

# In[ ]:


{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c0d598be",
   "metadata": {},
   "source": [
    "#   Created by Elshad Karimov on 05/06/2020.\n",
    "#   Copyright © 2020 AppMillers. All rights reserved."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a2f09b6",
   "metadata": {},
   "outputs": [],
   "source": [
    "class TreeNode:\n",
    "    def __init__(self, data, children = []):\n",
    "        self.data = data\n",
    "        self.children = children\n",
    "    \n",
    "    def __str__(self, level=0):\n",
    "        ret = \"  \" * level + str(self.data)  + \"\\n\"\n",
    "        for child in self.children:\n",
    "            ret += child.__str__(level + 1)\n",
    "        return ret\n",
    "    \n",
    "    def addChild(self, TreeNode):\n",
    "        self.children.append(TreeNode)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "06759e3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Drinks\n",
      "  Cold\n",
      "    Cola\n",
      "    Fanta\n",
      "  Hot\n",
      "    Tea\n",
      "    Coffee\n",
      "\n"
     ]
    }
   ],
   "source": [
    "tree = TreeNode('Drinks', [])\n",
    "cold = TreeNode('Cold', [])\n",
    "hot = TreeNode('Hot', [])\n",
    "tree.addChild(cold)\n",
    "tree.addChild(hot)\n",
    "tea = TreeNode('Tea', [])\n",
    "coffee = TreeNode('Coffee', [])\n",
    "cola = TreeNode('Cola', [])\n",
    "fanta = TreeNode('Fanta', [])\n",
    "cold.addChild(cola)\n",
    "cold.addChild(fanta)\n",
    "hot.addChild(tea)\n",
    "hot.addChild(coffee)\n",
    "print(tree)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af123c31",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

