# -*- coding: iso-8859-15 -*-
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#opening the sheets through pandas 
#df is the complete data frame taken from the source
df = pd.read_excel(open('/home/douglas/Juliane/local.xlsx', 'rb'), decoding = 'utf-8', sheetname = 'Planilha2', index_col='Name')

#segregating the OEM group
oem = df.loc[df['Frage 1'].isin(['Ford', 'BMW'])]
#segregating the Tier1 group
tier1 = df.loc[df['Frage 1'].isin(['Conti', 'Conti Reg','Conti  Babenhausen', 'TRW', 'TRW DUeS', 'TRW Sherly',"TRW Ko", "Hella","Hella Lippstadt", "ZF Sachs","DRX BOeB", "Bosch Schwaebisch Gmuend", "Webasto","Bombardier -Primove", "Draexelmaier Interior", "Peiker"])]
#segregating the Tier2 group
tier2 = df.loc[df['Frage 1'].isin(['Renesas DUeS', 'Renesas', 'Perei'])]
#segregating the Non-Automotive group
na = df.loc[df['Frage 1'].isin(['Bosch- eBike Systems', 'Franki Gundbau', 'Soehner'])]

# second segmentations (VW, BMW, Others, Not Relevant)
vw = df.loc[df['Frage 6'].isin(['VW Konzern', 'Porsche /VW', 'VW', 'Audi', 'Porsche', 'Audi, VW, Seat Porsche'])]
bmw = df.loc[df['Frage 6'].isin(['BMW'])]
others = df.loc[df['Frage 6'].isin(['Daimler', 'Fiat', 'viele OEMS', 'Evobus', 'PSA', 'Honda/GM'])]
notrelevant = df.loc[df['Frage 6'].isin(['Eigenentwicklung, kein OEM, aber Fahrradhersteller geben Features vor', 'Hella', 'Eigenentwicklung / Marketing als Kunde', 'Franki Gundbau'])]


#size of the team
y = [1, 2, 3, 4, 5, 6]
labels = ['kleiner 10', '11 - 25', '26 - 50', '51 - 75', '75 - 100', ' groesser 100']
oem['Frage 7'].plot(kind='bar')
plt.xticks(rotation = 45)
plt.yticks(y, labels, rotation = 'horizontal')
plt.title('OEM')
plt.ylabel('Teamgroesse')
#plt.show()

tier1['Frage 7'].plot(kind= 'bar')
plt.xticks(rotation = 45)
plt.yticks(y, labels, rotation = 'horizontal')
plt.title('TIER 1')
plt.ylabel('Teamgroesse')
#plt.show()

tier2['Frage 7'].plot(kind= 'bar')
plt.xticks(rotation = 45)
plt.yticks(y, labels, rotation = 'horizontal')
plt.title('TIER 2')
plt.ylabel('Teamgroesse')
#plt.show()


na['Frage 7'].plot(kind= 'bar')
plt.xticks(rotation = 45)
plt.yticks(y, labels, rotation = 'horizontal')
plt.title('Non-automotive')
plt.ylabel('Teamgroesse')
#plt.show()


print vw