# christmas tree pattern with for loop
#        *
#       * *
#      * * *
#     * * * *
#    * * * * *          
#   * * * * * *        
#  * * * * * * *        
# * * * * * * * *   
#       ***
#       ***
#       ***   

n = 8 
i = 0
for i in range(n + 1):
     if i == n:
          print(("*" + " ") * n)
     else:
          print("*" +  " " * (n * 2 - 3) + "*")
     i += 1