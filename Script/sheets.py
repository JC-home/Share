# -*- coding: iso-8859-15 -*-
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#opening the sheets through pandas 
df1 = pd.read_excel(open('/home/douglas/Juliane/local.xlsx', 'rb'), decoding = 'utf-8', sheetname = 'Planilha2')
df = df1.sort_values('Frage 1')

#segregating the OEM group
oem = df.loc[df['Frage 1'].isin(['Ford', 'BMW'])]
#segregating the Tier1 group
tier1 = df.loc[df['Frage 1'].isin(['Conti', 'Conti Reg','Conti  Babenhausen', 'TRW', 'TRW DUeS', 'TRW Sherly',"TRW Ko", "Hella","Hella Lippstadt", "ZF Sachs","DRX BOeB", "Bosch Schwaebisch Gmuend", "Webasto","Bombardier -Primove", "Draexelmaier Interior", "Peiker"])]
#segregating the Tier2 group
tier2 = df.loc[df['Frage 1'].isin(['Renesas DUeS', 'Renesas', 'Perei'])]
#segregating the Non-Automotive group
na = df.loc[df['Frage 1'].isin(['Bosch- eBike Systems', 'Franki Gundbau', 'Soehner'])]




#size of the team
flag = [1, 1, 1, 1]
ii = flag.count(1)




y = [1, 2, 3, 4, 5, 6]
labels = ['kleiner 10', '11 - 25', '26 - 50', '51 - 75', '75 - 100', ' groesser 100']

if ii == 1:
    if flag[0] == 1:
        oem = oem.set_index('Frage 1')
        oem['Frage 7'].plot(kind='bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('OEM')
        plt.ylabel('Teamgroesse')       
    else: 
        pass
        
    if flag[1] == 1:
        tier1 = tier1.set_index('Frage 1')
        tier1['Frage 7'].plot(kind= 'bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('TIER 1')
        plt.ylabel('Teamgroesse')        
    else:
        pass

    if flag[2] == 1:
        tier2 = tier2.set_index('Frage 1')
        tier2['Frage 7'].plot(kind= 'bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('TIER 2')
        plt.ylabel('Teamgroesse')
    else:
        pass

    if flag[3] == 1:
        na = na.set_index('Frage 1')
        na['Frage 7'].plot(kind= 'bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('Non-automotive')
        plt.ylabel('Teamgroesse')
    else:
        pass
else:
    pass


if ii == 2 or ii == 3:
    fig, axes = plt.subplots(ii, 1)
    kk = 0
    if flag[0] == 1:
        oem = oem.set_index('Frage 1')
        oem['Frage 7'].plot( ax=axes[kk], kind='bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('OEM')
        plt.ylabel('Teamgroesse')
        kk = kk + 1
    else: 
        pass
        
    if flag[1] == 1:
        tier1 = tier1.set_index('Frage 1')
        tier1['Frage 7'].plot( ax = axes[kk], kind= 'bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('TIER 1')
        plt.ylabel('Teamgroesse')
        kk = kk + 1
    else:
        pass

    if flag[2] == 1:
        tier2 = tier2.set_index('Frage 1')
        tier2['Frage 7'].plot(ax = axes[kk], kind= 'bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('TIER 2')
        plt.ylabel('Teamgroesse')
        kk = kk +  1
    else:
        pass

    if flag[3] == 1:
        na = na.set_index('Frage 1')
        na['Frage 7'].plot(ax = axes[kk],  kind= 'bar')
        plt.xticks(rotation = 45)
        plt.yticks(y, labels, rotation = 'horizontal')
        plt.title('Non-automotive')
        plt.ylabel('Teamgroesse')
    else:
        pass




if ii ==  4:
    fig, axes = plt.subplots(2, 2)
    oem = oem.set_index('Frage 1')   
    oem['Frage 7'].plot( ax=axes[0,0], kind='bar')
    plt.xticks(rotation = 45)
    plt.yticks(y, labels, rotation = 'horizontal')
    plt.title('OEM')
    plt.ylabel('Teamgroesse')

    tier1 = tier1.set_index('Frage 1')         
    tier1['Frage 7'].plot( ax = axes[0,1], kind= 'pie')
    plt.xticks(rotation = 45)
    plt.yticks(y, labels, rotation = 'horizontal')
    plt.title('TIER 1')
    plt.ylabel('Teamgroesse')

    tier2 = tier2.set_index('Frage 1')
    tier2['Frage 7'].plot(ax = axes[1,0], kind= 'bar')
    plt.xticks(rotation = 45)
    plt.yticks(y, labels, rotation = 'horizontal')
    plt.title('TIER 2')
    plt.ylabel('Teamgroesse')
 
    na = na.set_index('Frage 1')
    na['Frage 7'].plot(ax = axes[1,1],  kind= 'bar')
    plt.xticks(rotation = 45)
    plt.yticks(y, labels, rotation = 'horizontal')
    plt.title('Non-automotive')
    plt.ylabel('Teamgroesse')
    
else:
    pass

plt.show()


# second segmentations (VW, BMW, Others, Not Relevant)
vw = df.loc[df['Frage 6'].isin(['VW Konzern', 'Porsche /VW', 'VW', 'Audi', 'Porsche', 'Audi, VW, Seat Porsche'])]
bmw = df.loc[df['Frage 6'].isin(['BMW'])]
others = df.loc[df['Frage 6'].isin(['Daimler', 'Fiat', 'viele OEMS', 'Evobus', 'PSA', 'Honda/GM'])]
notrelevant = df.loc[df['Frage 6'].isin(['Eigenentwicklung, kein OEM, aber Fahrradhersteller geben Features vor', 'Hella', 'Eigenentwicklung / Marketing als Kunde', 'Franki Gundbau'])]

