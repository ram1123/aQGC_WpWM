import sys

if len(sys.argv) != 1:
     print "Usage:"
     print "python2.6 make_reweight_card.py"
     sys.exit(0)

#print "#******************************************************************"
#print "#                       Reweight Module                           *"
#print "#******************************************************************"
#print "# launch"
#print "#* Use the set command to specify the new set of parameter"
#print "#* Or specify a path to a valid param_card/banner"
#print "#* Example of valid command:"
#print "#*     set aewm1 137"
#print "#*     ~/param_card.dat"
#print "#*"
#print "#* Note:"
#print "#*   1) the value of alphas will be used from the event"
#print "#*      so the value of the param_card is not taken into account."
#print "#*   2) It is dangerous to change a mass of any particle."
#print ""
#print ""
#print "#* If you want to compute the weight for more than one hyppothesis"
#print "#* you need first to uncomment the following line:"
#print "# launch"
#print "# and then use the set command to specify your parameter."
#print "# All modification will start from the ORIGINAL card not from the"
#print "# last define one."
#print "#* You can have as many weight as you want."
#print ""
#print ""
print "change helicity False"
print "change rwgt_dir rwgt"
print ""
print ""

#FS0
# Some problem with FS0 and FS1 parameter; Cross-section remains flat with parameter.
count=0
for i in range(-900,901):
    if i%20 == 0:
	test = str(round((i*1.0),4))
	test = test.replace("-","m")
	test = test.replace(".","p")
     	print "#************	FS0	***************************"
     	print "launch --rwgt_name=FS0_"+test
     	print "        set anoinputs 12 0.000000e+00"
     	print "        set anoinputs 1 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""

##FS1
for i in range(-330,331):
    if i%10 == 0:
	test = str(round((i*1.0),4))
     	test = test.replace("-","m")
     	test = test.replace(".","p")
     	print "#************	FS1	***************************"
     	print "launch --rwgt_name=FS1_"+test
     	print "        set anoinputs 12 0.000000e+00"
     	print "        set anoinputs 2 " +str((i*1.0)) + "00000e-12"
     	print ""
     	print ""

#FM0
for i in range(-42,43):
    if i%1 == 0:
     test = str(round((i*1),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print "#************	FM0	***************************"
     print "launch --rwgt_name=FM0_"+test
     print "        set anoinputs 12 0.000000e+00"
     print "        set anoinputs 3 " +str((i*1.0)) + "00000e-12"
     print ""
     print ""

#FM1
for i in range(-165,166):
    if i%5 == 0:
     test = str(round((i*1.0),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print "#************	FM1	***************************"
     print "launch --rwgt_name=FM1_"+test
     print "        set anoinputs 12 0.000000e+00"
     print "        set anoinputs 4 " +str((i*1.0)) + "00000e-12"
     print ""
     print ""

#FM6
for i in range(-84,84):
    if i%2 == 0:
     test = str(round((i*1.0),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print "#************	FM6	***************************"
     print "launch --rwgt_name=FM6_"+test
     print "        set anoinputs 12 0.000000e+00"
     print "        set anoinputs 9 " +str((i*1.0)) + "00000e-12"
     print ""
     print ""

#FM7
for i in range(-300,301):
    if i%5 == 0:
     test = str(round((i*1.0),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print "#************	FM7	***************************"
     print "launch --rwgt_name=FM7_"+test
     print "        set anoinputs 12 0.000000e+00"
     print "        set anoinputs 10 " +str((i*1.0)) + "00000e-12"     
     print ""
     print ""

#FT0
#for i in range(-8,9):
for i in range(-34,35):
    if i%1 == 0:
     test = str(round((i*0.2),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print "#************	FT0	***************************"
     print "launch --rwgt_name=FT0_"+test
     print "        set anoinputs 12 0.000000e+00"
     print "        set anoinputs 11 " +str((i*0.2)) + "00000e-12"
     print ""
     print ""

#FT1
#for i in range(-15,16):
for i in range(-25,26):
    if i%1 == 0:
     test = str(round((i*0.5),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print "#************	FT1	***************************"
     print "launch --rwgt_name=FT1_"+test
     print "        set anoinputs 12 " +str((i*0.5)) + "00000e-12"          
     print ""
     print ""

#FT2
#for i in range(-20,21):
for i in range(-41,42):
    if i%1 == 0:
     test = str(round((i*0.5),4))
     test = test.replace("-","m")
     test = test.replace(".","p")
     print ""
     print ""
     print "#************	FT2	***************************"
     print "launch --rwgt_name=FT2_"+test
     print "        set anoinputs 12 0.000000e+00"
     print "        set anoinputs 13 " +str((i*0.5)) + "00000e-12"
