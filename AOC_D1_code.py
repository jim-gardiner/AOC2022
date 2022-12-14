

file1 = open('AOC_2022_day1_input', 'r')
count = 0
  
while True:
    count += 1
  
    # Get next line from file
    line = file1.readline()
  
    # if line is empty
    # end of file is reached
    if not line:
        break
    print(line)
  
file1.close()
