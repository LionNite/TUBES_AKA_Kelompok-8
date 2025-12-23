import sys
import time
import random
import threading
import tkinter
from tkiner import tkk, messagebox
import matplotlib.pyplot as plt

sys.batasrekursi(20000)

class nodeFile_or_Folder :
    def initial (self, nama, is_folder=False, size = 0 ):
        self.name = name
        self.is_folder = is_folder
        self.size = size # ukuran file (bytes). jika folder maka 0
        self.children = [] # list untuk menyimpan anak (jika folder)

    def add_child (self, node) :
        if self.is_folder :
            self.children.append(node)

#BAGIAN 2: ALGORITMA

def generate_node_dummy(total_items):
    #membuat sebuah folder bernama "Root" dan di isi dengan Folder dan file 
    root = nodeFile_or_Folder("Root", is_folder=True) 
    available_folders = [root]

    for i in range(total_items):
        parent = random.choice(available_folders)

        if random.random() > 0.3 : #Probabilitas 70% File & 30% Folder
            #Membuat file acak 1-10MB
            file_node = nodeFile_or_Folder(f"File_{i}", is_folder=False, size=random.randint(1024, 102400))
            parent.add_child(file_node)
        else:
            #Membuat Folder
            folder_node = nodeFile_or_Folder(f"Folder_{i}", is_folder=True)
            parent.add_child(folder_node)
            available_folders.append(folder_node) #Memasukan folder ke "available folder agar bisa di isi file nantinya"

    return root

def hitung_rekursif(node):
    """
    Algoritma 1: Rekursif (Memanggil fungsi diri sendiri)
    Kompleksitas: O(N)
    """

    #Base Case: Jika File, maka kembalikan size/ukuran file
    if not node.is_folder:
        return node.size
    
    total = 0
    for child in node.children:
        total += hitung_rekursif(child)
    return total 

def hitung_iteratif(root_node):
    """
    Algoritma 2: Iteratif (Menggunakan Stack Manual)
    Kompleksitas: O(N)
    """
    if not root_node.is_folder:
        return root_node.size

    total_size = 0 
    stack = [root_node] # Inisialisasi Stack

    while len(stack) > 0:
        current = stack.pop() # Ambil item paling atas (LIFO)

        if not current.is_folder:
            total_size + current.size
        else:
            stack.extend(current.children)
    
    return total_size