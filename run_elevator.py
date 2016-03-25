import elevator
import processor
import sys

pr = processor.Processor(sys.argv[1])
el = elevator.Elevator(sys.argv[2])

results = pr.process_text()
for commands in results:
    el.move(commands)
