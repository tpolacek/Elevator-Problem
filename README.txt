The design of the program is rather simple, many of the comments inside the code speak for themselves.  The most difficult to understand part would be the processing of the textile using regular expressions, which gets a little hairy in splitting by different delimiters and doing some processing in between.  Other than that, the processing of the route and number of floors traversed is rather straightforward.

Assumptions I have made with my code is that it will be run with command line arguments in the fashion:

python run_elevator.py testfile.txt B

where testfile.txt would be the name of the text file being input into the program, and B (or A) is the mode in which the user would like the elevator to run.

If there are any questions about what is happening at any point in the source code, please feel free to contact me at tim.polacek@gmail.com.

Thanks,
Tim Polacek