#!/usr/bin/python
import os

os.system("sed -n '/=>/p' gdb.txt | tr -d '=> ' > address.txt")

f2 = open('highight.idc','w')
f3 = open('clear.idc', 'w')

f2.write("#include <idc.idc>\n")
f3.write("#include <idc.idc>\n")

f2.write("static main(void) {\n")
f3.write("static main(void) {\n")

with open('address.txt') as f1:
   for address in f1:
      f2.write("SetColor(" + address.replace("\n","") + ", CIC_ITEM, 0xc7c7FF);\n")
      f3.write("SetColor(" + address.replace("\n","") + ", CIC_ITEM, 0xFFFFFF);\n")

f2.write("}\n")
f3.write("}\n")

f2.close()
f3.close()
