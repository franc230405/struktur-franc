#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#   Created by Elshad Karimov 
#   Copyright © 2020 AppMillers. All rights reserved.

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"
    
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
    
    def deleteBT(self):
       self.customList = None
       return "The BT has been successfully deleted"

    
 

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

print(newBT.deleteBT())

newBT.levelOrderTraversal(1)



BinaryTreePL.py
Menampilkan BinaryTreePL.py.
Tugas Personal 9
Wilianto Gan
•
16 Mei (Diedit 23 Mei)
Tenggat: 23 Mei, 23.59
Silahkan dibuatkan kode python untuk file yang dikirimkan di bawah, beserta file latihan di kelas tadi. Kemudian kumpulkan kode python dalam format .py dan .ipynb yang sudah di push ke repository GitHub anda. Submit juga dalam zip file.

BinaryTree.py
Teks

BinaryTreePL.py
Teks

CreateTree.ipynb
File Biner

QueueLinkedList.py
Teks

BST.py
Teks

QueueLinkedList.py
Teks
Komentar kelas

