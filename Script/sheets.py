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


# second segmentations (VW, BMW, Others, Not Relevant)
vw = df.loc[df['Frage 6'].isin(['VW Konzern', 'Porsche /VW', 'VW', 'Audi', 'Porsche', 'Audi, VW, Seat Porsche'])]
bmw = df.loc[df['Frage 6'].isin(['BMW'])]
others = df.loc[df['Frage 6'].isin(['Daimler', 'Fiat', 'viele OEMS', 'Evobus', 'PSA', 'Honda/GM'])]
notrelevant = df.loc[df['Frage 6'].isin(['Eigenentwicklung, kein OEM, aber Fahrradhersteller geben Features vor', 'Hella', 'Eigenentwicklung / Marketing als Kunde', 'Franki Gundbau'])]

#dictionaries for each plot
aufteitung = 'Frage 1' #or Frage 6 - gives the macroset
frage = 'Frage 7' #input
##TODO CHANGE THE Y LABELS
if aufteitung == 'Frage 1':
    question_dict = {
                    'Frage 7': {'question': 'Frage 7', 'labels': ['kleiner 10', '11 - 25', '26 - 50', '51 - 75', '75 - 100', ' groesser 100'], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'bar', 'y_label' : 'Teamgroesse' },
                    'Frage 9': {'question': 'Frage 9', 'labels': ['Nein', 'Ja', 'Wenn Ja, findet'], 'y_axis' : [1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 13': {'question': 'Frage 13', 'labels': ['PL, TPL, SW-HW PL', 'PL, SW-HW PL', 'nur PL oder TPL', 'Programmmanager, PL, SW-HW'], 'y_axis' : [1, 2, 3, 4], 'kind' : 'bar', 'y_label' : 'Teamgroesse'},
                    'Frage 14': {'question': 'Frage 14', 'labels': ['keine', 'MS Project', 'RPlan', 'Excel'], 'y_axis' : [1, 2, 3, 4], 'kind' : 'bar','y_label' : 'Teamgroesse'},
                    'Frage 15': {'question': 'Frage 15', 'labels': ['Nein', 'Ja', 'Kundengetrieben'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'bar', 'y_label' : 'Teamgroesse' },
                    'Frage 18': {'question': 'Frage 18', 'labels': ['gar nicht', 'in MS Project geplant', 'in MS Project geplant und getrackt', 'in anderem Tool geplant'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : 'Teamgroesse' },
                    'Frage 19': {'question': 'Frage 19', 'labels': ['gar nicht', 'in SAP geplant', 'in SAP geplant and getrackt', 'in anderem Tool geplant'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 20': {'question': 'Frage 20', 'labels': ['gar nicht', '¨uber Versionierung', 'über Baseline', 'Versionierung und Baseline'], 'y_axis' : [1, 2, 3], 'kind' : 'pie','y_label' : 'Teamgroesse' },
                    'Frage 24a': {'question': 'Frage 24a', 'labels': [1, 2, 3, 4, 5, 6], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 24b': {'question': 'Frage 24b', 'labels': ['Teammeeting', 'Teammeeting und Standupmeeting', 'Teammeeting und Kundenmeeting', 'Team, Kunde- und Kundenmeeting', 'Standup, Team, weitere interne Meetings', 'Team, Kunde, weitere interne Meetings' ], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 26': {'question': 'Frage 26', 'labels': ['keine', 'Projektpläne', 'Terminplan, Projektplan, PM Plan, Projekthandbuch', 'zahlreiche PM Dokumente'], 'y_axis' : [0,1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 32': {'question': 'Frage 32', 'labels': ['Matrix', 'Linie', 'Matrix und Linie', 'Projektorga'], 'y_axis' : [1, 2, 3, 4], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 33': {'question': 'Frage 33', 'labels': ['Nein', 'Ja, erstellen Templates und Porzesse', 'andere Funktion'], 'y_axis' : [0, 1 ,2], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },            
                    }
elif aufteitung == 'Frage 6':
    question_dict = {
                    'Frage 10': {'question': 'Frage 10', 'labels': ['bis 25', '26-30', '31-35', '36-40', '41-45', '46-50', '>50'], 'y_axis' : [1, 2, 3, 4, 5, 6, 7], 'kind' : 'bar', 'y_label' : 'Teamgroesse' },
                    'Frage 12a': {'question': 'Frage 12a', 'labels': ['keine', 'OEM Schnittstelle PM', 'OEM Schnittstelle', 'OEM Schnittstellen zu vielen'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 15': {'question': 'Frage 15', 'labels': ['Nein', 'Ja', 'Kundengetrieben'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'bar', 'y_label' : 'Teamgroesse' },
                    'Frage 16': {'question': 'Frage 16', 'labels': ['Nein', 'Ja', 'von OEN vorgegeben', 'eigene Planung'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'bar','y_label' : 'Teamgroesse'},
                    'Frage 20': {'question': 'Frage 20', 'labels': ['gar nicht', '¨uber Versionierung', 'über Baseline', 'Versionierung und Baseline'], 'y_axis' : [1, 2, 3], 'kind' : 'pie','y_label' : 'Teamgroesse' },
                    'Frage 21': {'question': 'Frage 18', 'labels': ['gar nicht', 'über Versionierung', 'über Baselinie', 'über Spalte in Plan', 'automatisiert'], 'y_axis' : [0, 1, 2, 3, 4], 'kind' : 'pie','y_label' : 'Teamgroesse' },
                    'Frage 24a': {'question': 'Frage 24a', 'labels': [1, 2, 3, 4, 5, 6], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse' },
                    'Frage 24b': {'question': 'Frage 24b', 'labels': ['Teammeeting', 'Teammeeting und Standupmeeting', 'Teammeeting und Kundenmeeting', 'Team, Kunde- und Kundenmeeting', 'Standup, Team, weitere interne Meetings', 'Team, Kunde, weitere interne Meetings' ], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse' }
                      }

vector = question_dict[frage]    

#size of the team
flag = [0, 1, 0, 0]
ii = flag.count(1)

if ii == 1:
    if flag[0] == 1:
        if aufteitung == 'Frage 1':
            oem = oem.set_index('Frage 1')
            oem[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            vw = vw.set_index('Frage 6')
            vw[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('OEM')
        plt.ylabel(vector['y_label'])       
    else: 
        pass
        
    if flag[1] == 1:
        if aufteitung == 'Frage 1':
            tier1 = tier1.set_index('Frage 1')
            tier1[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            bmw = bmw.set_index('Frage 6')
            bmw[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('TIER 1')
        plt.ylabel(vector['y_label'])        
    else:
        pass

    if flag[2] == 1:
        if aufteitung == 'Frage 1':
            tier2 = tier2.set_index('Frage 1')
            tier2[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            others = others.set_index('Frage 6')
            others[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('TIER 2')
        plt.ylabel(vector['y_label'])
    else:
        pass

    if flag[3] == 1:
        if aufteitung == 'Frage 1':
            na = na.set_index('Frage 1')
            na[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            notrelevant = notrelevant.set_index('Frage 6')
            notrelevant[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('Non-automotive')
        plt.ylabel(vector['y_label'])
    else:
        pass
else:
    pass

if ii == 2 or ii == 3:
    fig, axes = plt.subplots(ii, 1)
    kk = 0
    if flag[0] == 1:
        if aufteitung == 'Frage 1':
            oem = oem.set_index('Frage 1')
            oem[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            vw = vw.set_index('Frage 6')
            vw[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('OEM')
        plt.ylabel(vector['y_label'])
        kk = kk + 1
    else: 
        pass
        
    if flag[1] == 1:

        if aufteitung == 'Frage 1':
            tier1 = tier1.set_index('Frage 1')
            tier1[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            bmw = bmw.set_index('Frage 6')
            bmw[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('TIER 1')
        plt.ylabel(vector['y_label'])
        kk = kk + 1
    else:
        pass

    if flag[2] == 1:
        if aufteitung == 'Frage 1':
            tier2 = tier2.set_index('Frage 1')
            tier2[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            others = others.set_index('Frage 6')
            others[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('TIER 2')
        plt.ylabel(vector['y_label'])
        kk = kk +  1
    else:
        pass

    if flag[3] == 1:
        if aufteitung == 'Frage 1':
            na = na.set_index('Frage 1')
            na[vector['question']].plot(kind= vector['kind'])
        elif aufteitung == 'Frage 6':
            notrelevant = notrelevant.set_index('Frage 6')
            notrelevant[vector['question']].plot(kind= vector['kind'])
        plt.xticks(rotation = 45)
        plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
        plt.title('Non-automotive')
        plt.ylabel(vector['y_label'])
    else:
        pass

if ii == 4:
    fig, axes = plt.subplots(2, 2)
    if aufteitung == 'Frage 1':
        oem = oem.set_index('Frage 1')
        oem[vector['question']].plot(kind= vector['kind'])
    elif aufteitung == 'Frage 6':
        vw = vw.set_index('Frage 6')
        vw[vector['question']].plot(kind= vector['kind'])
   # ax.set_title('OEM')
    plt.xticks(rotation = 45)
    plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
    #plt.title('OEM')
    plt.ylabel(vector['y_label'])

    if aufteitung == 'Frage 1':
        tier1 = tier1.set_index('Frage 1')
        tier1[vector['question']].plot(kind= vector['kind'])
    elif aufteitung == 'Frage 6':
        bmw = bmw.set_index('Frage 6')
        bmw[vector['question']].plot(kind= vector['kind'])
    plt.xticks(rotation = 45)
    plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
    plt.title('TIER 1')
    plt.ylabel(vector['y_label'])

    if aufteitung == 'Frage 1':
        tier2 = tier2.set_index('Frage 1')
        tier2[vector['question']].plot(kind= vector['kind'])
    elif aufteitung == 'Frage 6':
        others = others.set_index('Frage 6')
        others[vector['question']].plot(kind= vector['kind'])
    plt.xticks(rotation = 45)
    plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
    plt.title('TIER 2')
    plt.ylabel(vector['y_label'])
 
    if aufteitung == 'Frage 1':
        na = na.set_index('Frage 1')
        na[vector['question']].plot(kind= vector['kind'])
    elif aufteitung == 'Frage 6':
        notrelevant = notrelevant.set_index('Frage 6')
        notrelevant[vector['question']].plot(kind= vector['kind'])
    plt.xticks(rotation = 45)
    plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
    plt.title('Non-automotive')
    plt.ylabel(vector['y_label'])    
else:
    pass

plt.show()




