class VISA:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number
        
    def display_detais(self):
        print(self.holder_name)
        print(self.card_number)
        
    def compute_rewards(self,amount):
        reward=amount*0.01
        print("Reward for VISA is: ",reward)
        
class HPVISA(VISA):
    def compute_rewards(self,purchase_type,amount):
        reward=amount*0.01
        if purchase_type=="Fuel":
            reward+=10
        print("reward for HPVISA is",reward)
        
card_type = input().strip()
holder_name = input().strip()
card_number = input().strip()
amount = float(input())
purchase_type = input().strip()

if card_type == "VISA":
    card = VISA(holder_name, card_number)
elif card_type == "HPVISA":
    card = HPVISA(holder_name, card_number)
else:
    print("InvalidChoice")
    exit()

card.display_details()
print(f"{card.compute_reward_points(purchase_type, amount):.2f}")