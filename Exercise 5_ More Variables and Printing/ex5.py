
my_name = ' Milene Wiebe '
my_age = 17 # this is true
my_height  = 74 # inches
my_weight = 115 #pounds
my_eyes = ' Brown'
my_teeth = 'white' 
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "She's %d inches tall" % my_height
print "She's %d pounds heavy" % my_weight
print "Actually, that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# 2) Convert lbs to kilos and inches to cm'

lbs_to_kilos = 1/2.2
in_to_cm = 2.54

print "She's %dcm tall" % (my_height * in_to_cm)
print "She's %d kilograms heavy." % (my_weight * lbs_to_kilos)
