ingredients={
    "brownieMix":"1 box",
    "marshmallow creme":"1 cup",
    "water":"1/2 cup",
    "vegetable oil": "1/2 cup",
    "eggs": "1",
    "hot fudge topping":"1 jar",
    "graham crackers":"1 cup",
    "miniature marshmallows":"2 cups"
    }

steps= ["Heat oven to 350°F. Spray 9-inch square pan with cooking spray.", "Make brownies as directed on box for 9x9-inch pan. Cool 30 minutes. Use a wooden dowel to poke holes in brownies about 1 inch apart, pushing all the way down to bottom of pan.", "In small microwavable bowl, microwave marshmallow crème uncovered on High 30 seconds or until soft. Add water; stir until smooth and pourable. Pour over brownies. Let stand 30 minutes.", "Spread half of the hot fudge topping over top of brownies. Top with broken graham crackers and miniature marshmallows. Set oven control to broil. Broil with marshmallows 4 to 6 inches from heat 2 to 3 minutes or until marshmallows are lightly browned. Drizzle with remaining hot fudge topping. When ready to serve, cut into 4 rows by 4 rows."]

cookbook= {"recipes":{'brownies':"['ingredients', 'step']"}}
def smores_brownie():
    print("             ")
    print("How to Make S'mores Brownies")
    print("             ")
    print("Ingredients:")
    counter=1
    for i in ingredients:
        print (ingredients[i], i)
    print("             ")
    print("Instructions")
    for n in steps:
        print (counter, ".", n)
        counter+=1

def userRecipe():
    user_Input= input("Which ingredient do you want to know the amount of?")
    if user_Input in ingredients:
        print(ingredients[user_Input])
    else:
        print("Please retype, that ingredient doesn't exist")

# def cook_book():
#     print(cookbook["recipes"]['brownies'])
    # print(cookbook["recipes"])
    # user_choice= input("Which one")
    # if user_choice== "brownies":
    #     print(cookbook["recipes"['brownies']])
    # if user_choice=="cookies":
    #
    # else:
    #     print("Please retype, there is no such ingredient")

#cook_book()
smores_brownie()
print("        ")
userRecipe()
