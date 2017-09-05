# -*- coding: iso-8859-15 -*-
#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import PyQt5 as pq4
import matplotlib.gridspec as gridspec

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

color_map = ['blue', 'red', 'green', 'orange', 'purple', 'pink', 'brown', 'yellow', 'magenta', 'gray']
#dictionaries for each plot
aufteilung = 'Frage 1' #or Frage 6 - gives the macroset
frage = 'Frage 33' #input
##TODO CHANGE THE Y LABELS
if aufteilung == 'Frage 1':
    question_dict = {
                    'Frage 7': {'question': 'Frage 7', 'labels': ['kleiner 10', '11 - 25', '26 - 50', '51 - 75', '75 - 100', ' groesser 100'], 'y_axis' : [ 1, 2, 3, 4, 5, 6], 'kind' : 'bar', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie gross war Projektteam?'},
                    'Frage 9': {'question': 'Frage 9', 'labels': ['Nein', 'Ja', 'Wenn ja, findet Anwendung in Projekt'], 'y_axis' : [0, 1, 2], 'kind' : 'pie', 'y_label' : 'Teamgroesse','supertitle': 'Gibt es einen PEP?/ Kommunikation im Projekt?'},
                    'Frage 13': {'question': 'Frage 13', 'labels': ['PL, TPL, SW-HW PL', 'PL, SW-HW PL', 'nur PL oder TPL', 'Programmmanager, PL, SW-HW','andere Rollen' ], 'y_axis' : [1, 2, 3, 4, 5], 'kind' : 'bar', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie ist die Organisationsstruktur im Projekt (PL, TPL,SWPL, Programmmanager, etc)?'},
                    'Frage 14': {'question': 'Frage 14', 'labels': ['keine', 'MS Project', 'RPlan', 'Excel'], 'y_axis' : [1, 2, 3, 4], 'kind' : 'bar','y_label' : 'Teamgroesse', 'supertitle': 'Welche Tools wurden von PM genutzt? (Gibt es Schnittstellen von Tools?)'},
                    'Frage 15': {'question': 'Frage 15', 'labels': ['Nein', 'Ja', 'Kundengetrieben', 'Ja, interne Vorgaben'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Gibt es eine Detailplanung? (Wenn ja, wie umfangreich/detailiiert?)Wann plant ihr im Detail? Wie lange vor Meilenstein?' },
                    'Frage 18': {'question': 'Frage 18', 'labels': ['gar nicht', 'in MS Project geplant', 'in MS Project geplant und getrackt', 'in anderem Tool geplant', 'in anderem Tool geplant und getrackt'], 'y_axis' : [0, 1, 2, 3, 4], 'kind' : 'pie','y_label' : 'Teamgroesse', 'supertitle': 'Wo werden Resourcen geplant und getrackt?' },
                    'Frage 19': {'question': 'Frage 19', 'labels':  ['gar nicht', 'in SAP geplant','in SAP geplant and getrackt', 'in anderem Tool geplant', 'in anderem Tool geplant und getrackt'], 'y_axis' : [ 0, 1, 2, 3,  4], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wo werden Kosten geplant und getrackt?' },
                    'Frage 20': {'question': 'Frage 20', 'labels': ['gar nicht', 'ueber Versionierung', 'ueber Baseline', 'Versionierung und Baseline'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : 'Teamgroesse', 'supertitle': 'Wie wird dokumentiert ihr Aenderungen im Terminplan?' },
                    'Frage 24a': {'question': 'Frage 24a', 'labels': [0, 1, 2, 3, 4, 5, 6], 'y_axis' : [0, 1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?) : Anzahl regelmeetings'},
                    'Frage 24b': {'question': 'Frage 24b', 'labels': ['unknown','Teammeeting', 'Teammeeting und Standupmeeting', 'Teammeeting und Kundenmeeting', 'Team, Kunde- und Kundenmeeting', 'Standup, Team, weitere interne Meetings', 'Team, Kunde, weitere interne Meetings' ], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?)' },
                    'Frage 26': {'question': 'Frage 26', 'labels': ['keine', 'Projektplaene', 'Termin- und Porjektplaene','Terminplan, Projektplan, PM Plan, Projekthandbuch', 'zahlreiche PM Dokumente'], 'y_axis' : [0,1, 2, 3, 4], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Dokumente fuer PM als Firmentemplates oder Projektverantwortung? (WP liste, gener. Terminplan..)' },
                    'Frage 32': {'question': 'Frage 32', 'labels': ['Matrix', 'Linie', 'Matrix und Linie', 'Projektorga'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie ist in dieser Firma PM organisatorisch aufgestellt (Linie, Matrix, etc)?' },
                    'Frage 33': {'question': 'Frage 33', 'labels': ['Nein', 'Ja, erstellen Templates und Porzesse', 'andere Funktion'], 'y_axis' : [0, 1 ,2], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Gibt es PMO?' },            
                    }
elif aufteilung == 'Frage 6':
    question_dict = {
                    'Frage 10': {'question': 'Frage 10', 'labels': ['bis 25', '26-30', '31-35', '36-40', '41-45', '46-50', '>50'], 'y_axis' : [1, 2, 3, 4, 5, 6, 7], 'kind' : 'bar', 'y_label' : 'Monate', 'supertitle': 'Monate bis 1. SOP (ausrechnen)', 'supertitle': 'Monate bis 1. SOP (ausrechnen)'},
                    'Frage 12a': {'question': 'Frage 12a', 'labels': ['keine', 'OEM Schnittstelle PM', 'OEM Schnittstelle', 'OEM Schnittstellen zu vielen'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Gab es Schnittstellen (intern/extern OEM) die mitbetreut wurden? ' },
                    'Frage 15': {'question': 'Frage 15', 'labels': ['Nein', 'Ja', 'Kundengetrieben', 'Ja, interne Vorgaben'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Gibt es eine Detailplanung? (Wenn ja, wie umfangreich/detailiiert?)Wann plant ihr im Detail? Wie lange vor Meilenstein?' },
                    'Frage 16': {'question': 'Frage 16', 'labels': ['Nein', 'Ja', 'von OEN vorgegeben', 'eigene Planung'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : 'Teamgroesse', 'supertitle': 'Gibt es einen Feature Releaseplan? Wenn ja, in welcher Form'},
                    'Frage 20': {'question': 'Frage 20', 'labels': ['gar nicht', 'ueber Versionierung', 'ueber Baseline', 'Versionierung und Baseline'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : 'Teamgroesse', 'supertitle': 'Wie wird dokumentiert ihr Aenderungen im Terminplan?' },
                    'Frage 21': {'question': 'Frage 21', 'labels': ['gar nicht', 'ueber Versionierung', 'ueber Baselinie', 'ueber Spalte in Plan', 'automatisiert'], 'y_axis' : [0, 1, 2, 3, 4], 'kind' : 'pie','y_label' : 'Teamgroesse', 'supertitle': 'Werden IST/Soll Abweichungen in der Projektplanung dargestellt?' },
                    'Frage 24a': {'question': 'Frage 24a', 'labels': [0, 1, 2, 3, 4, 5, 6], 'y_axis' : [0, 1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?) : Anzahl regelmeetings'},
                    'Frage 24b': {'question': 'Frage 24b', 'labels': ['unknown','Teammeeting', 'Teammeeting und Standupmeeting', 'Teammeeting und Kundenmeeting', 'Team, Kunde- und Kundenmeeting', 'Standup, Team, weitere interne Meetings', 'Team, Kunde, weitere interne Meetings' ], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?)' },
                      }

vector = question_dict[frage]    

#size of the team
flag = [ 0, 1, 1, 1]
ii = flag.count(1)
rot = 70



#TODO change the labels for each entry in the dictionary


if vector['kind'] ==  'bar':
    if ii == 1:
        if flag[0] == 1:
            plt.suptitle(vector['supertitle'])
            if aufteilung == 'Frage 1':
                oem = oem.set_index('Frage 1')
                #oem[vector['question']].plot(kind = vector['kind'] )
                #plt.title('OEM')
            #oem = oem.set_index('Frage 1')
                x = oem[vector['question']].plot(kind = vector['kind'] )
                x.set_title('OEM')
            elif aufteilung == 'Frage 6':
                vw = vw.set_index('Frage 6')
                vw[vector['question']].plot(kind= vector['kind'])
                plt.title('VW')
            plt.xticks(rotation = 45)
            plt.yticks(vector['y_axis'], rotation = 'horizontal')
            x.set_yticklabels(vector['labels'])
            #x.set_yticklabels(vector['y_label'])
            x.set_xlabel("Firma")
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
                   
        else: 
            pass


        if flag[1] == 1:
            if aufteilung == 'Frage 1':
                plt.suptitle(vector['supertitle'])
                tier1 = tier1.set_index('Frage 1')
                tier1[vector['question']].plot(kind= vector['kind'])
                plt.title('TIER 1')
            elif aufteilung == 'Frage 6':
                bmw = bmw.set_index('Frage 6')
                bmw[vector['question']].plot(kind= vector['kind'])
                plt.title('BMW')
            plt.xticks(rotation = 45)
            plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
            plt.ylabel(vector['y_label'])
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()        
        else:
            pass

        if flag[2] == 1:
            plt.suptitle(vector['supertitle'])
            if aufteilung == 'Frage 1':
                tier2 = tier2.set_index('Frage 1')
                tier2[vector['question']].plot(kind= vector['kind'])
                plt.title('TIER 2')
            elif aufteilung == 'Frage 6':
                others = others.set_index('Frage 6')
                others[vector['question']].plot(kind= vector['kind'])
                plt.title('OTHERS')
            plt.xticks(rotation = 45)
            plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
            plt.ylabel(vector['y_label'])
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
        else:
            pass

        if flag[3] == 1:
            plt.suptitle(vector['supertitle'])
            if aufteilung == 'Frage 1':
                na = na.set_index('Frage 1')
                na[vector['question']].plot(kind= vector['kind'])
                plt.title('Non-automotive')
            elif aufteilung == 'Frage 6':
                notrelevant = notrelevant.set_index('Frage 6')
                notrelevant[vector['question']].plot(kind= vector['kind'])
                plt.title('Not relevant')
            plt.xticks(rotation = 45)
            plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal')
            plt.ylabel(vector['y_label'])
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
        else:
            pass
    else:
        pass

    if ii == 2 or ii == 3:
        fig, axes = plt.subplots(ii, 1)   
 
        plt.suptitle(vector['supertitle'])
        plt.tight_layout()
        kk = 0
        if flag[0] == 1:
            if aufteilung == 'Frage 1':
                oem = oem.set_index( 'Frage 1')
                x1 = oem[vector['question']].plot( ax = axes[kk], kind = vector['kind'], color = 'red')
                x1.set_title('OEM')
            elif aufteilung == 'Frage 6':
                vw = vw.set_index('Frage 6')
                x1 = vw[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'red')
                x1.set_title('VW')
            else:
                pass
            plt.setp(x1.get_xticklabels(), rotation = rot)
            x1.set_yticks(vector['y_axis'])
            x1.set_yticklabels(vector['labels'])
            x1.set_ylabel(vector['y_label'])
            x1.set_xlabel('')
            kk = kk + 1
        else: 
            pass
            
        if flag[1] == 1:
            if aufteilung == 'Frage 1':
                tier1 = tier1.set_index('Frage 1')
                x2 = tier1[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'blue')
                x2.set_title('TIER 1')
            elif aufteilung == 'Frage 6':
                bmw = bmw.set_index('Frage 6')
                x2 = bmw[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'blue')
                x2.set_title('BMW')
            else:
                pass
            plt.setp(x2.get_xticklabels(), rotation = rot)
            x2.set_yticks(vector['y_axis'])
            x2.set_yticklabels(vector['labels'])
            x2.set_ylabel(vector['y_label'])
            x2.set_xlabel('')
            kk = kk + 1
        else:
            pass

        if flag[2] == 1:
            if aufteilung == 'Frage 1':
                tier2 = tier2.set_index('Frage 1')
                x3 = tier2[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'green')
                plt.title('TIER 2')
            elif aufteilung == 'Frage 6':
                others = others.set_index('Frage 6')
                x3 = others[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'green')
                x3.set_title('Others')
            plt.setp(x3.get_xticklabels(), rotation = rot)
            x3.set_yticks(vector['y_axis'])
            x3.set_yticklabels(vector['labels'])
            x3.set_ylabel(vector['y_label'])
            x3.set_xlabel('')
            kk = kk +  1
        else:
            pass

        if flag[3] == 1:
            if aufteilung == 'Frage 1':
                na = na.set_index('Frage 1')
                x4 = na[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'purple')
                plt.title('Non-automotive')
            elif aufteilung == 'Frage 6':
                notrelevant = notrelevant.set_index('Frage 6')
                x4 = notrelevant[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'purple')
                x4.set_title('Not relevant')
            plt.setp(x4.get_xticklabels(), rotation = rot)
            x4.set_yticks(vector['y_axis'])
            x4.set_yticklabels(vector['labels'])
            x4.set_ylabel(vector['y_label'])
            x4.set_xlabel('')
        
                
        else:
            pass

        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()   
        if ii == 2:
            plt.subplots_adjust(top=0.92, bottom=0.11, left=0.12, right=0.89, hspace=0.71, wspace=0.2)
        elif ii == 3:
            plt.subplots_adjust(top=0.93, bottom=0.10, left=0.20, right=0.80, hspace=0.68, wspace=0.15)
        else:
            pass
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()

    if ii == 4:
        fig, axes = plt.subplots(2, 2)
        plt.suptitle(vector['supertitle'])
        plt.tight_layout()
        rot = 60
        if aufteilung == 'Frage 1':
            oem = oem.set_index('Frage 1')
            x1 = oem[vector['question']].plot(ax = axes[0,0], kind= vector['kind'], color = 'red')
            x1.set_title('OEM')
        elif aufteilung == 'Frage 6':
            vw = vw.set_index('Frage 6')
            x1 = vw[vector['question']].plot(ax = axes[0,0], kind= vector['kind'],color = 'red')
            x1.set_title('VW')
        plt.setp(x1.get_xticklabels(), rotation = rot)
        x1.set_yticks(vector['y_axis'])
        x1.set_yticklabels(vector['labels'])
        x1.set_ylabel(vector['y_label'])
        x1.set_xlabel('')

        if aufteilung == 'Frage 1':
            tier1 = tier1.set_index('Frage 1')
            x2 = tier1[vector['question']].plot(ax = axes[0,1], kind= vector['kind'], color = 'blue')
            plt.title('TIER 1')
        elif aufteilung == 'Frage 6':
            bmw = bmw.set_index('Frage 6')
            x2 = bmw[vector['question']].plot(ax = axes[0,1], kind= vector['kind'],color = 'blue')
            x2.set_title('BMW')
        plt.setp(x2.get_xticklabels(), rotation=rot)
        x2.set_yticks(vector['y_axis'])
        x2.set_yticklabels(vector['labels'])
        x2.set_ylabel(vector['y_label'])
        x2.set_xlabel('')
    

        if aufteilung == 'Frage 1':
            tier2 = tier2.set_index('Frage 1')
            x3 = tier2[vector['question']].plot(ax = axes[1,0], kind= vector['kind'], color = 'green')
            x3.set_title('Tier 2')
        elif aufteilung == 'Frage 6':
            others = others.set_index('Frage 6')
            x3 = others[vector['question']].plot(ax = axes[1, 0], kind= vector['kind'], color = 'green')
            x3.set_title('Others')
        plt.setp(x3.get_xticklabels(), rotation=rot)
        x3.set_yticks(vector['y_axis'])
        x3.set_yticklabels(vector['labels'])
        x3.set_ylabel(vector['y_label'])
        x3.set_xlabel('')
    
        if aufteilung == 'Frage 1':
            na = na.set_index('Frage 1')
            x4 = na[vector['question']].plot(ax = axes[1,1], kind= vector['kind'],color = 'purple')
            x4.set_title('Non-automotive')
        elif aufteilung == 'Frage 6':
            notrelevant = notrelevant.set_index('Frage 6')
            x4 = notrelevant[vector['question']].plot(ax = axes[1,1], kind= vector['kind'], color = 'purple')
            x4.set_title('Not relevant')
        plt.setp(x4.get_xticklabels(), rotation=rot)
        x4.set_yticks(vector['y_axis'])
        x4.set_yticklabels(vector['labels'])
        x4.set_ylabel(vector['y_label'])
        x4.set_xlabel('')
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.subplots_adjust(top=0.92, bottom=0.08, left=0.04, right=0.97, hspace=0.50, wspace=0.15)   
    else:
        pass
    plt.show()

#Processing of the pie charts
    
  
elif vector['kind'] ==  'pie':
    if ii == 1:
        plt.subplots_adjust(top=0.90, bottom=0.03, left=0.24, right=0.76, hspace=0.20, wspace=0.20) 
        if flag[0] == 1:
            if aufteilung == 'Frage 1':
                oem = oem.set_index('Frage 1')
                filter = oem[vector['question']]
                plt.title('OEM')                  
            elif aufteilung == 'Frage 6':
                vw = vw.set_index('Frage 1')
                filter = vw[vector['question']] 
                plt.title('VW')              
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()
            labels = [int(i) for i in labels]           
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            draft = plt.pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            plt.suptitle(vector['supertitle'])
            plt.legend(labels, loc = 'lower right')
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
            plt.show()      
        else: 
            pass

        if flag[1] == 1:
            if aufteilung == 'Frage 1':
                tier1 = tier1.set_index('Frage 1')
                filter = tier1[vector['question']]
                plt.title('Tier 1')    
            elif aufteilung == 'Frage 6':
                bmw = bmw.set_index('Frage 1')
                filter = bmw[vector['question']]
                plt.title('BMW')              
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()
            labels = [int(i) for i in labels]           
            total = sum(values)
            labels_tst = vector['labels']
            labels = [int(i) for i in labels]
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]    
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]
            draft = plt.pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            plt.suptitle(vector['supertitle'])
            plt.legend(labels, loc = 'lower right')
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
            plt.show()      
        else: 
            pass

        if flag[2] == 1:
            if aufteilung == 'Frage 1':
                tier2 = tier2.set_index('Frage 1')
                filter = tier2[vector['question']]
                plt.title('Tier 2')    
            elif aufteilung == 'Frage 6':
                others = others.set_index('Frage 1')
                filter = others[vector['question']] 
                plt.title('Others')             
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()           
            total = sum(values)
            labels_tst = vector['labels']
            labels = [int(i) for i in labels]
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels] 
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            draft = plt.pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            plt.suptitle(vector['supertitle'])
            plt.legend(labels, loc = 'lower right')
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
            plt.show()      
        else: 
            pass


        if flag[3] == 1:
            if aufteilung == 'Frage 1':
                na = na.set_index('Frage 1')
                filter = na[vector['question']] 
                plt.title('Non-automotive')   
            elif aufteilung == 'Frage 6':
                notrelevant = notrelevant.set_index('Frage 1')
                filter = notrelevant[vector['question']]
                plt.title('Not relevant')              
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()           
            total = sum(values)
            labels_tst = vector['labels']
            labels = [int(i) for i in labels]
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels] 
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            draft = plt.pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            plt.suptitle(vector['supertitle'])
            plt.legend(labels, loc = 'lower right')
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()
            plt.show()      
        else: 
            pass
    
    elif ii == 2 or ii == 3:
        fig, axes = plt.subplots(1, ii)
        if ii == 2:
            plt.subplots_adjust(top=0.91, bottom=0.08, left=0.01, right=0.97, hspace=0.18, wspace=0.0)
        elif ii == 3:
            plt.subplots_adjust(top=0.83, bottom=0.26, left=0.02, right=0.98, hspace=0.0, wspace=0.0)
        else:
            pass                                    
        plt.suptitle(vector['supertitle'])
        #plt.tight_layout()
        #    
        #x1 = oem[vector['question']].plot( ax = axes[kk], kind = vector['kind'], color = 'red')
        kk = 0
        if flag[0] == 1:           
            if aufteilung == 'Frage 1':
                oem = oem.set_index('Frage 1')
                filter = oem[vector['question']]
                axes[kk].set_title('OEM')                 
            elif aufteilung == 'Frage 6':
                vw = vw.set_index('Frage 1')
                filter = vw[vector['question']]
                axes[kk].set_title('VW')               
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()           
            total = sum(values)
            labels_tst = vector['labels']
            labels = [int(i) for i in labels]
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
           # draft = plt.pie(values, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[kk].pie(values, colors = color_map_local,  autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[kk].legend(labels, loc = 'lower right')                     
            kk = kk + 1 
        else: 
            pass

        if flag[1] == 1:
            #plt.subplot(the_grid(0,1), aspect = 1)
            if aufteilung == 'Frage 1':
                tier1 = tier1.set_index('Frage 1')
                filter = tier1[vector['question']] 
                axes[kk].set_title('Tier 1')   
            elif aufteilung == 'Frage 6':
                bmw = bmw.set_index('Frage 1')
                filter = bmw[vector['question']]              
                axes[kk].set_title('BMW') 
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()    
            labels = [int(i) for i in labels]     
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]            
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            #draft = plt.pie(values, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[kk].pie(values, colors = color_map_local,  autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[kk].legend(labels, loc = 'lower right')
            kk = kk + 1 
        else: 
            pass

        if flag[2] == 1:
            if aufteilung == 'Frage 1':
                tier2 = tier2.set_index('Frage 1')
                filter = tier2[vector['question']]
                axes[kk].set_title('Tier 2')     
            elif aufteilung == 'Frage 6':
                others = others.set_index('Frage 1')
                filter = others[vector['question']]
                axes[kk].set_title('Others')               
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()
            labels = [int(i) for i in labels]           
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            axes[kk].pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[kk].legend(labels, loc = 'lower right')  
            kk = kk + 1 
        else: 
            pass

        if flag[3] == 1:
            #plt.subplot(the_grid(1, 1), aspect = 1)
            if aufteilung == 'Frage 1':
                na = na.set_index('Frage 1')
                filter = na[vector['question']] 
                axes[kk].set_title('Non-automotive')    
            elif aufteilung == 'Frage 6':
                notrelevant = notrelevant.set_index('Frage 1')
                filter = notrelevant[vector['question']]
                axes[kk].set_title('Not relevant')               
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist() 
            labels = [int(i) for i in labels]          
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[0:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            axes[kk].pie(values, colors = color_map_local,  autopct=lambda(p): '{:.0f}'.format(p * total / 100))  
            axes[kk].legend(labels, loc = 'lower right')
        #plt.legend(labels) 
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()        
        plt.show()
    elif ii == 4:
        fig, axes = plt.subplots(2, 2, sharey = True)                      
        plt.suptitle(vector['supertitle'])
        #fig.legend(labels, (axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]), 'center') 
        plt.tight_layout()
        if flag[0] == 1:           
            if aufteilung == 'Frage 1':
                oem = oem.set_index('Frage 1')
                filter = oem[vector['question']]
                axes[0, 0].set_title('OEM')                 
            elif aufteilung == 'Frage 6':
                vw = vw.set_index('Frage 1')
                filter = vw[vector['question']]
                axes[0 ,0].set_title('VW')               
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()
            labels = [int(i) for i in labels]           
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
           # draft = plt.pie(values, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[0, 0].pie(values,  colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[0, 0].legend(labels, loc = 'lower right')                     
             
        else: 
            pass

        if flag[1] == 1:
            #plt.subplot(the_grid(0,1), aspect = 1)
            if aufteilung == 'Frage 1':
                tier1 = tier1.set_index('Frage 1')
                filter = tier1[vector['question']] 
                axes[0, 1].set_title('Tier 1')   
            elif aufteilung == 'Frage 6':
                bmw = bmw.set_index('Frage 1')
                filter = bmw[vector['question']]              
                axes[0, 1].set_title('BMW') 
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()
            labels = [int(i) for i in labels]           
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            #draft = plt.pie(values, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[0, 1].pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[0, 1].legend(labels, loc = 'lower right')
            
        else: 
            pass

        if flag[2] == 1:
            # plt.subplot(the_grid(1,0), aspect = 1)
            if aufteilung == 'Frage 1':
                tier2 = tier2.set_index('Frage 1')
                filter = tier2[vector['question']]
                axes[1 ,0].set_title('Tier 2')     
            elif aufteilung == 'Frage 6':
                others = others.set_index('Frage 1')
                filter = others[vector['question']]
                axes[1, 0].set_title('Others')               
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist() 
            labels = [int(i) for i in labels]          
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            axes[1, 0].pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))
            axes[1, 0].legend(labels, loc = 'lower right')  
             
        else: 
            pass

        if flag[3] == 1:
            #plt.subplot(the_grid(1, 1), aspect = 1)
            if aufteilung == 'Frage 1':
                na = na.set_index('Frage 1')
                filter = na[vector['question']] 
                axes[1, 1].set_title('Non-automotive')    
            elif aufteilung == 'Frage 6':
                notrelevant = notrelevant.set_index('Frage 1')
                filter = notrelevant[vector['question']]
                axes[1, 1].set_title('Not relevant')               
            else:
                pass
            map = filter.value_counts().reset_index()
            values =  map[vector['question']].tolist()
            labels = map['index'].tolist()  
            labels = [int(i) for i in labels]         
            total = sum(values)
            labels_tst = vector['labels']
            color_map_local = color_map[:len(labels)]
            color_map_local = [color_map[ii] for ii in labels]
            for idx in labels:
                labels[labels.index(idx)] = labels_tst[int(idx)]     
            axes[1, 1].pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100))  
            axes[1, 1].legend(labels, loc = 'lower right')
        #plt.legend(labels, handles = [axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]], loc= "center")
        #fig.legend(labels, (x0, x1, x2, x3), 'center')
        plt.subplots_adjust(top=0.91, bottom=0.02, left=0.21, right=0.80, hspace=0.05, wspace=0.32)
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()         
        plt.show()

    else: 
        pass         
                

else:
    pass
