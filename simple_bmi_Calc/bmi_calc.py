# A simple Calculator to Determin your body mass index (BMI)

# BMI is a function of height and weight. you can get more details from any medical journal online

# Please this is not any professional info or medical directives, and nothing is implied regarding your weight or health
# Please consult your doctor for professional directive and information

# Welcome the User

print("Welcome to your BMI Self Calculator") 

# Ask for use firstname 

firstName = input("Enter your firstname: ")

# Ask user for there weight
weight = input("Enter your weight: ")

# ask for user height
height = input("Enter your height: ")

# Type cast wegiht and height properly
main_weight = int(weight)
main_height = float(height) 

# print BMI to user 

bmi = main_weight/(main_height**2)
main_bmi = int(bmi) 
print(f" Hello {firstName}, your BMI as of today from the  data you entered is {main_bmi} \n \n ") 














