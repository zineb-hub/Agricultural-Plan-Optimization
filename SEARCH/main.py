from collections import deque
import heapq
import queue
import copy

import matplotlib.pyplot as plt
import numpy as np
import time

from plan import Plan
from node import Node
from agriplan import agriculturePlan
from gui import DynamicPlot

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

plan = {
    "Wilayas": {
      
        "Adrar": {
            "left_land": 275551,
            "land_used": 0,
            "Products": {
                "Dates": {"land": 0, "production": 0, "yield": 33.1},
                "Potato": {"land": 0, "production": 0, "yield": 0},
                "Tomato": {"land": 0, "production": 0, "yield": 114.5},
                "Lentils": {"land": 0, "production": 0, "yield": 0},
                "Olives": {"land": 0, "production": 0, "yield": 0},
                "Orange": {"land": 0, "production": 0, "yield": 0},
                "Wheat": {"land": 0, "production": 0, "yield": 62.2},
                "Corn": {"land": 0, "production": 0, "yield": 45.7},
            },
        },
        # Continue with the rest of the wilayas
        "Tlemcen": {
            "left_land": 1073274,
            "land_used": 0,
            "Products": {
                "Dates": {"land": 0, "production": 0, "yield": 0},
                "Potato": {"land": 0, "production": 0, "yield": 107.3},
                "Tomato": {"land": 0, "production": 0, "yield": 0},
                "Lentils": {"land": 0, "production": 0, "yield": 0},
                "Olives": {"land": 0, "production": 0, "yield": 30},
                "Orange": {"land": 0, "production": 0, "yield": 0},
                "Wheat": {"land": 0, "production": 0, "yield": 101.5},
                "Corn": {"land": 0, "production": 0, "yield": 0},
            },
        },

        "Mostaganem": {
            "left_land": 444778,
            "land_used": 0,
            "Products": {
                "Dates": {"land": 0, "production": 0, "yield": 0},
                "Potato": {"land": 0, "production": 0, "yield": 142},
                "Tomato": {"land": 0, "production": 0, "yield": 0},
                "Lentils": {"land": 0, "production": 0, "yield": 0},
                "Olives": {"land": 0, "production": 0, "yield": 0},
                "Orange": {"land": 0, "production": 0, "yield": 105.8},
                "Wheat": {"land": 0, "production": 0, "yield": 121},
                "Corn": {"land": 0, "production": 0, "yield": 0},
            },
        },
        "Mascara": {
            "left_land": 334132,
            "land_used": 0,
            "Products": {
                "Dates": {"land": 0, "production": 0, "yield": 0},
                "Potato": {"land": 0, "production": 0, "yield": 104.5},
                "Tomato": {"land": 0, "production": 0, "yield": 0},
                "Lentils": {"land": 0, "production": 0, "yield": 0},
                "Olives": {"land": 0, "production": 0, "yield": 40.4},
                "Orange": {"land": 0, "production": 0, "yield": 64.6},
                "Wheat": {"land": 0, "production": 0, "yield": 92.3},
                "Corn": {"land": 0, "production": 0, "yield": 0},
            },
        },
    "Chlef": {"left_land": 462511, 
        "land_used":0, 
        "Products":{ 
            "Dates":{"land": 0, "production":0, "yield":0}, 
            "Potato":{"land": 0, "production":0, "yield":170.1}, 
            "Tomato":{"land": 0, "production": 0, "yield":300}, 
            "Lentils":{"land": 0 , "production": 0, "yield":12}, 
            "Olives":{"land": 0, "production":0, "yield":0}, 
            "Orange":{"land": 0, "production":0, "yield":50.3}, 
            "Wheat":{"land": 0, "production":0, "yield":85}, 
            "Corn":{"land": 0, "production":0, "yield":0} 
        }  
     }, 
    
   
    "Annaba": {  
 
        "left_land":117820, 
        "land_used":0, 
        "Products":{ 
            "Dates":{"land": 0, "production":0, "yield":0}, 
            "Potato":{"land":0, "production":0, "yield":0}, 
            "Tomato":{"land": 0, "production": 0, "yield":150}, 
            "Lentils":{"land": 0, "production":0, "yield":11.7}, 
            "Olives":{"land": 0, "production":0, "yield":0}, 
            "Orange":{"land": 0, "production":0, "yield":0}, 
            "Wheat":{"land":0, "production":0, "yield":117.6}, 
            "Corn":{"land": 0, "production":0, "yield":0} 
        }  
 
     }, 
     "Skikda": {"left_land": 193023,
            "land_used": 0,
            "Products": {
                "Dates": {"land": 0, "production": 0, "yield": 0},
                "Potato": {"land": 0, "production": 0, "yield": 104.7},
                "Tomato": {"land": 0, "production": 0, "yield": 250},
                "Lentils": {"land": 0, "production": 0, "yield": 0},
                "Olives": {"land": 0, "production": 0, "yield": 0},
                "Orange": {"land": 0, "production": 0, "yield": 0},
                "Wheat": {"land": 0, "production": 0, "yield": 84.9},
                "Corn": {"land": 0, "production": 0, "yield": 42.2},
            },
        },
            "El-Oued": {  
 
        "left_land": 159876, 
        "land_used":0, 
        "Products":{ 
            "Dates":{"land": 0, "production":0, "yield":72.1}, 
            "Potato":{"land": 0, "production":0, "yield":124.1}, 
            "Tomato":{"land": 0, "production": 0, "yield":0}, 
            "Lentils":{"land":0 , "production":0, "yield":0}, 
            "Olives":{"land": 0, "production":0, "yield":0}, 
            "Orange":{"land": 0, "production":0, "yield":0}, 
            "Wheat":{"land": 0, "production":0, "yield":116.2}, 
            "Corn":{"land": 0, "production":0, "yield":0} 
        }  
 
     }
       
},
"Self-Sufficiency-Ratio": {
        "Dates": 0,
        "Potato": 0,
        "Tomato": 0,
        "Lentils": 0,
        "Olives": 0,
        "Orange": 0,
        "Wheat": 0,
        "Corn": 0,
    },
    
    "Prices": {
        "Dates": {"Season":0, "Out-Season": 0 } , 
        "Potato":  {"Season":0, "Out-Season": 0 } , 
        "Tomato": {"Season":0, "Out-Season": 0 }, 
        "Lentils": {"Season":0, "Out-Season": 0 }, 
        "Olives": {"Season":0, "Out-Season": 0 }, 
        "Orange": {"Season":0, "Out-Season": 0 }, 
        "Wheat": {"Season":0, "Out-Season": 0 }, 
        "Corn": {"Season":0, "Out-Season": 0 } 
    }
}


def search_algorithm(problem, strategy, dynamic_plot=None):
    if strategy not in ["DFS", "UCS", "A*"]:
        raise ValueError("Invalid search strategy")

    start_time = time.time()  # Track start time for dynamic plotting

    if strategy == "DFS":
        frontier = queue.LifoQueue() 
    else:
        frontier = queue.PriorityQueue() 

    # Create the start node
    start_node = Node(problem.initial_state)
    
    # Put the start node into the frontier with appropriate priority
    if strategy == "A*":
        frontier.put((-(start_node.cost + problem.heuristic(start_node.state)), start_node))
    elif strategy == "UCS":
        frontier.put((-start_node.cost, start_node))
    else:
        frontier.put(start_node)

    # Set to keep track of explored states
    explored = set()

    # Main loop for searching
    while not frontier.empty():
        current_time_ms = (time.time() - start_time) * 1000
        if strategy in ["A*", "UCS"]:
            cost, node = frontier.get()
        else:
            node = frontier.get()

        # Update dynamic plot with new data
        if dynamic_plot:

            production_values = [node.state.product_self_suff(product) for product in problem.products]
            dynamic_plot.add_data(current_time_ms, production_values)
            dynamic_plot.update_plot()

        if problem.Global_goal_test(node):
            return node

        explored.add(node.state)

        for child_node in problem.expand_node(node, strategy):
            if child_node.state not in explored:
                if strategy == "A*":
                    frontier.put((-(child_node.cost + problem.heuristic(child_node.state)), child_node))
                elif strategy == "UCS":
                    frontier.put((-child_node.cost, child_node))
                else:
                    frontier.put(child_node)

        # Add a small delay to make the plot appear more dynamic
        time.sleep(0.1)

    return None


def hill_climbing(problem):
    current_node = Node(problem.initial_state)
    steps = 0
    start_time = time.time()

    while True:
        steps += 1
        # print("Exploring node with cost:", problem.heuristic(current_node.state))
        # print("Depth:", current_node.depth)

        current_time_ms = (time.time() - start_time) * 1000
        if dynamic_plot:

            production_values = [current_node.state.product_self_suff(product) for product in problem.products]
            dynamic_plot.add_data(current_time_ms, production_values)
            dynamic_plot.update_plot()

        if problem.Global_goal_test(current_node):
            return current_node

        neighbors = problem.expand_node(current_node, "hc")
        best_neighbor = min(neighbors, key=lambda x: problem.heuristic(x.state))

        if problem.heuristic(best_neighbor.state) >= problem.heuristic(current_node.state):
            return current_node

        current_node = best_neighbor

    return None

def display_solution(plan):
    
    solution_window = tk.Toplevel()
    solution_window.title("Agriculture Plan Solution")

    # Calculate total production for each product
    total_production = {}
    for wilaya, details in plan["Wilayas"].items():
        for product, product_details in details["Products"].items():
            total_production[product] = total_production.get(product, 0) + product_details["production"]

    # Create a canvas and a vertical scrollbar
    canvas = tk.Canvas(solution_window)
    scrollbar = ttk.Scrollbar(solution_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
    solution_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=solution_frame, anchor="nw")

    # Function to configure the canvas scroll region
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    solution_frame.bind("<Configure>", on_frame_configure)

    # Title
    title_label = ttk.Label(solution_frame, text="Agriculture Plan Solution", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, columnspan=5, pady=10)

    # Wilayas details
    wilayas = list(plan["Wilayas"].keys())
    # Header
    wilaya_header_label = ttk.Label(solution_frame, text="Wilayas", font=("Helvetica", 14, "bold"))
    wilaya_header_label.grid(row=1, column=0)
    land_header_label = ttk.Label(solution_frame, text="Left Land (Ha)", font=("Helvetica", 14, "bold"))
    land_header_label.grid(row=1, column=1)
    land_used_header_label = ttk.Label(solution_frame, text="Land Used (Ha)", font=("Helvetica", 14, "bold"))
    land_used_header_label.grid(row=1, column=2)

    for i, wilaya in enumerate(wilayas):
        details = plan["Wilayas"][wilaya]
        # Wilaya name
        wilaya_label = ttk.Label(solution_frame, text=wilaya)
        wilaya_label.grid(row=i + 2, column=0, padx=5, pady=5)
        # Land
        land_label = ttk.Label(solution_frame, text=details["left_land"])
        land_label.grid(row=i + 2, column=1, padx=5, pady=5)
        # Land Used
        land_used_label = ttk.Label(solution_frame, text=details["land_used"])
        land_used_label.grid(row=i + 2, column=2, padx=5, pady=5)

    # Total Production
    total_production_label = ttk.Label(solution_frame, text="Total Production (Qx)", font=("Helvetica", 14, "bold"))
    total_production_label.grid(row=len(wilayas) + 2, column=0, columnspan=2, pady=10, sticky="w")

    for i, (product, production) in enumerate(total_production.items()):
        product_label = ttk.Label(solution_frame, text=f"{product}: {production}")
        product_label.grid(row=len(wilayas) + 3 + i, column=0, columnspan=2, pady=5, sticky="w")

    # Self Sufficiency
    self_sufficiency_label = ttk.Label(solution_frame, text="Self Sufficiency", font=("Helvetica", 14, "bold"))
    self_sufficiency_label.grid(row=1, column=3, pady=10, padx=10)

    for i, (product, self_sufficiency) in enumerate(plan["Self-Sufficiency-Ratio"].items()):
        ratio_label = ttk.Label(solution_frame, text=f"{product}: {self_sufficiency}")
        ratio_label.grid(row=i + 2, column=3, pady=5, padx=10)

    # Prices
    prices_label = ttk.Label(solution_frame, text="Prices (DZA)", font=("Helvetica", 14, "bold"))
    prices_label.grid(row=len(wilayas) + 2, column=3, pady=10, padx=10)

    for i, (product, price_details) in enumerate(plan["Prices"].items()):
        price_label = ttk.Label(solution_frame, text=f"{product}: Season - {price_details['Season']}, Out-Season - {price_details['Out-Season']}")
        price_label.grid(row=len(wilayas) + 3 + i, column=3, pady=5, padx=10)


def start_search(problem,algorithm,plot):
   
    if algorithm=="HC":
       solution = hill_climbing(problem)
    else : 
       solution = search_algorithm(problem,algorithm,plot)

    display_solution(solution.state.plan)


#Initialisation
initial_state = Plan(plan)

seasonal_factor = {"Potato":1.2, "Tomato":1.5 ,"Dates":2.3 , "Wheat":1.25 , "Corn": 1 , "Lentils":1.2 , "Olives":1.7 ,"Orange":4 }
production_cost = {"Potato":75.8, "Tomato":150 ,"Dates":580.15 , "Wheat":200.4 , "Corn": 500 , "Lentils":380 , "Olives":750.4 ,"Orange": 350}
prices_ranges = {"Potato":[30, 50], "Tomato":[25, 60] ,"Dates":[200, 300] , "Wheat":[70, 100] , "Corn": [200, 250], "Lentils":[150, 200] , "Olives":[300, 400] ,"Orange":[80, 150]}
wilayas = {"Skikda","Adrar", "Chlef","Tlemcen", "Mostaganem","El-Oued", "Annaba", "Mascara"}
suitable_wilayas = {  
    'Corn':[ "Skikda","Adrar", "Chlef"] , 
    'Wheat':["Tlemcen", "Mostaganem","El-Oued", "Adrar" ],  
    'Olives':["Mascara", "Tlemcen"] , 
    'Orange':["Mostaganem", "Chlef","Mascara", "El-Oued"] , 
    "Potato": [ "El-Oued",  "Mascara", "Mostaganem"],  
    "Dates": ["Adrar", "El-Oued"], 
    "Tomato": ["Skikda","Adrar","Annaba"], 
    "Lentils": ["Annaba","Chlef"],
}
consumption ={"Potato":21323758.405, "Tomato":1835946.912 ,"Dates":573733.41 , "Wheat":22073783.4 , "Corn":1200000  , "Lentils":347717.2181 , "Olives":7649778.8 ,"Orange":2486178.11 }
products = ["Dates", "Potato", "Tomato", "Lentils", "Olives","Orange", "Wheat", "Corn" ]


# Create the agriculturePlan object
myPlan = agriculturePlan(initial_state, seasonal_factor, production_cost, suitable_wilayas, consumption, prices_ranges, products, wilayas)

# Create a tkinter window
root = tk.Tk()
root.title("Agriculture Plan Search")
root.geometry("800x400")  # Set window size

# Title
title_label = ttk.Label(root, text="Agriculture Plan Search", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# #Display image
# image = Image.open("MEFTAH ZINEB/Project/SEARCH/logo.jpg")
# photo = ImageTk.PhotoImage(image)
# image_label = ttk.Label(root, image=photo)
# image_label.pack()

# Label for algorithm selection
algo_label = ttk.Label(root, text="Select Search Algorithm:", font=("Helvetica", 12))
algo_label.pack(pady=5)
# Combobox for selecting algorithm
algorithm_var = tk.StringVar()
algorithm_combobox = ttk.Combobox(root, textvariable=algorithm_var, values=["A*", "UCS", "DFS","HC"], font=("Helvetica", 12))
algorithm_combobox.pack()

fig, _ = plt.subplots(figsize=(8, 6))

# Initialize the DynamicPlot object with the existing figure
dynamic_plot = DynamicPlot(fig, num_products=8, products=products)
# Button to start the search
search_button = ttk.Button(root, text="Find Solution", command=lambda: start_search(myPlan,algorithm_var.get(),dynamic_plot))
search_button.pack(pady=10)
root.mainloop()

plt.show(block=True)

'''Please before running the program make sure to run the following command
 on terminal to instal matplot library: pip install matplotlib '''