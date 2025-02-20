from collections import deque
import heapq
import copy
from node import Node 


''' This is the main class that defines the problem, Each functions'''
class agriculturePlan:
    def __init__(self, initial_state, seasonal_factor, production_cost, suitable_wilayas, consumption , prices_ranges, products, wilayas):

        self.initial_state = initial_state
        self.seasonal_factor = seasonal_factor
        self.production_cost = production_cost
        self.suitable_wilayas = suitable_wilayas
        self.consumption = consumption
        self.prices_ranges = prices_ranges
        self.products = products
        self.wilayas = wilayas
        pass 

    def action_cost(self,state,prod):
        total=0
        wilayas = self.suitable_wilayas[prod]
        for city in wilayas:
           total += state.compute_production(city,prod)

        return (1/total)


    def total_left_land_percentage (self, state):
        state_total = 0
        initial = 0
        for wilaya in self.wilayas:
           state_total += state.left_land(wilaya)
           initial += ( state.left_land(wilaya) + state.land_used(wilaya)) 

        p = ((state_total * 100) / initial)
        return p

    def self_suff_heuristic (self, state):
        sum = 0
        for prod in self.products:
            sum += state.product_self_suff(prod)
        s= 1-(sum/8)
        return s

    def heuristic (self, state):
        return (self.self_suff_heuristic(state)+ self.total_left_land_percentage(state))


    ##function that checks if the product is self sufficient in the state 
    def self_suff(self, node, product): 
                consumption= self.get_consumption(product) 
                production=node.state.product_total_amount(product) 
                if self.get_consumption(product)!= 0: 
                    ratio =  production / consumption 
                    node.state.update_self_sufficiency_ratio(product,ratio)  
             
    def is_self_suff(self, node , product):
        return (node.state.product_self_suff(product)>1 or node.state.product_self_suff(product)==1 )

    def lowest_price(self, state , product):
      production_cost_per_kg = self.production_cost[product]
      profit_margin = 0.1
      seasonal_factor = self.seasonal_factor[product]
      transportation_cost_per_kg = 50

      production_quantity = state.product_total_amount (product)
      demand_quantity = self.consumption[product]

      if not production_quantity == 0:
        season_price = (production_cost_per_kg + transportation_cost_per_kg) * ( demand_quantity /production_quantity ) 
        season_price *= (1 + profit_margin)

        out_season_price = (production_cost_per_kg + transportation_cost_per_kg) * ( demand_quantity / production_quantity ) * seasonal_factor
        out_season_price *= (1 + profit_margin)

        state.update_price ( product, season_price, out_season_price )

    def get_successors(self, node):
        chosen_product = []
        for product in self.products:
            if not self.Product_goal_test(node, product) and not self.Highest_production_lowest_price(node, product):
                chosen_product.append(product)
        return chosen_product
       
    def get_consumption (self, product):
        return self.consumption[product]

    
    def Highest_production_lowest_price(self,node, product): 
                if node.state.product_left_land(self.suitable_wilayas[product]) < node.state.product_all_land(self.suitable_wilayas[product]) *  0.05:
                    return True  
                else:
                    return False
                
    
    def Product_goal_test(self, node , product): 
            if self.is_self_suff( node ,product ) and self.satisfy_price(node, product): 
                return True 
            return False 
            
    def Global_goal_test( self , node ): 
            for product in self.products: 
                if not self.Product_goal_test( node, product ): 
                    return False 
            return True

    def land_factor(self, state, wilaya, current_product):
            Yield = state.get_yield(wilaya, current_product)
            if state.left_land(wilaya) < ( state.left_land(wilaya) + state.land_used(wilaya) )*0.05:
                return 0
            else:
                land_percentage = state.left_land(wilaya) / state.product_left_land(self.suitable_wilayas[current_product])

            if state.product_amount_per_wilaya(wilaya, current_product) == 0:
                prod_percentage = 0
            else:
                prod_percentage = state.product_amount_per_wilaya(wilaya, current_product) / state.product_total_amount(current_product)
            
            if Yield >= 100:
                Yield /= 1000
            elif Yield >= 10:
                Yield /= 100
            elif Yield >= 1:
                Yield /= 10

            return Yield - prod_percentage + land_percentage
    
    
    def action(self, current_product, state):
        wilayas = self.suitable_wilayas[current_product]
        max_average = -float('inf')
        best_wilaya = None
        for wilaya in wilayas:
            #land left for other activities(other products excluding the main ones we are working on ,and ranching)
            if not state.left_land(wilaya) == 0:
                factor = self.land_factor(state, wilaya, current_product)
                if factor == 0:
                    continue
                if factor > max_average:
                    max_average = factor
                    best_wilaya = wilaya
        if best_wilaya == None:
            return None
        child_state = copy.deepcopy(state)
        child_state.update_product_land (best_wilaya, current_product ) 
        self.lowest_price ( child_state , current_product)

        return child_state
    
    def expand_node(self, node, strategy="BFS"):
        state = node.state
        valid_actions = self.get_successors(node)
        child_nodes = []
        for product in valid_actions:
            child_state = self.action(product, state)
            if child_state is None:
                continue
            child_cost = 0
            if strategy in ["BFS", "DFS", "UCS"]:
                child_cost = node.cost + self.action_cost(child_state, product)
            elif strategy == "A*":
                child_heuristic = self.heuristic(child_state)
                child_cost = node.cost + self.action_cost(child_state, product) + child_heuristic
            elif strategy == "HC":
                child_heuristic = self.heuristic(child_state)
                child_cost = child_heuristic

            child_node = Node(child_state, parent=node, action=product, cost=child_cost)
            self.self_suff(child_node, product)
            child_nodes.append(child_node)

        return child_nodes

  
    def satisfy_price(self, node, product):
        return node.state.product_price(product) >= self.prices_ranges[product][0] and node.state.product_price(product) <= self.prices_ranges[product][1]

    def update_plot(self):
        for i, ax in enumerate(self.axes):
            ax.clear()
            ax.set_xlabel('Time (ms)')
            ax.set_ylabel('Value')
            ax.set_title(self.products[i])
            ax.plot(self.x_data, self.production_data[i], label='Production Value')
            ax.legend()
        plt.draw()
        plt.pause(0.1) 


   