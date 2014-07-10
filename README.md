poortrace
=========

scripts that generates an IDA script to highlight instructions that were executed in GDB. 

To use:

assuming we have a ELF binary called "hello" we want to trace.

gdb --batch -x trace.gdb ./hello

the above command will generate a gdb.txt file

Now run ./ida_highlight.py

it will generate highlight.idc and clear.idc

Run IDA pro and load the highlight.idc script.  It will highlight the instructions that gdb recorded as executed.

Assuming you're using a white background for the graph, the clear.idc will revert the 'highlighted' lines and turn 
them back to white.
