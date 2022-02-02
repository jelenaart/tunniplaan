from tkinter import *

aken=Tk()
aken.title("Tunnpiplaan")
aken.geometry("1200x700")

#Tunnid
t0=Label(text="0",relief="solid",width=10,height=5).grid(row=0,column=1,sticky=N+S+W+E)
t1=Label(text="1",relief="solid",width=10,height=5).grid(row=0,column=2,sticky=N+S+W+E)
t2=Label(text="2",relief="solid",width=10,height=5).grid(row=0,column=3,sticky=N+S+W+E)
t3=Label(text="3",relief="solid",width=10,height=5).grid(row=0,column=4,sticky=N+S+W+E)
t4=Label(text="4",relief="solid",width=10,height=5).grid(row=0,column=5,sticky=N+S+W+E)
t5=Label(text="5",relief="solid",width=10,height=5).grid(row=0,column=6,sticky=N+S+W+E)
t6=Label(text="6",relief="solid",width=10,height=5).grid(row=0,column=7,sticky=N+S+W+E)
t7=Label(text="7",relief="solid",width=10,height=5).grid(row=0,column=8,sticky=N+S+W+E)
t8=Label(text="8",relief="solid",width=10,height=5).grid(row=0,column=9,sticky=N+S+W+E)
t9=Label(text="9",relief="solid",width=10,height=5).grid(row=0,column=10,sticky=N+S+W+E)
t10=Label(text="10",relief="solid",width=10,height=5).grid(row=0,column=11,sticky=N+S+W+E)

#Paevad
Ep=Label(aken,text="Esmaspaev",relief="solid",height=7).grid(row=1,column=0,rowspan=2,sticky=N+S+W+E)
Tp=Label(aken,text="Teisipaev",relief="solid",height=7).grid(row=3,column=0,rowspan=2,sticky=N+S+W+E)
Kl=Label(aken,text="Kolmapaev",relief="solid",height=7).grid(row=5,column=0,rowspan=2,sticky=N+S+W+E)
Nl=Label(aken,text="Neljapaev",relief="solid",height=7).grid(row=7,column=0,rowspan=2,sticky=N+S+W+E)
Rd=Label(aken,text="Reede",relief="solid",height=7).grid(row=9,column=0,rowspan=2,sticky=N+S+W+E)

#Esmaspaev
EpMul1=Button(aken,text="Multimeedia Grupp 1",relief="solid",bg="#abc0ff").grid(row=1,column=2,columnspan=2,sticky=N+S+W+E)
EpProg2=Button(aken,text="Programmeerimise alused Grupp 2",relief="solid",bg="#abe0ff").grid(row=2,column=2,columnspan=3,sticky=N+S+W+E)
EpProg1=Button(aken,text="Programmeerimise alused Grupp 1",relief="solid",bg="#abe0ff").grid(row=1,column=5,columnspan=3,sticky=N+S+W+E)
EpMul2=Button(aken,text="Multimeedia Grupp 2",relief="solid",bg="#abc0ff").grid(row=2,column=5,columnspan=2,sticky=N+S+W+E)
EpRuhm=Button(aken,text="Ruhmajuhatajatund",relief="solid",bg="#abe0ff").grid(row=1,column=8,rowspan=2,sticky=N+S+W+E)



#Teisipaev
TpIn1=Button(aken,text="Inglise keel Grupp 1",relief="solid",bg="ivory").grid(row=3,column=2,columnspan=2,sticky=N+S+W+E)
TpIn2=Button(aken,text="Inglise keel Grupp 2",relief="solid",bg="plum").grid(row=4,column=2,columnspan=2,sticky=N+S+W+E)
TpOp=Button(aken,text="Operatsioonisusteemide alused",relief="solid",bg="violet").grid(row=3,column=4,columnspan=2,rowspan=2,sticky=N+S+W+E)
TpKeh=Button(aken,text="Kehaline kasvatus",relief="solid",bg="orchid").grid(row=3,column=7,columnspan=2,rowspan=2,sticky=N+S+W+E)
TpEst1=Button(aken,text="Eesti keel Grupp 1",relief="solid",bg="#ccb3ff").grid(row=3,column=9,sticky=N+S+W+E)
TpEst2=Button(aken,text="Eesti keel Grupp 2",relief="solid",bg="#cab4c7").grid(row=4,column=9,sticky=N+S+W+E)
TpAj=Button(aken,text="Ajalugu, inimgeograafia",relief="solid",bg="#ffe6b3").grid(row=3,column=10,rowspan=2,sticky=N+S+W+E)

#Kolmapaev
KlProg1=Button(aken,text="Programmeerimise alused Grupp 1",relief="solid",bg="#abe0ff").grid(row=5,column=2,columnspan=3,sticky=N+S+W+E)
KlMul2=Button(aken,text="Multimeedia Grupp 2",relief="solid",bg="#abc0ff").grid(row=6,column=2,columnspan=3,sticky=N+S+W+E)
KlMul1=Button(aken,text="Multimeedia Grupp 1",relief="solid",bg="#abc0ff").grid(row=5,column=6,columnspan=3,sticky=N+S+W+E)
KlProg2=Button(aken,text="Programmeerimise alused Grupp 2",relief="solid",bg="#abe0ff").grid(row=6,column=6,columnspan=3,sticky=N+S+W+E)
KlKuns=Button(aken,text="Kunstiained",relief="solid",bg="#e080ce").grid(row=5,column=9,columnspan=2,rowspan=2,sticky=N+S+W+E)

#Neljapaev
NlAnd=Button(aken,text="Andmebaasisusteemide alused (eesti keeles)",relief="solid",bg="#ff80a1").grid(row=7,column=2,columnspan=5,rowspan=2,sticky=N+S+W+E)
NlAj=Button(aken,text="Ajalugu, inimgeograafia",relief="solid",bg="#ffe6b3").grid(row=7,column=7,rowspan=2,sticky=N+S+W+E)
NlEst1=Button(aken,text="Eesti keel Grupp 1",relief="solid",bg="#ccb3ff").grid(row=7,column=8,sticky=N+S+W+E)
NlEst2=Button(aken,text="Eesti keel Grupp 2",relief="solid",bg="#cab4c7").grid(row=8,column=8,sticky=N+S+W+E)

#Reede
RdKeel=Button(aken,text="Keel ja kirjandus",relief="solid",bg="#e0ff80").grid(row=9,column=3,columnspan=2,rowspan=2,sticky=N+S+W+E)
RdMt=Button(aken,text="Matemaatika",relief="solid",bg="#fcb9d1").grid(row=9,column=6,columnspan=2,rowspan=2,sticky=N+S+W+E)
RdSuh=Button(aken,text="Suhtlemine ja klienditeenindus",relief="solid",bg="#c0abff").grid(row=9,column=8,columnspan=2,rowspan=2,sticky=N+S+W+E)
RdAj=Button(aken,text="Ajalugu, inimgeograafia",relief="solid",bg="#ffe6b3").grid(row=9,column=10,rowspan=2,sticky=N+S+W+E)


aken.mainloop()