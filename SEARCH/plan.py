''' This class is the data structure where the data will be stored.
    It implements some methods that makes it easy to access and modify the data
    during the search
    Then inner state of each node'''


class Plan: 
        def __init__(self, plan):
            self.plan = plan 
            pass
       
        def left_land (self, wilaya ):
            return self.plan["Wilayas"][wilaya]["left_land"]
        
     
        def land_used (self, wilaya ):
            return self.plan["Wilayas"][wilaya]["land_used"]
        

        def compute_expanded_land (self, wilaya, product ):
             return ( self.left_land(wilaya) + self.land_used(wilaya) )*0.05
        
        def compute_production (self, wilaya,product ):
           return self.plan["Wilayas"][wilaya]["Products"][product]["yield"]*self.compute_expanded_land(wilaya,product)

        def update_left_land (self, wilaya, land ):
            self.plan["Wilayas"][wilaya]["left_land"] -= land
            pass
        def update_land_used (self, wilaya, land):
            self.plan["Wilayas"][wilaya]["land_used"] += land
            pass

        def update_production (self, wilaya, product):
            self.plan["Wilayas"][wilaya]["Products"][product]["production"] = self.plan["Wilayas"][wilaya]["Products"][product]["yield"]*self.plan["Wilayas"][wilaya]["Products"][product]["land"]
            pass

        def update_product_land (self, wilaya, product):
            land = self.compute_expanded_land (wilaya, product) 
            self.plan["Wilayas"][wilaya]["Products"][product]["land"] += land
        
            ## after expanding  a land we must update these data  
            self.update_left_land(wilaya, land)
            self.update_land_used ( wilaya, land)
            self.update_production(wilaya, product)
            pass

        def product_left_land (self, suitable_wilayas ):
            total_left_land = 0
            for wilaya in suitable_wilayas:
                total_left_land += self.plan["Wilayas"][wilaya]["left_land"]
            return total_left_land

        def product_all_land (self, suitable_wilayas ):
            total_left_land = 0
            for wilaya in suitable_wilayas:
                total_left_land += self.plan["Wilayas"][wilaya]["left_land"]
                total_left_land += self.plan["Wilayas"][wilaya]["land_used"]
            return total_left_land
        
        def product_amount_per_wilaya(self, wilaya, product):
         try:
          return self.plan["Wilayas"][wilaya]["Products"][product]["production"]
         except KeyError:
          print(f"KeyError: The product '{product}' or the wilaya '{wilaya}' does not exist in the plan.")

        
        def product_total_amount (self, product):
            total_amount = 0
            for wilaya in self.plan["Wilayas"] :
                total_amount += self.product_amount_per_wilaya(wilaya,product)
            return total_amount
        
        def product_self_suff (self,product):
            return self.plan["Self-Sufficiency-Ratio"][product]
        
        def product_price (self, product):
            return self.plan["Prices"][product]["Season"]
        
        def update_price (self, product, season_price, out_season_price ):
             self.plan["Prices"][product]["Season"] = season_price
             self.plan["Prices"][product]["Out-Season"] = out_season_price
             pass

        def update_self_sufficiency_ratio (self, product, ratio ):
             self.plan["Self-Sufficiency-Ratio"][product] = ratio
             pass

        def get_yield(self,wilaya, product):
            yield_value =self.plan["Wilayas"][wilaya]["Products"][product]["yield"]
            return yield_value if yield_value is not None else 0
            pass

        def print_plan(self):
            for wilaya, details in self.plan["Wilayas"].items():
                print(f"Wilaya: {wilaya}")
                print(f"Left Land: {details['left_land']}")
                print(f"Land Used: {details['land_used']}")
                print("Products:")
                for product, product_details in details["Products"].items():
                    print(f"  {product}:")
                    print(f"    Land: {product_details['land']}")
                    print(f"    Production: {product_details['production']}")
                    print(f"    Yield: {product_details['yield']}")
                print()
            print("Self-Sufficiency-Ratio:")
            for product, value in self.plan["Self-Sufficiency-Ratio"].items():
                print(f"  {product}: {value}")
            print()
            print("Prices:")
            for product, value in self.plan["Prices"].items():
                print(f"  {product}: {value}")
            pass