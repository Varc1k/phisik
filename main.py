# импорт библиотек
import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np


# написание функции графика
def plot_graph(formula, x_label, y_label):
    x = np.linspace(-10, 10, 100)
    y = eval(formula)

    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


# создание события создания кнопки
def on_button_click():
    formula = formula_entry.get()
    x_label = x_label_entry.get()
    y_label = y_label_entry.get()
    plot_graph(formula, x_label, y_label)


# выбор типа графика
def on_graph_type_selected(event):
    selected_graph = graph_type_combobox.get()
    if selected_graph == "Гипербола":
        formula_entry.delete(0, tk.END)
        formula_entry.insert(0, "1 / x")
    elif selected_graph == "Парабола":
        formula_entry.delete(0, tk.END)
        formula_entry.insert(0, "x**2")
    elif selected_graph == "Прямая":
        formula_entry.delete(0, tk.END)
        formula_entry.insert(0, "x")


# вызов окна
root = tk.Tk()
root.title("Графики")

formula_label = ttk.Label(root, text="Формула:")
formula_label.pack()
formula_entry = ttk.Entry(root)
formula_entry.pack()

x_label_label = ttk.Label(root, text="Название оси X:")
x_label_label.pack()
x_label_entry = ttk.Entry(root)
x_label_entry.pack()

y_label_label = ttk.Label(root, text="Название оси Y:")
y_label_label.pack()
y_label_entry = ttk.Entry(root)
y_label_entry.pack()

graph_type_label = ttk.Label(root, text="Тип графика:")
graph_type_label.pack()
graph_type_combobox = ttk.Combobox(root, values=["Гипербола", "Парабола", "Прямая"])
graph_type_combobox.bind("<<ComboboxSelected>>", on_graph_type_selected)
graph_type_combobox.pack()

plot_button = ttk.Button(root, text="Построить график", command=on_button_click)
plot_button.pack()

root.mainloop()
