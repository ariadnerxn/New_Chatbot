name = input('What is your name? ')
print(f"\nHello {name}, welcome to your personal Recipe cheatsheet.")

print("What type of recipe would you like?\n")
print('1. Dessert\n')
print('2. Main meal\n')
print('3. Appetizer\n')
print('quit')
choice = input('\nType answer here (enter: 1, 2, 3, or quit): ')
while choice != 'quit':
    choiceDes = 'y'
    choiceMain = 'y'
    choiceApp = 'y'
    while choice != '1' and choice != '2' and choice != '3' and choice != 'quit':
        choice = input('Enter your choice again (enter: 1, 2, 3, or quit): ')
        
    if choice == '1':
        
        while choiceDes == 'y':
            
            print('\n\n\nWhat dessert recipe would you like to learn? \n')
            print('1. Brownie')
            print('2. Orange Shortbread Cookies')
            
            recipe = input('\nEnter what recipe you wish to learn: ')
            if recipe == '1':
                
                print(f"\n\n~~{name}'s Brownie~~\n\n\n")
                print('servings: around 16\n')
                
                print('Ingredients:')
                print('\t1 1/2 cups granulated sugar (1 cup still works if you wish it to be less sweet)')
                print('\t3/4 cup all-purpose flour')
                print('\t2/3 cup cocoa powder, sifted if lumpy')
                print('\t1/2 cup powdered sugar, sifted if lumpy')
                print('\t1/2 cup dark chocolate chips')
                print('\t3/4 cup sea salt')
                print('\t2 large eggs')
                print('\t1/2 cup canola oil or extra-virgin olive oil')
                print('\t2 tablespoons water')
                print('\t1/2 teaspoon vanilla\n\n')
                
                print('instructions:')
                print('\tPreheat oven to 325 degrees F. ')
                print('\tUse an 8x8 pan. And as we all know, you are supposed to spray the pan (unless you have a non-stick pan, then you are fine).\n')
                print('\tIn a medium bowl, combine the sugar, flour, cocoa powder, powdered sugar, chocolate chips, and salt.\n')
                print('\tIn a large bowl, whisk together the eggs, olive oil, water, and vanilla.\n')
                print('\tDrizzle dry mix over wet mix, stirring until mixed fully.\n')
                print("\tPour the batter into the prepared pan (it'll be thick - that's ok) and use a spatula to smooth the top. Bake for 40 to 48 minutes,\n")
                print("\tor until a toothpick comes out with only a few crumbs attached")
                print('\n\t**It is better to pull the brownies out early than leaving them in too long.**\n')

                calories = input('Would you like to know the calorie count per serving of this recipe (enter: y/n)? ')
                while calories != 'y' and calories != 'n':
                    calories = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
                if calories == 'y':
                    print('\n\nCalories:\taround 167\n\n')

                choiceDes = input('Would you like another dessert recipe (enter: y/n)? ')
                while choiceDes != 'y' and choiceDes != 'n':
                    choiceDes = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')


            elif recipe == '2':
                
                print(f"\n\n~~{name}'s Orange Shortbread Cookies~~\n\n\n")
                print('servings: around 30\n')
                
                print('Ingredients:')
                print('\t1/2 cup unsalted butter, softened')
                print('\t1/3 cup cane sugar')
                print('\tzest of 1 medium orange')
                print('\t1 tablespoon fresh orange juice')
                print('\tA few drops of orange oil, optional, for more orange flavor')
                print('\t1 1/4 cups all-purpose flour, more for rolling')
                print('\t1/4 teaspoon sea salt')
                
                print('\nGlaze:')
                print('\t1/2 cup plus 1 tablespoon powdered sugar')
                print('\tsequin sprinkles, for decorating, optional')
                print('\tzest of 1 orange, for garnish')
                print('\t1 tablespoon almond milk\n\n')
                
                print('instructions:')
                
                print('cookie')
                print('\tPreheat oven to 350 degrees F. ')
                print('\tAn electric mixer is recommended to cream the butter, then add the sugar and beat until fluffy.\n')
                print('\tThen, add the orange zest, orange juice, and orange oil, if using, and mix again.\n')
                print('\tFinally, add the flour and salt and mix until just combined.\n')
                print('\tTurn the dough out onto a floured surface and flatten into a 1” disk. If the dough is sticky, wrap and chill for 15 to 30 minutes until firm but still pliable.\n')
                print("\tRoll the dough on a lightly floured surface until about ¼“ thick.\n")
                print('\tTransfer to the baking sheet and bake for 10 to 14 minutes or until the edges are lightly browned.\n')
                
                print('glaze')
                print('\tRemove from the oven and transfer the cookies to wire racks to cool completely before glazing.\n')
                print('\tMake the glaze. Whisk the powdered sugar and almond milk until smooth.\n')
                print("\tDrizzle over the cooled cookies and decorate them with sprinkles, if using, and orange zest.\n")


                calories = input('Would you like to know the calorie count per serving of this recipe (enter: y/n)? ')
                while calories != 'y' and calories != 'n':
                    calories = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
                if calories == 'y':
                    print('\n\nCalories w/ glaze:\taround 47\n')
                    print('Calories w/out glaze:\taround 40\n\n')
    
                    
                choiceDes = input('Would you like another dessert recipe (enter: y/n)? ')
                while choiceDes != 'y' and choiceDes != 'n':
                    choiceDes = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')


    elif choice == '2':

        while choiceMain == 'y':
            
            print('\n\n\nWhat meal recipe would you like to learn? \n')
            print('1. Honey Glazed Chicken')
            print('2. Slow Cooker Chicken Tacos')

            recipe = input('\nEnter what recipe you wish to learn: ')
            if recipe == '1':
                
                print(f"\n\n~~{name}'s Honey Glazed Chicken~~\n\n\n")
                print('servings: around 4\n')
                
                print('Ingredients:')
                print('\t1/4 cup honey')
                print('\t2 tablespoons soy sauce')
                print('\t1/8 teaspoon red pepper flakes')
                print('\t1 1/2 tablespoons olive oil')
                print('\t2 skinless, boneless chicken breast halves, cut into bite-sized pieces\n\n')
                
                print('instructions:')
                print('\twhisk honey, soy sauce, and red pepper flakes in a bowl. \n')
                print('\tHeat olive oil in a skillet over medium heat; cook and stir chicken in hot oil until lightly brown, about 5 minutes.\n')
                print('\tPour honey mixture into the skillet; continue to cook and stir until chicken is no longer pink in the center and sauce is thickened, about 5 minutes more.\n')


                calories = input('Would you like to know the calorie count per serving of this recipe (enter: y/n)? ')
                while calories != 'y' and calories != 'n':
                    calories = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
                if calories == 'y':
                    print('\n\nCalories:\taround 179\n\n')


                choiceMain = input('Would you like another main meal recipe (enter: y/n)? ')
                while choiceMain != 'y' and choiceMain != 'n':
                    choiceMain = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')


            elif recipe == '2':

                print(f"\n\n~~{name}'s Slow Cooker Chicken Tacos~~\n\n\n")
                print('servings: around 8\n')
                
                print('Ingredients:')
                print('\t1 cup chicken broth')
                print('\t3 tablespoons taco seasoning mix')
                print('\t1 pound skinless boneless chicken breasts\n\n')
                
                print('instructions:')
                print('\tPut chicken broth and taco seasoning mix in a bowl. \n')
                print('\tPlace chicken in a slow cooker and pour chicken broth mixture over chicken. \n')
                print('\tCook on low for 6-8 hours, then shred the chicken\n')


                calories = input('Would you like to know the calorie count per serving of this recipe (enter: y/n)? ')
                while calories != 'y' and calories != 'n':
                    calories = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
                if calories == 'y':
                    print('\n\nCalories:\taround 71\n\n')


                choiceMain = input('Would you like another main meal recipe (enter: y/n)? ')
                while choiceMain != 'y' and choiceMain != 'n':
                    choiceMain = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
    elif choice == '3':

        while choiceApp == 'y':
            
            print('\n\n\nWhat Appetizer recipe would you like to learn? \n')
            print('1. Velveeta Spicy Sausage Dip')
            print('2. Sausage and Cream Cheese Pinwheels')

            recipe = input('\nEnter what recipe you wish to learn: ')
            if recipe == '1':
                
                print(f"\n\n~~{name}'s Velveeta Spicy Sausage Dip~~\n\n\n")
                print('servings: around 32\n')
                
                print('Ingredients:')
                print('\t1 pound Velveeta, cut into 1/2 inch cubes')
                print('\t1 (10 ounce) can RO*TL Diced Tomatoes and Green Chilies, undrained')
                print('\t1/2 pound breakfast pork sausage, cooked and drained\n\n')
                
                print('instructions:')
                print('\tMix Velveeta, Ro-Tel, and cooked sausage together in microwave safe bowl \n')
                print('\tMicrowave on high for 3 minutes.\n')
                print('\tStir and microwave until Velveeta is completely melted for about 2 more minutes.\n')


                calories = input('Would you like to know the calorie count per serving of this recipe (enter: y/n)? ')
                while calories != 'y' and calories != 'n':
                    calories = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
                if calories == 'y':
                    print('\n\nCalories:\taround 62\n\n')


                choiceApp = input('Would you like another appetizer recipe (enter: y/n)? ')
                while choiceApp != 'y' and choiceApp != 'n':
                    choiceApp = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')


            elif recipe == '2':

                print(f"\n\n~~{name}'s Sausage and Cream Cheese Pinwheels~~\n\n\n")
                print('servings: around 12\n')
                
                print('Ingredients:')
                print('\t1 pound bulk pork sausage')
                print('\t2 (8 ounce) packages refrigerated crescent rolls')
                print('\t1 (8 ounce) package cream cheese, softened\n\n')
                
                print('instructions:')
                print('\tCook and stir sausage in large skillet over medium-high heat until brown and crumbly for about 10 minutes, then discard and drain the grease. \n')
                print('\tSpread dough from one package crescent rolls out onto a work surface and pinch perforations together to create a single sheet of dough. \n')
                print('\tSpread 1/2 of the cream cheese over dough leaving 1/2 inch margin on each edge.\n')
                print('\tSprinkle 1/2 of the cooked sausage evenly over the cream cheese.\n')
                print('\tStarting at the long edge, roll the dough around the filling into a log. Proceed to make a second one.\n')
                print('\tPut the rolls into the refridgerater for at least an hour.\n\n')
                print('\tPreheat the oven for 375 degrees F and cut rolls into 1/2 inch thick slices. Place on a backing sheet.\n')
                print('\tBake in the oven until golden brown. 10-15 minutes.\n')

                calories = input('Would you like to know the calorie count per serving of this recipe (enter: y/n)? ')
                while calories != 'y' and calories != 'n':
                    calories = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')
                if calories == 'y':
                    print('\n\nCalories:\taround 308\n\n')


                choiceApp = input('Would you like another appetizer recipe (enter: y/n)? ')
                while choiceApp != 'y' and choiceApp != 'n':
                    choiceApp = input('Enter a valid answer (y for yes / n for no: LOWERCASE): ')

    print('\n\n\n\n\n\n1. Dessert\n')
    print('2. Main Meal\n')
    print('3. Appetizer\n')
    print('\nquit')
    choice = input('\nType answer here (enter: 1, 2, 3, or quit): ')
    while choice != '1' and choice != '2' and choice != '3' and choice != 'quit':
        choice = input('Enter your choice again (enter: 1, 2, 3, or quit): ')

