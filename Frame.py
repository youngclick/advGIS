# Arup Guha
# 5/31/2012
# Calculates the area of a frame.

# Setting the dimensions of the outer and inner part of the frame.
out_length = int(input("What is the outer length of the frame?\n"))
out_width = int(input("What is the outer width of the frame?\n"))
in_length = int(input("What is the inner length of the frame?\n"))
in_width = int(input("What is the inner width of the frame?\n"))

# Calculate the area of both rectangles, and subtract to find the frame area.
total_area = out_length*out_width
inner_area = in_length*in_width
frame_area = total_area - inner_area

# Output the result.
print("The area of the border is ",frame_area,".",sep="")
