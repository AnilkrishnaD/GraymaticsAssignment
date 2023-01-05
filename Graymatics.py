#Solution: 1

#Assuming_firstline of input is max_weight
max_wt = int(input())
#Assuming_secondline of input is total_no_of_objects
n = int(input())
names_list = []
wt_list = []
vl_list = []
#Assuming weight&value are stored in a list
#next n lines of input are (name, weight, value)
for i in range(n):
    name, weight, value = input().split()
    names_list.append(name)
    wt_list.append(int(weight))
    vl_list.append(int(value))
    
def finding_max_value(max_wt, n, wt_list, vl_list):
    #Base case
    if max_wt == 0 or n == 0:
        return 0
    if (wt_list[n-1] > max_wt):
        return finding_max_value(max_wt, n-1, wt_list, vl_list)
    else:
        return max(vl_list[n-1]+finding_max_value(max_wt-wt_list[n-1], n-1, wt_list, vl_list), finding_max_value(max_wt, n-1, wt_list, vl_list))

max_possible_value = finding_max_value(max_wt, n, wt_list, vl_list)
print(max_possible_value)

#Solution 2 :-

def isCorrect (string):
       stack = []
       opening = set('([{')
       closing = set(')]}')
       pair = {')' : '(' , ']' : '[' , '}' : '{'}
       for i in string :
           if i in opening :
               stack.append(i)
           if i in closing :
               if not stack :
                   return False
               elif stack.pop() != pair[i] :
                   return False
               else :
                   continue
       if not stack :
           return True
       else :
           return False
           
input_string = input()
print(isCorrect(input_string))



#Solution: 3

import cv2 

def main():
	
	# reading the input
	cap = cv2.VideoCapture("C:\Users\91809\Pictures\Camera Roll\short video.mp4")

	output = cv2.VideoWriter(
		"output.avi", cv2.VideoWriter_fourcc(*'MPEG'),
	36, (1085, 1910))

	while(True):
		ret, frame = cap.read()
		if(ret):
			
			# adding filled rectangle on each frame
			cv2.rectangle(frame, (100, 140), (500, 650),
						(0, 255, 0), -1)
			
			# writing the new frame in output
			output.write(frame)
			cv2.imshow("output", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			break

	cv2.destroyAllWindows()
	output.release()
	cap.release()

main()

