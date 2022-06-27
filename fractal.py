
def bubbles(x, y, r, depth):
  if depth > 0:
    
    picture.draw_filled_square(x, y, r)

    north_x = x + r//3
    north_y = y - 2* r//3
    bubbles(north_x, north_y, r//3, depth - 1)

    south_x = x + r//3
    south_y = y +  4* r//3
    bubbles(south_x, south_y, r//3, depth - 1)

    west_x = x - 2* r//3
    west_y = y + r//3
    bubbles(west_x, west_y, r//3, depth - 1)

    
    east_x = x + 4 * r//3
    east_y = y + r//3
    bubbles(east_x, east_y, r//3, depth - 1)

    northeast_x = x + 4 * r//3
    northeast_y = y - 2* r//3
    bubbles(northeast_x, northeast_y, r//3, depth - 1)


    northwest_x = x - 2* r//3
    northwest_y = y - 2* r//3
    bubbles(northwest_x, northwest_y, r//3, depth - 1)
    
    southwest_x = x - 2 * r//3
    southwest_y = y +  4* r//3
    bubbles(southwest_x, southwest_y, r//3, depth - 1)


    southeast_x = x + 4 * r//3
    southeast_y = y + 4 * r//3
    bubbles(southeast_x, southeast_y, r//3, depth - 1)
    


    
    

 























import picture


def main(dim,depth):
  
  
  
  
  picture.new_picture(dim, dim)

  
  picture.set_fill_color("brown")
  picture.set_outline_color("brown")
  picture.draw_filled_square(0, 0, dim)

  # set buble colors
  picture.set_fill_color("orange")
  picture.set_outline_color("orange")

  r = dim//3
  center_x = dim // 3
  center_y = dim//3
  

 

  
  
  picture.draw_filled_square(center_x,center_y,r)
  bubbles(center_x, center_y, r, depth)
  
  
  picture.run()

def snowflakes(length,depth):
  if depth == 1:
    picture.draw_forward(length)
  if depth > 1:    
    snowflakes(length//3, depth-1)
           
    
    picture.rotate(-60)
    snowflakes(length//3, depth-1)
        
    
    picture.rotate(120)
    snowflakes(length//3, depth-1)
        
    
    picture.rotate(-60)
    snowflakes(length//3, depth-1)



    
    
    
    
        
        

        
        
        
       
        

      

        

import picture


def main1(dim,depth):

    

    picture.new_picture(dim, dim)

    picture.set_fill_color("skyblue")
    picture.set_outline_color("skyblue")
    picture.draw_filled_square(0, 0, dim)

    # set buble colors
    picture.set_fill_color("red")
    picture.set_outline_color("red")
    
    length = 0.8 * dim

    
    
    if depth == 1:
     picture.set_position(20,380)
     

     snowflakes(length, depth)
     picture.rotate(-120)
     snowflakes(length, depth)
     picture.rotate(-120)
     snowflakes(length, depth)
     

    
    

    else:

     
     picture.set_position(20,110)
    
     snowflakes(length, depth)
     picture.rotate(120)
    
    
     snowflakes(length, depth)
     picture.rotate(120)
     snowflakes(length, depth)

    

    picture.run()









  
print("Welcome to my program! ")
pattern = int(input("print 1 for the Carpet and 2 for the Snowflake."))


if pattern == 1 :
  dim = int(input("Please enter the size the canvas: "))
  depth = int(input("Please enter the depth: "))

  a = main(dim,depth)
  print(a)
if pattern == 2:
  dim = int(input("Please enter the size the canvas: "))
  depth = int(input("Please enter the depth: "))
  b = main1(dim,depth)
  print(b)

  

