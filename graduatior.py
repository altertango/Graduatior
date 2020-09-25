import csv

programs=[]
min_opcional=[]
CSs=[]
OSs=[]

f="Programs.csv"
with open(f, "rt", encoding="utf8") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	header = reader.__next__()
	for line in reader:
		if line[0]=="P" and not line[1] in programs: 
			programs.append(line[1])
			min_opcional.append(line[2])
			CSs.append([])
			OSs.append([])
		elif line[0]=="CS":
			CSs[programs.index(line[1])].append(line[2])
		elif line[0]=="OS":
			OSs[programs.index(line[1])].append(line[2])

f="Input.csv"
st=[]
st_p=[]

with open(f, "rt", encoding="utf8") as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	header = reader.__next__()
	for line in reader:
		if line[0] not in st:
			st.append(line[0])
			st_p.append([])
		st_p[st.index(line[0])].append([line[1],line[2]])

out=[["Student ID","Graduated","Obs"]]
for s in st:
	CP=[]
	CCSs=[]
	COSs=[]
	grad=False
	c_bool=False
	o_bool=False
	obs=""
	
	for i in st_p[st.index(s)]:
		if i[1] not in CP:
			CP.append(i[1])
			CCSs.append([])
			COSs.append([])
		if i[0] in CSs[programs.index(i[1])]:
			CCSs[CP.index(i[1])].append(i[0])
		if i[0] in OSs[programs.index(i[1])]:
			COSs[CP.index(i[1])].append(i[0])
	for i in CP:
		if len(CCSs[CP.index(i)])==len(CSs[programs.index(i)]):
			c_bool=True
		if len(COSs[CP.index(i)])>=int(min_opcional[programs.index(i)]):
			o_bool=True
		if not grad:
			grad= c_bool and o_bool
		if not grad:
			obs+=i+": "+(not c_bool)*("(Compulsory: "+"; ".join([x for x in CSs[programs.index(i)] if x not in CCSs[CP.index(i)]])+") ")+(not o_bool)*("(Optional: "+str(int(min_opcional[programs.index(i)])-len(COSs[CP.index(i)]))+" subject(s))")
	print("Student ID: ",s,"Graduated: ","Yes"*grad,("No"+" - "+obs)*(not grad))
	out.append([s,"Yes"*grad+("No")*(not grad),obs*(not grad)])
print("Saving output file")
with open('output.csv', 'wt', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for o in out:
		spamwriter.writerow(o)
input("Press Enter to continue...")