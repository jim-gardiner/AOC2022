

file1 = open('AOC_2022_day1_input', 'r')
count = 0
calorie_counter = 0 
highest_count = 0
highest_count_list = []
while True:
    count += 1
  
    # Get next line from file
    line = file1.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break
    
    line = line.strip()
    
    if len(line) == 0:
        highest_count_list.append(calorie_counter)
        calories = 0
        calorie_counter = 0
        
    else:
        calories = int(line)
        calorie_counter = calories + calorie_counter

    if calorie_counter > highest_count:
        highest_count = calorie_counter
    
    print(calories, calorie_counter)
  
file1.close()


print(highest_count)

#print(highest_count_list)

highest_count_list.sort(reverse=True)

print(sum(highest_count_list[0:3]))

#print (highest_count)
#print (highest_count_list)
