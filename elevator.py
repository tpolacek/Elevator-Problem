"""Elevator Problem for BofA Code Review"""

class Elevator():
    building_height = 12
    op_mode = None
    commands = []

    # constructor
    def __init__(self, mode):
        self.op_mode = mode

    # basic move command, broken down by operating mode
    def move(self, commands):

        if self.op_mode == 'A':
            self.mode_A(commands)
        elif self.op_mode == 'B':
            self.mode_B(commands)
        else:
            print 'Improper operating mode given, please choose "A" or "B"'


    # define movement of elevator in Mode A
    def mode_A(self, commands):
        # In this mode, processs the commands one at a time, regardless of performance
        travel_distance = 0
        travel_log = []

        # get initial floor and remove it from the list of commands
        i_floor = commands[0]
        travel_log.append(i_floor)
        del commands[0]

        # now process each command one at a time
        for command in commands:
            for stop in command:

                # quick check to make sure command is a valid floor
                if stop > self.building_height or stop < 1:
                    print 'Elevator can not travel outside the ranges of floors 1 through 12'
                    return 0
                else:
                    current_floor = travel_log[-1]
                    travel_distance += abs(current_floor - stop)
                    if stop != travel_log[-1]:
                        travel_log.append(stop)

        # format and print output in correct fashion
        self.format_output(travel_distance, travel_log)

    # define movement of elevator in Mode B
    def mode_B(self, commands):
        # In this mode, processs the commands more than one at a time, if possible, to optimize performance
        travel_distance = 0
        travel_log = []

        # get initial floor and remove it from the list of commands
        i_floor = commands[0]
        travel_log.append(i_floor)
        del commands[0]

        # determine up and down component of each command
        up = []
        for command in commands:
            if command[0] < command[1]:
                up.append(True)
            else:
                up.append(False)

        # now process commands in optimal order
        while commands:
            queue = []

            # determine initial travel direction
            going_up = commands[0][0] < commands[0][1]

            # check to see if consecutive commands are going in the same direction
            # put all consecutive same direction commands in a queue to be executed
            for floors, direction in zip(commands, up):
                if direction == going_up:
                    queue.append(floors[0])
                    queue.append(floors[1])
                    commands.remove(floors)
                    up.remove(direction)
                else:
                    break

            # determine most efficient order of all queue commands
            if going_up:
                queue = sorted(set(queue))
            else:
                queue = sorted(set(queue), reverse=True)

            # remove first stop if elevator is already on that floor
            if queue[0] == travel_log[-1]:
                del queue[0]

            # execute stops
            for stop in queue:
                # quick check to make sure command is a valid floor
                if stop > self.building_height or stop < 1:
                    print 'Elevator can not travel outside the ranges of floors 1 through 12'
                    return 0
                else:
                    current_floor = travel_log[-1]
                    travel_distance += abs(current_floor - stop)
                    travel_log.append(stop)

        # format and print output in correct fashion
        self.format_output(travel_distance, travel_log)

    # method to format/print the output the correct way
    def format_output(self, distance, log):
        log.append(distance)
        str = ''

        for j in log:
            if j == log[-1]:
                str += '(%d)'
            else:
                str += '%d '

        print str % (tuple(log))
