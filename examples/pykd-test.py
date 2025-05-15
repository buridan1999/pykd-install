# .load pykd
# use python 2x

import pykd

def my_function():
    print('BP trig')

#print(pykd.dbgCommand("kp"))

#pykd.callFunctionRaw(("DbgPrint", "message"))
result = pykd.getSystemVersion()
print(result)

nt_module = pykd.module("nt").begin()
print(nt_module)

nt_DbgPrint = pykd.getOffset('nt!DbgPrint')
print(nt_DbgPrint)

bp = pykd.setBp(nt_DbgPrint, my_function)
print(bp)
#help(bp)

bp_id = bp.getId()
print(bp_id)

pykd.dprintln("<b><u>The following command reloads all symbols</b></u>", True)
pykd.dprintln("<link cmd=\".reload /f\">reload</link>", True)

