import sys                      # if  modules is present in the system directory eg location of dir_utitlity  folder -->import sys                      # if  modules is present in the system directory eg location of dir_utitlity  folder -->D:\\Programming\\DataScience
sys.path.append("D:\\Programming\\DataScience")


# import area                    # for import modules within itself.
from dir_utility import area     # for import modules from the directory "dir_utility"......(i)

print("Area of a circle is: ",area.area_circle(3))
print("Area of a rectangle is: ",area.area_square(2))

import dir_utility.area as xyz     # differnt statement simillar to ....(i)
print("Area of a circle is: ",xyz.area_circle(5))
print("Area of a rectangle is: ",xyz.area_square(6))
sys.path.append("D://Programming//DataScience")


# import area                    # for import modules within itself.
from dir_utility import area     # for import modules from the directory "dir_utility"......(i)

print("Area of a circle is: ",area.area_circle(3))
print("Area of a rectangle is: ",area.area_square(2))

import dir_utility.area as xyz     # differnt statement simillar to ....(i)
print("Area of a circle is: ",xyz.area_circle(5))
print("Area of a rectangle is: ",xyz.area_square(6))