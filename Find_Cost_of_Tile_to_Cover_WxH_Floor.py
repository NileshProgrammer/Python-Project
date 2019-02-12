#Taking cost of 1 Tile
cost = int(input("Enter the cost of 1 Tile:" ))
print(f"Cost of 1 Tile is {cost}Rs")

#floor height and width
f_width = 11
f_height = 10
print('Floor  width is 11 Feet and height is 10 Feet ')

#Tile Height and width
t_width = 60
t_height = 60
print('Tile width is 60 cm and height is 60 cm ')

#Total Area of Floor
f_area = f_width * f_height
print(f'Total area of floor is {f_area} sq ft')

#Total area of Tile
t_area = t_width * t_height
print(f'Total area of tile is {t_area} cm^2')

# COnverting cm to sq feet to equal unit 1cm^2 = 0.001sq feet
t_area_sqft = t_area * 0.001
print(f'Total area of 1 tile in sq feet is {t_area_sqft} sq ft')


#Calcualting Total Number of Tiles Required
no_of_Tile_Required = round(f_area / t_area_sqft)
print(f'Number of tiles required is {no_of_Tile_Required} tiles')
print(f'Total cost of Tile to cover{f_area} sq feet is {no_of_Tile_Required * cost} Rs')
