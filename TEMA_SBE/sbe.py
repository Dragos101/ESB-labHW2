import publications as pub
import subscriptions as sub

# publications = pub.Publication().generate_publications(5)
# for x in publications:    
#   print(x)

subscriptii = sub.Subscription().generate_objects(5)
for x in subscriptii:
    for value in x:
      print(value, end = ';')
    print()
