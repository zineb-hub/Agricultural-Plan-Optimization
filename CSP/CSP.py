
from itertools import product
from tabulate import tabulate


## a dictionary that contains main information related to wilayas (land and yield for specific products)
Wilayas_info = {
    "Adrar": {
        "land":190,
        "Yield": {
            "Corn":40,
            "Dates": 53,
             "Tomato": 114.5},
        },
    
    "Tlemcen": {
            "land": 1037,
            "Yield": {
                
                "Olives":  500,
                
            },
        },
    "Mostaganem": {
            "land": 4480,

            "Yield": {

            "Potato": 1400,
            "Orange":  105.8,              
            },
        },
    
    "Mascara": {
            "land": 3332,
            "Yield": {
    
                
                "Olives": 900.4,
                "Orange": 640.6,
              
            },
        },     
    "Chlef": {
        "land": 4630, 
        "Yield": { 
            "Potato":1701, 
            "Tomato":300, 
            "Lentils":200, 
            "Orange":50.3, 
           
            },
       }, 
    "Annaba": {  
 
        "land":1170, 
        "Yield": {
            "Olives":  900,
            "Tomato":50, 
            "Lentils":110.7, 
           
        }  
 
     }, 
    "Skikda": {
            "land": 10430,
            "Yield": {  
                "Potato": 400,
                "Tomato": 250,
                "Corn":120.2,
            },
        },
    "El-Oued": {  
 
        "land": 9000, 
        "Yield": {
            "Dates":72.1, 
            "Potato":600,  

           
        },},
    "Bejaia": {
        "land": 5000,
        "Yield": {
            "Olives": 700,
        },
    },

}


# Data used for price calculations and self-sufficiency checking
production_cost = {"Potato":1.8, "Tomato":20 ,"Dates":150.15 , "Wheat":14.5 , "Corn": 150 , "Lentils":400 , "Olives":250.4 ,"Orange": 30}
seasonal_factor_dict = {"Potato":1.2, "Tomato":1.5 ,"Dates":2.3 , "Wheat":1.25 , "Corn": 1 , "Lentils":1.2 , "Olives":1.7 ,"Orange":4 }
consumption ={"Potato":21323758.405, "Tomato":1835946.912 ,"Dates":573733.41 , "Wheat":42073783.4 , "Corn":1200000  , "Lentils":347717.2181 , "Olives":7649778.8 ,"Orange":2486178.11 }
prices_ranges = {"Potato":[30, 60], "Tomato":[25, 60] ,"Dates":[200, 300] , "Wheat":[60, 100] , "Corn": [200, 250], "Lentils":[150, 200] , "Olives":[300, 400] ,"Orange":[60, 150]}

# a dictionary containing suitable lands for each product according to algerian wilayas
suitable_wilayas = {  
    'Corn': ["Skikda", "Adrar"],  
    'Dates': ["Adrar", "El-Oued"],  
    'Tomato': ["Adrar", "Chlef", "Annaba", "Skikda"],  
    'Potato': [ "Mostaganem",  "Chlef", "Skikda", "El-Oued"],  
    'Orange': ["Mostaganem", "Mascara", "Chlef"],  
    'Olives': ["Tlemcen", "Mascara","Annaba", "Bejaia"],  
    'Lentils': ["Chlef", "Annaba"],  
}

# a dictionary containing the each products neighbors ( other products having vommon lands )
common_wilayas_products = {  
    "Corn": {  
        "Adrar": ["Dates"],  
         "Skikda": ["Tomato"]  
    },  
    "Dates": {  
        "Adrar": ["Corn"],  
        "El-Oued": ["Potato", ]   
    },  
    "Tomato": {  
        "Adrar": ["Corn"],  
        "Chlef": ["Potato", "Lentils", "Orange"],  
       "Skikda": ["Potato",  "Corn"] ,
       "Annaba": ["Lentils"],
        "Skikda": ["Potato", "Corn"]   
    },  
    "Potato": {  
      "Mostaganem": ["Orange"],   
          
        "Chlef": ["Tomato", "Lentils", "Orange"],  
        "Skikda": ["Tomato",  "Corn"],   
        "El-Oued": [ "Dates"]  
    },  
    "Orange": {  
        "Mostaganem": ["Potato"], 
        "Mascara": ["Olives"],  
        "Chlef": ["Tomato", "Potato", "Lentils"]  
    },  
 
    "Olives": {  
        "Tlemcen": [],
        "Mascara": ["Orange"],
       "Annaba": ["Tomato",  "Lentils"], 
        "Bejaia": [],
    },  
    "Lentils": {  
        "Chlef": ["Tomato", "Potato", "Orange"],  
        "Annaba": ["Tomato"]  
    }  
}

# function that calculates the price for each product in season and out of the season
def lowest_price(product, land):
    production_cost_per_kg = production_cost[product]
    profit_margin = 0.1
    seasonal_factor = seasonal_factor_dict[product]  
    transportation_cost_per_kg = 50

    production_quantity = get_total_production(product, land)
    demand_quantity = consumption[product]

    if production_quantity != 0:  
        season_price = (production_cost_per_kg + transportation_cost_per_kg) * ( demand_quantity / production_quantity ) 
        season_price *= (1 + profit_margin)

        out_season_price = (production_cost_per_kg + transportation_cost_per_kg) * ( demand_quantity / production_quantity ) * seasonal_factor
        out_season_price *= (1 + profit_margin)

        return season_price, out_season_price  
    else:
        return None, None  

# function that returns the self-sufficiency ratio
def get_self_suff_ratio(product, land):
    ratio = get_total_production(product,land) / consumption[product]
    return ratio

# function that returns the total production if a specific product taken as a parameter along side with the land used for this production
def get_total_production(product, land):  
    wilayas = suitable_wilayas[product]
    production = 0
    for wilaya, wilaya_land in zip(wilayas, land or []):  
        production += Wilayas_info[wilaya]["Yield"][product] * wilaya_land
    return production

# function that returns all the possible land sets of a product for each wilaya 
# example: for corn and specifically in Adrar ,assuming it has a land of 190 hectars, then the possible lend set for it will be :
# S = { 0, 19 , 38, 57, 76, 95, 114, 133, 152, 171, 190 }: where the elements are increaing with 0.1 from the total land amount , in this case this amount is 19 hectars
# for each wilaya that produces the product passed as a parameter , a set is created as shown previously , and a list of sets is returned as a result

def possible_land_sets(product):
    wilayas = suitable_wilayas[product]
    land_sets = []
    for wilaya in wilayas:
        land = Wilayas_info[wilaya]["land"]
        land_value = 0
        land_set = []
        while land_value <= land :
            land_set.append(land_value)
            land_value += land * 0.1
        land_sets.append(land_set)

    return land_sets

# this function creates tuples containing all combinations from the elements of sets passed as parameters in which the order does not matter :
# eg: two sets are passed S1= {0,1}, S2 = {3, 4} , the created tuples are : (0,3), (0,4), (1,3), (1,4) , and returned as a list containing them
def different_set_tuples(*sets):
    tuples_list = []
    for tuple_elements in product(*sets):
        if len(set(tuple_elements)) == len(tuple_elements):
            tuples_list.append(tuple_elements)
    return tuples_list

# this function calls the previously explained functions such that: 
def possible_domain_values(product):
    #this function is called to create all possible land sets  of a product
    sets = possible_land_sets(product)
    #and this one takes those sets as parameters then creates all combinations tuples 
    tuples_list = different_set_tuples(*sets)
    return tuples_list # the result is a list of all tuples containing a land size from each wilaya that the product can grow in 

# this function creates the main domain of a product, a product value is a tuple of lands from all wilayas , the according production and price, self-sufficinecy ratio 
def product_domain(product):
    domain_values = possible_domain_values(product)
    domain = []
    wilayas = suitable_wilayas[product] 
    for land in domain_values:
        value = {}
        self_suff_ratio = get_self_suff_ratio(product, land)
        production = get_total_production(product, land)
        price = lowest_price(product, land) 

        value["price"] = price
        value["production"] = production
        value["self_sufficiency_rate"] = self_suff_ratio

        value["land"] = {}  

        for wilaya_land, wilaya in zip(land or [], wilayas):
            value["land"][wilaya] = wilaya_land

        domain.append(value)

    return domain

# this function prints the domain values
def print_domain_result(result):
    if not result:
        print("No domain values found.")
        return

    for value_count, value in enumerate(result, start=1):
        print(f"Value {value_count}:")
        print(f"  Price: {value.get('price', 'N/A')}")
        print(f"  Production: {value.get('production', 'N/A')}")
        print("  Land:")
        for wilaya, land in value.get('land', {}).items():
            print(f"    {wilaya}: {land}")
        print(f"  Self-sufficiency rate: {value.get('self_sufficiency_rate', 'N/A')}")
        





# -----------------------------------------Data for problem formulation:-----------------------------------------------------------------------

#****CONSTRAINTS****: here our constraints are defined as function to directly perform the checking withing the CSP class
# returns true if self-sufficiency ratio is greater than or equal to 1, else it returns false
def self_suff_constraint (value, product = None ):
    return value["self_sufficiency_rate"]>=1

# returns true if the seasonal price is in the convenient price range, else it returns false
def price_constraint(value,product):
    min_price, max_price = prices_ranges[product]
    if min_price <= value["price"][0] <= max_price:
        return True
    else:
        return False

# this is a list containing the constraints
constraints = []
constraints.append(self_suff_constraint)
constraints.append(price_constraint)

#****VARIABLES**** : 
products = [ "Corn","Dates","Lentils","Olives","Orange","Potato","Tomato"]
#****DOMAINS**** :

# returns a list of all products domains 
def total_domains():
    domains = {}
    for product in products:
        domain_of_product = product_domain(product)
        domains[product] = domain_of_product  
    return domains

domains = total_domains()

#-------------------------------------------------------------------------------------------------------------------------------------------------


#CSP class:

class CSP:
    def __init__(self, variables, domains, constraints ): 
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def solve(self):
      return self.backtrack({})

  
    def select_unassigned_variable(self, assignment): 
        for var in self.variables: 
            if var not in assignment: 
                return var 
        return None #might have an error

    def order_domain_values(self, var): 
        return self.domains[var]
  
    def is_consistent(self, value, var):  
       for constraint in constraints:
            if constraint(value , var ) == False: return False
       return True 

    

    def backtrack(self, assignment):
       
       
        if len(assignment) == len(self.variables):
             return assignment # All variables assigned

        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var):
            if self.is_consistent( value , var ):
                assignment[var] = value
                domains_backup = self.domains.copy() 
                self.update_domains(var, value)  # Update domains before inference
            
                result = self.backtrack(assignment)
                if result is not None:
                       return result
                       del assignment[var]
                       self.domains = domains_backup
                
        return None  # No solution found
        
    # updates the domains of the variables (products) having common lands with the chosen product (current variable), such that:
    #for each wilaya: all products having this wilaya land in common with the chosen products are involved in domain update
    #domain is updated as follows: if the chosen land from this wilaya is *190*, and the *maximum-land-value* that can be used from this wilaya is 171, then:
    #all those domains land values for this wilaya that are striclty greater than threshold = 190 - 171 = 19 must be removed
    def update_domains(self,product, value):

        wilayas = suitable_wilayas[product]
        current_product_domain = self.domains[product]
        

        for wilaya in wilayas:
            # finding the max land amount in wilaya
            max_land_amount = 0 
            for val in current_product_domain:
                    land = val["land"][wilaya]
                    if land > max_land_amount : max_land_amount = land
            # finding the chosen land   amount from the wilaya
            chosen_land_amount = value["land"][wilaya]   
            # finding the limit to update the products
            land_limit = max_land_amount - chosen_land_amount

            neighbor_products  =  common_wilayas_products[product][wilaya]

            for neighbor_product in neighbor_products:

                neighbor_domain = self.domains[neighbor_product] 

                for val in neighbor_domain:
                    land = val["land"][wilaya]
                    if land > land_limit : neighbor_domain.remove(val)

                self.domains[neighbor_product] = neighbor_domain 
            

    

# CSP object creation
csp=CSP( products, domains, constraints )
# CSP result test
result = csp.solve()






def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"
# function to print our assignment as a table
def print_table(data):
    headers = ["Crop", "Price (Season , Out Season)", "Production", "Self-Sufficiency Rate", "Land Distribution"]
    table = []
    
    for crop, details in data.items():
        price = f"({details['price'][0]:.2f}, {details['price'][1]:.2f})"
        production = f"{details['production']}"
        self_sufficiency_rate = f"{details['self_sufficiency_rate']}"
        land_distribution = ", ".join([f"{region}: {area}" for region, area in details['land'].items()])
        
        table.append([crop, price, production, self_sufficiency_rate, land_distribution])
    
    table_string = tabulate(table, headers, tablefmt="grid")

    green_frame_table_string = (
        table_string.replace("+", color_text("+", "92"))
                    .replace("-", color_text("-", "92"))
                    .replace("|", color_text("|", "92"))
    )
    
    header_color_code = "93"
    lines = green_frame_table_string.split('\n')
    
    for i, line in enumerate(lines):
        if all(c in "+-|" for c in line):
            lines[i] = color_text(line, "92")
        elif any(header in line for header in headers):
            lines[i] = color_text(line, header_color_code)
    
    # Print the colored table
    print('\n'.join(lines))


# printing the result of CSP
print_table(result)




