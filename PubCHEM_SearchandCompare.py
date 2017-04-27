###Author Ahmed Mahmoud 2017###########

from Tkinter import *
import Tkinter as tk
import pubchempy as pcp
import os
import time
import datetime
import difflib
i = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
master = Tk()
cwgt=Canvas(master)
cwgt.pack(expand=YES, fill=BOTH)
cwgt.configure(background='white')
key = tk.StringVar(cwgt)
key.set('Choose Identifier Type')
choices = ["name","smiles","sdf","inchi","inchikey","formula"]
option = tk.OptionMenu(cwgt, key, *choices)
option.grid(row=0, column=5, sticky=S, pady=2)
Label(cwgt, text="Enter your Identifier: ").grid(row=0)
Label(cwgt, text='Compare two Compounds:').grid(row=4, column=1)
Label(cwgt, text='Compound 1 Name: ').grid(row=5)
Label(cwgt, text='Compound 2 Name: ').grid(row=7)
ID = Entry(cwgt)
ID.grid(row=0, column=1)
comp1 = Entry(cwgt)
comp1.grid(row=5, column=1)
comp2 = Entry(cwgt)
comp2.grid(row=7, column=1)
key1 = tk.StringVar(cwgt)
key1.set('Choose Identifier Type')
choices1 = ["isomeric_smiles","fingerprint","molecular_formula"]
option1 = tk.OptionMenu(cwgt, key, *choices1)
option1.grid(row=6, column=5, sticky=S, pady=2)
def pubchemsearch(ID,key):
    newdir= "/Users/ahmed.mahmoud/Documents/"+ ID + "_"+ str(i)
    os.makedirs(newdir,0755)
    results = pcp.get_compounds(ID,key)
    print 'There are ' + str(len(results)) + " Hits That Match to " + ID + ": "
    print results
    count = 1
    for c in results:
        dash = "------------------------------------------\n"
        print "###########################################\n"
        print " Hit " + str(count) + ": SMILES Annotation for " + str(c) + "\n"
        print str(c.isomeric_smiles) + "\n"
        print dash
        print " Hit " + str(count) + ": Formula for " + str(c) + "\n"
        print str(c.molecular_formula) + "\n"
        print dash
        print " Hit " + str(count) + ": Weight for " + str(c) + "\n"
        print str(c.molecular_weight) + "\n"
        print dash
        print " Hit " + str(count) + ": IUPAC for " + str(c) + "\n"
        print str(c.iupac_name) + "\n"
        print dash
        print " Hit " + str(count) + ": Fingerprint for " + str(c) + "\n"
        print str(c.fingerprint) + "\n"
        print " Hit " + str(count) + ": Synonyms for " + str(c) + "\n"
        print str(c.synonyms) + "\n"
        print "###########################################\n"
        text = "###########################################\n" + " Hit " + str(count) + ": SMILES Annotation for " + str(c) + "\n" + str(c.isomeric_smiles) + "\n" + dash + " Hit " + str(count) + ": Formula for " + str(c) + "\n" +  str(c.molecular_formula) + "\n" + dash + " Hit " + str(count) + ": Weight for " + str(c) + "\n" + str(c.molecular_weight)+ "\n" + dash + " Hit " + str(count) + ": IUPAC for " + str(c) + "\n" + dash + str(c.iupac_name) + "\n" +" Hit " + str(count) + ": Fingerprint for " + str(c) + "\n" + str(c.fingerprint) + "\n" + " Hit " + str(count) + ": Synonyms for " + str(c) + "\n"+ str(c.synonyms) 
        with open(newdir + "/" + str(c) + ".txt" , 'ab') as out:
            out.write(newdir+text)
            pcp.download('PNG', newdir + "/" + str(c) +'.png', ID, key)
        count = count + 1                  

def FingerprintCOMP(a1,a2,key):
    p = pcp.get_compounds(a1, "name")

    d = pcp.get_compounds(a2, "name")

    for c in p:
        if key == "isomeric_smiles":
            a = c.isomeric_smiles
        elif key == "molecular_formula":
            a = c.molecular_formula
        elif key == "fingerprint":
            a = c.fingerprint
        else:
            a = c.fingerprint
        print "Input 1 = " + a1
        print a
        print len(a)
        for i in d:
            if key == "isomeric_smiles":
                b = i.isomeric_smiles
            elif key == "molecular_formula":
                b = i.molecular_formula
            elif key == "fingerprint":
                b = i.fingerprint
            else:
                b = i.fingerprint
            print "Input 2 = " + a2
            print b
            print len(b)
            s = difflib.SequenceMatcher(None, a, b)
            print a1 + " and "+ a2 + " Have a similarity score of " + str(s.ratio()*100)
            for block in s.get_matching_blocks():
                print "Input 1 1[%d] and Input 2[%d] match for %d elements" % block
def run():
    pubchemsearch(ID.get(),key.get())

def run2():
    FingerprintCOMP(comp1.get(),comp2.get(),key1.get())
def quit_script():
   master.destroy()
   sys.exit()    

Button(cwgt, text='Quit', command=quit_script).grid(row=8, column=2)
Button(cwgt, text='Search PubChem!', command=run).grid(row=3, column=1, sticky=W, pady=4)
Button(cwgt, text='Compare', command=run2).grid(row=8, column=1, sticky=W, pady=4)
master.minsize(700,700)
mainloop( )
