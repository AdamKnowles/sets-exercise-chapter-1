# Practice: Showroom & Junkyard
# Create an empty set named showroom.
# Add four of your favorite car model names to the set.
# Print the length of your set.
# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
# Using update(), add two more car models to your showroom with another set.
# You've sold one of your cars. Remove it from the set with the discard() method.
# Acquiring more cars
# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

showroom = { 'honda', 'nissan', 'toyota', 'bmw', 'nissan'  }
print(len(showroom))
print(showroom)

showroom2 = {'tesla', 'acura'}
showroom.update(showroom2)
print(showroom)

showroom.discard('tesla')
print(showroom)


junkyard = {'lexus', 'ford', 'chevy', 'buick', 'toyota', 'acura'}

matching_cars = showroom.intersection(junkyard)
print(matching_cars)

all_cars = junkyard.union(showroom)
print(all_cars)

all_cars.discard('honda')
print(all_cars)