import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
#import the module created in the qtdesigner
from dialog1 import Ui_InitalDialog
from dialog2 import Ui_Dialog2
from dialog3 import Ui_Dialog3

import pandas as pd #pandas for data analytics
import matplotlib.pyplot as plt #matplotlib for visualization


#Dropdown of AppWindow1
AW11="In welchen Firmen hattest du dein Projekt (Branche/OEM/Tier1,2,3)?"
AW12='Wer ist der Kunde?'
showTrigger = 1 #Show AppWindow1
#Flagcheckbox


#Main window
class AppWindow1(QDialog):
    def __init__(self, parent=None):
        super(AppWindow1, self).__init__()
        #Set up interface from designer
        self.ui = Ui_InitalDialog()
        self.ui.setupUi(self)
        #Connect to buttons
        self.ui.PushButton1ok.clicked.connect(self.decision)
        #load GUI
        self.show()
        
    def decision(self):
        text_decision = str(self.ui.comboBox1.currentText())
        global aufteilung 
        if text_decision == AW11:
            
            aufteilung = 'Frage 1'
            self.hide()
            self.QDialog = AppWindow2(self)
            #print aufteilung
            #return aufteilung
        elif text_decision == AW12:
            self.hide()
            self.QDialog = AppWindow3(self)
            aufteilung = 'Frage 6'
            #return aufteilung
            #print aufteilung
        else:        
            return 
        
#Window if the following response is selected by AppWindow1
#In welchen Firmen hattest du dein Projekt (Branche/OEM/Tier1,2,3)?
class AppWindow2(QDialog):
    def __init__(self, parent=None):
        super(AppWindow2, self).__init__()
        #Set up interface from designer
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        #Connect to buttons
        self.ui.PlotButton2.clicked.connect(self.plot2)
        self.ui.backButton2.clicked.connect(self.back2)
        #load GUI
        self.show()

    def plot2(self):
        #Question
        global frage
        frage = str(self.ui.comboBox2.currentText())
        #print frage
        global flag 
        flag = [0, 0, 0, 0]

        #get flags if checked self.ui.checkBox31.isChecked() = True
        #starts with a zero [0 x x x x]
        if self.ui.checkBox21.isChecked():
            flag[0] = 1
        else:
            flag[0] = 0
        if self.ui.checkBox22.isChecked():
            flag[1] = 1
        else:
            flag[1] = 0
        if self.ui.checkBox23.isChecked():
            flag[2] = 1  
        else:
            flag[2] = 0         
        if self.ui.checkBox24.isChecked():
            flag[3] = 1
        else:
            flag[3] = 0
        #print flag
        #print aufteilung  

        def my_print_1() : printing() 

        my_print_1()   

    def back2(self):
        self.hide()
        self.QDialog = AppWindow1(self)
    
#Window if the following response is selected by AppWindow1
#Wer ist der Kunde?
class AppWindow3(QDialog):
    def __init__(self, parent=None):
        super(AppWindow3, self).__init__()
        #Set up interface from designer
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        #Connect to buttons
        self.ui.PlotButton3.clicked.connect(self.plot3)
        self.ui.backButton3.clicked.connect(self.back3)
        #load GUI
        self.show()

    def plot3(self):

        #Question
        global frage
        frage = str(self.ui.comboBox3.currentText())
        #print frage
        global flag
        flag = [0, 0, 0, 0]
        #get flags if checked self.ui.checkBox31.isChecked() = True
        if self.ui.checkBox31.isChecked():
            flag[0] = 1
        else:
            flag[0] = 0
        if self.ui.checkBox32.isChecked():
            flag[1] = 1
        else:
            flag[1] = 0
        if self.ui.checkBox33.isChecked():
            flag[2] = 1  
        else:
            flag[2] = 0         
        if self.ui.checkBox34.isChecked():
            flag[3] = 1
        else:
            flag[3] = 0
        #print flag
        #print aufteilung

        def my_print_2() : printing() 
        my_print_2() 



    def back3(self):
        self.hide()
        self.QDialog = AppWindow1(self)


def printing():
    #importing the sheet content as a pandas data frame
    #path is local folder and the sheet name is set according to the document
    df1 = pd.read_excel(open('./local.xlsx', 'rb'), decoding = 'utf-8', sheetname = 'Planilha2')
    df = df1.sort_values('Frage 1') #sort values to have them in alphabetic order

    #segregating the OEM group
    oem = df.loc[df['Frage 1'].isin(['Ford', 'BMW'])]
    #segregating the Tier1 group
    tier1 = df.loc[df['Frage 1'].isin(['Conti', 'Conti Reg','Conti  Babenhausen', 'TRW', 'TRW DUeS', 'TRW Sherly',"TRW Ko", "Hella","Hella Lippstadt", "ZF Sachs","DRX BOeB", "Bosch Schwaebisch Gmuend", "Webasto","Bombardier -Primove", "Draexelmaier Interior", "Peiker"])]
    #segregating the Tier2 group
    tier2 = df.loc[df['Frage 1'].isin(['Renesas DUeS', 'Renesas', 'Perei'])]
    #segregating the Non-Automotive group
    na = df.loc[df['Frage 1'].isin(['Bosch- eBike Systems', 'Franki Gundbau', 'Soehner'])]
    # second segmentations (VW, BMW, Others, Not Relevant)
    #segregating the VW group
    vw = df.loc[df['Frage 6'].isin(['VW Konzern', 'Porsche /VW', 'VW', 'Audi', 'Porsche', 'Audi, VW, Seat Porsche'])]
    #segregating the BMW group
    bmw = df.loc[df['Frage 6'].isin(['BMW'])]
    #segregating the Others group
    others = df.loc[df['Frage 6'].isin(['Daimler', 'Fiat', 'viele OEMS', 'Evobus', 'PSA', 'Honda/GM'])]
    #segregating the NotRelevant group
    notrelevant = df.loc[df['Frage 6'].isin(['Eigenentwicklung, kein OEM, aber Fahrradhersteller geben Features vor', 'Hella', 'Eigenentwicklung / Marketing als Kunde', 'Franki Gundbau'])]

    #color map is declared for making the colors in the pie chart plots consistent
    color_map = ['blue', 'red', 'green', 'orange', 'purple', 'pink', 'brown', 'yellow', 'magenta', 'gray']
    
    #aufteilung = 'Frage 1' #or Frage 6 - gives the macroset
    ##frage = 'Frage 33' #input
    #dictionary for each plot - has the custom featues for each plot associated to the kez (name of the plot)
    #there are two versions of the dictionary, each one dependent of which data segmentation we use (this case either question 1 or 6)
    if aufteilung == 'Frage 1':
        question_dict = {
                        'Teamgroese': {'question': 'Frage 7', 'labels': ['kleiner 10', '11 - 25', '26 - 50', '51 - 75', '75 - 100', ' groesser 100'], 'y_axis' : [ 1, 2, 3, 4, 5, 6], 'kind' : 'bar', 'y_label' : 'Teamgroesse', 'supertitle': 'Wie gross war Projektteam?'},
                        'PEP': {'question': 'Frage 9', 'labels': ['Nein', 'Ja', 'Wenn ja, findet Anwendung in Projekt'], 'y_axis' : [0, 1, 2], 'kind' : 'pie', 'y_label' : '','supertitle': 'Gibt es einen PEP?/ Kommunikation im Projekt?'},
                        'Struktur': {'question': 'Frage 13', 'labels': ['PL, TPL, SW-HW PL', 'PL, SW-HW PL', 'nur PL oder TPL', 'Programmmanager, PL, SW-HW','andere Rollen' ], 'y_axis' : [1, 2, 3, 4, 5], 'kind' : 'bar', 'y_label' : 'Organisationsstruktur', 'supertitle': 'Wie ist die Organisationsstruktur im Projekt (PL, TPL,SWPL, Programmmanager, etc)?'},
                        'Tools': {'question': 'Frage 14', 'labels': ['keine', 'MS Project', 'RPlan', 'Excel'], 'y_axis' : [1, 2, 3, 4], 'kind' : 'bar','y_label' : 'Tools', 'supertitle': 'Welche Tools wurden von PM genutzt? (Gibt es Schnittstellen von Tools?)'},
                        'Detailplanung': {'question': 'Frage 15', 'labels': ['Nein', 'Ja', 'Kundengetrieben', 'Ja, interne Vorgaben'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Gibt es eine Detailplanung? (Wenn ja, wie umfangreich/detailiiert?)Wann plant ihr im Detail? Wie lange vor Meilenstein?' },
                        'Ressourcenplanung': {'question': 'Frage 18', 'labels': ['gar nicht', 'in MS Project geplant', 'in MS Project geplant und getrackt', 'in anderem Tool geplant', 'in anderem Tool geplant und getrackt'], 'y_axis' : [0, 1, 2, 3, 4], 'kind' : 'pie','y_label' : '', 'supertitle': 'Wo werden Resourcen geplant und getrackt?' },
                        'Kostenplanung': {'question': 'Frage 19', 'labels':  ['gar nicht', 'in SAP geplant','in SAP geplant and getrackt', 'in anderem Tool geplant', 'in anderem Tool geplant und getrackt'], 'y_axis' : [ 0, 1, 2, 3,  4], 'kind' : 'pie', 'y_label' : 'Teamgroesse', 'supertitle': 'Wo werden Kosten geplant und getrackt?' },
                        'Aenderungen': {'question': 'Frage 20', 'labels': ['gar nicht', 'ueber Versionierung', 'ueber Baseline', 'Versionierung und Baseline'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : '', 'supertitle': 'Wie wird dokumentiert ihr Aenderungen im Terminplan?' },
                        'ProjektrundenA': {'question': 'Frage 24a', 'labels': [0, 1, 2, 3, 4, 5, 6], 'y_axis' : [0, 1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?) : Anzahl regelmeetings'},
                        'ProjektrundenB': {'question': 'Frage 24b', 'labels': ['unknown','Teammeeting', 'Teammeeting und Standupmeeting', 'Teammeeting und Kundenmeeting', 'Team, Kunde- und Kundenmeeting', 'Standup, Team, weitere interne Meetings', 'Team, Kunde, weitere interne Meetings' ], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?)' },
                        'Templates': {'question': 'Frage 26', 'labels': ['keine', 'Projektplaene', 'Termin- und Porjektplaene','Terminplan, Projektplan, PM Plan, Projekthandbuch', 'zahlreiche PM Dokumente'], 'y_axis' : [0,1, 2, 3, 4], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Dokumente fuer PM als Firmentemplates oder Projektverantwortung? (WP liste, gener. Terminplan..)' },
                        'Organisationsform': {'question': 'Frage 32', 'labels': ['Matrix', 'Linie', 'Matrix und Linie', 'Projektorga'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Wie ist in dieser Firma PM organisatorisch aufgestellt (Linie, Matrix, etc)?' },
                        'PMO': {'question': 'Frage 33', 'labels': ['Nein', 'Ja, erstellen Templates und Porzesse', 'andere Funktion'], 'y_axis' : [0, 1 ,2], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Gibt es PMO?' },            
                        }

    elif aufteilung == 'Frage 6':
        question_dict = {
                        'Entwicklungszeit': {'question': 'Frage 10', 'labels': ['bis 25', '26-30', '31-35', '36-40', '41-45', '46-50', '>50'], 'y_axis' : [1, 2, 3, 4, 5, 6, 7], 'kind' : 'bar', 'y_label' : 'Monate', 'supertitle': 'Monate bis 1. SOP (ausrechnen)', 'supertitle': 'Monate bis 1. SOP (ausrechnen)'},
                        'Schnittstelle': {'question': 'Frage 12a', 'labels': ['keine', 'OEM Schnittstelle PM', 'OEM Schnittstelle', 'OEM Schnittstellen zu vielen'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Gab es Schnittstellen (intern/extern OEM) die mitbetreut wurden? ' },
                        'Planung': {'question': 'Frage 15', 'labels': ['Nein', 'Ja', 'Kundengetrieben', 'Ja, interne Vorgaben'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Gibt es eine Detailplanung? (Wenn ja, wie umfangreich/detailiiert?)Wann plant ihr im Detail? Wie lange vor Meilenstein?' },
                        'Feature release': {'question': 'Frage 16', 'labels': ['Nein', 'Ja', 'von OEN vorgegeben', 'eigene Planung'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : '', 'supertitle': 'Gibt es einen Feature Releaseplan? Wenn ja, in welcher Form'},
                        'Aenderungen': {'question': 'Frage 20', 'labels': ['gar nicht', 'ueber Versionierung', 'ueber Baseline', 'Versionierung und Baseline'], 'y_axis' : [0, 1, 2, 3], 'kind' : 'pie','y_label' : '', 'supertitle': 'Wie wird dokumentiert ihr Aenderungen im Terminplan?' },
                        'Ist/Soll': {'question': 'Frage 21', 'labels': ['gar nicht', 'ueber Versionierung', 'ueber Baselinie', 'ueber Spalte in Plan', 'automatisiert'], 'y_axis' : [0, 1, 2, 3, 4], 'kind' : 'pie','y_label' : '', 'supertitle': 'Werden IST/Soll Abweichungen in der Projektplanung dargestellt?' },
                        'ProjektrundenA': {'question': 'Frage 24a', 'labels': [0, 1, 2, 3, 4, 5, 6], 'y_axis' : [0, 1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?) : Anzahl regelmeetings'},
                        'ProjektrundenB': {'question': 'Frage 24b', 'labels': ['unknown','Teammeeting', 'Teammeeting und Standupmeeting', 'Teammeeting und Kundenmeeting', 'Team, Kunde- und Kundenmeeting', 'Standup, Team, weitere interne Meetings', 'Team, Kunde, weitere interne Meetings' ], 'y_axis' : [1, 2, 3, 4, 5, 6], 'kind' : 'pie', 'y_label' : '', 'supertitle': 'Wie wurden Projektrunden gehandhabt? (Agenda?)' },
                        }
    else:  
        pass      

    #vector is a list that holds the dictionary values of the selected plot (coming from the GUI)
    vector = question_dict[frage] 
    #flag is the variable that represents which plots have been selected from the GUI
    #the variable ii holds the count of how many plots have been selected to be printed
    ii = flag.count(1)
    #rot is simple variable to generalize the rotation of the x labelticks to the bar plots
    rot = 70

    #PRINTING SESSION
    #There are two possible distinct printing subroutines namely BAR CHART PLOT and PIE CHART PLOT 
    #the kind of the plot is containg the the dictionary entry for that particular plot under the value 'kind'
    #by checkig the value of vector['kind'] we can detect which type of plot the graph has 
       
    if vector['kind'] ==  'bar': #check if the selected plot is a bar chart
        if ii == 1: #if only one plot has to be printed
            if flag[0] == 1: #check if the first plot has been selected
                plt.suptitle(vector['supertitle']) #set an overall title for the plot
                if aufteilung == 'Frage 1': #checks if we are segmenting the data based on question 1 or 6 - this case 1
                    oem = oem.set_index('Frage 1') #if so (question 1) then select oem as the data subset of interest 
                    x = oem[vector['question']].plot(kind = vector['kind'] ) #create a plot with a bar type
                    x.set_title('OEM') #set the title of the plot
                elif aufteilung == 'Frage 6': #however if the segmentation is based on the question 6
                    vw = vw.set_index('Frage 6') #make VW the subset of insterest
                    vw[vector['question']].plot(kind= vector['kind']) #plot VW as a bar chart
                    plt.title('VW') #set the title of the plot
                plt.xticks(rotation = 45) #explictly set rotation to 45 to the xlables - checked visually to see what fits best
                plt.yticks(vector['y_axis'], rotation = 'horizontal') #set the ylabels in horizontal position
                x.set_yticklabels(vector['labels']) #replace the labels with the ones from the dictionary
                x.set_xlabel("Firma") #name the x axis with Firma
                figManager = plt.get_current_fig_manager() #the two following line make the plot to show up maximized on the screen
                figManager.window.showMaximized()
                    
            else: #if the first plot hasn't been selected, simple move on 
                pass 


            if flag[1] == 1: #if the second plot has been selected
                if aufteilung == 'Frage 1': #if the segmentation was made based on the quesiton 1
                    plt.suptitle(vector['supertitle']) #read the title to the overall plot from the dictionary entry supertitle
                    tier1 = tier1.set_index('Frage 1') #make tier 1 the set of intereset and set index of the plot to be the question 1 (client)
                    tier1[vector['question']].plot(kind= vector['kind']) #plot the subset as a bar chart 
                    plt.title('TIER 1') #set the title of the subplot to tier1
                elif aufteilung == 'Frage 6': #if the segmentation was based on the question 6
                    bmw = bmw.set_index('Frage 6') #set the index to question 6 
                    bmw[vector['question']].plot(kind= vector['kind']) #plot the BMW dataframe as a bar kind
                    plt.title('BMW') #set the BMW title to the subplot
                plt.xticks(rotation = 45) #set explicitly rotation to 45 to the xticks
                plt.yticks(vector['y_axis'], vector['labels'], rotation = 'horizontal') #set horizontal rotation to the yticks
                plt.ylabel(vector['y_label']) #set ylabel to the label designinated at the dictionary
                figManager = plt.get_current_fig_manager() #make the plot open as a maximized window
                figManager.window.showMaximized()        
            else:
                pass
            #the following two subplots follow the same pattern as the two before 
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

        if ii == 2 or ii == 3: #case the number of plots selected to print is either 2 or 3, execute this subroutine
            fig, axes = plt.subplots(ii, 1)   #crate a figure with a matrix of subplots  - (2,1) or (3,1)
            plt.suptitle(vector['supertitle']) #set overall title of the whole plot 
            plt.tight_layout() #use tight layout to set up initial dimensions of the subplots
            kk = 0 #variable o iterate over the plots and print them
            if flag[0] == 1: #case the first plot has been selected
                if aufteilung == 'Frage 1': #case the segmentation as made based on the question
                    oem = oem.set_index( 'Frage 1') #set the oem subset and make quesiton one the index
                    x1 = oem[vector['question']].plot( ax = axes[kk], kind = vector['kind'], color = 'red') #plot the current subset as a bar plot color red
                    x1.set_title('OEM') #set title to OEM
                elif aufteilung == 'Frage 6': #case the segmentation is based on the question 6
                    vw = vw.set_index('Frage 6') #make the subset of interest VW and set the index to question 6
                    x1 = vw[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'red') #plot the subset as a bar char color red
                    x1.set_title('VW') #set title to VW
                else:
                    pass 
                plt.setp(x1.get_xticklabels(), rotation = rot) #set rotation to the xticks
                x1.set_yticks(vector['y_axis']) # override the ylabels
                x1.set_yticklabels(vector['labels']) #supply new labels to the yticks according to the values availabe on the dictionary
                x1.set_ylabel(vector['y_label']) #set title to the y axis
                x1.set_xlabel('') #set no title to the x axis
                kk = kk + 1 #increase the iteration variable
            else: 
                pass
                
            if flag[1] == 1: #checks for the second plot and if it is selected follow the same procedure as the first plot in this session
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

            if flag[2] == 1: #checks if the third plot is selected and if it is selected follow the same procedure as the first plot in the session
                if aufteilung == 'Frage 1':
                    tier2 = tier2.set_index('Frage 1')
                    x3 = tier2[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'green')
                    x3.set_title('TIER 2')
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

            if flag[3] == 1: #checks if the fourth plot is selected and if it is selected follow the same procedure as the first plot in this session
                if aufteilung == 'Frage 1':
                    na = na.set_index('Frage 1')
                    x4 = na[vector['question']].plot(ax = axes[kk], kind= vector['kind'], color = 'purple')
                    x4.set_title('Non-automotive')
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
            if ii == 2: #set the plotting dimensions (optimized of the lenovo machine) for 2 and 3 plots
                plt.subplots_adjust(top=0.92, bottom=0.11, left=0.12, right=0.89, hspace=0.71, wspace=0.2)
            elif ii == 3:
                plt.subplots_adjust(top=0.91, bottom=0.10, left=0.20, right=0.80, hspace=0.68, wspace=0.15)
            else:
                pass
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()

        if ii == 4: #case four plots are selected
            fig, axes = plt.subplots(2, 2) #create a matrix of plots (2,2)
            plt.suptitle(vector['supertitle']) #set supertitle as the overall title of the plot
            plt.tight_layout() #use tight layout to give an initial plot configuration
            rot = 60 #set local rotation to 60 degrees
            if aufteilung == 'Frage 1': #case the segmentation is made upon question 1
                oem = oem.set_index('Frage 1') # make the oem the subset of interest and set index to question 1
                x1 = oem[vector['question']].plot(ax = axes[0,0], kind= vector['kind'], color = 'red') #plot oem to the first subplot on the matrix and set color to red
                x1.set_title('OEM') #set subplot title to OEM
            elif aufteilung == 'Frage 6': #case the segmentation is made upon question 6
                vw = vw.set_index('Frage 6') #make VW the subset of interest and set index to question 6
                x1 = vw[vector['question']].plot(ax = axes[0,0], kind= vector['kind'],color = 'red') #plot vw to the first subplot on the matrix and set color to red
                x1.set_title('VW') #set subplot title to VW
            plt.setp(x1.get_xticklabels(), rotation = rot) #set rotation to the value declared internally (60) - optimized visually
            x1.set_yticks(vector['y_axis']) #set y ticks to the values declared on the dictionary - to make y axis always the maximum size
            x1.set_yticklabels(vector['labels']) #replace the value by the strings delcared on the dictionary
            x1.set_ylabel(vector['y_label']) #set the y label as the one delcared on the dictionary
            x1.set_xlabel('') #remove the x label

            if aufteilung == 'Frage 1': #continue to subplot 2 (0,1) and perform the same instructions as the first subplot in this session
                tier1 = tier1.set_index('Frage 1')
                x2 = tier1[vector['question']].plot(ax = axes[0,1], kind= vector['kind'], color = 'blue')
                x2.set_title('TIER 1')
            elif aufteilung == 'Frage 6':
                bmw = bmw.set_index('Frage 6')
                x2 = bmw[vector['question']].plot(ax = axes[0,1], kind= vector['kind'],color = 'blue')
                x2.set_title('BMW')
            plt.setp(x2.get_xticklabels(), rotation=rot)
            x2.set_yticks(vector['y_axis'])
            x2.set_yticklabels(vector['labels'])
            x2.set_ylabel(vector['y_label'])
            x2.set_xlabel('')
        

            if aufteilung == 'Frage 1': #continue to subplot 3 (1,0) and perform the same instructions as the first subplot in this session
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
        
            if aufteilung == 'Frage 1': #continue to subplot 4 (1,1) and perform the same instructions as the first subplot in this session
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
            plt.subplots_adjust(top=0.90, bottom=0.10, left=0.10, right=0.97, hspace=0.66, wspace=0.24) #set the overall configuration for the subplots
        else:
            pass
        plt.show() #print the figure

    #Processing of the pie charts
        
    #case the kind of the plot present in the dictionary is pie chart
    elif vector['kind'] ==  'pie':
        if ii == 1:
            #set configuration of the plot
            plt.subplots_adjust(top=0.91, bottom=0.00, left=0.28, right=0.72, hspace=0.20, wspace=0.20) 
            if flag[0] == 1: #case it is the first plot has been selected
                if aufteilung == 'Frage 1': #perform the segmentation of the data set based on the question 1
                    oem = oem.set_index('Frage 1') #make the question 1 the index of the subset
                    filter = oem[vector['question']] #isolate the column of the desired question
                    plt.title('OEM') #set title of the subplot to OEM                 
                elif aufteilung == 'Frage 6': #case the segmentation is made upon the question 6
                    vw = vw.set_index('Frage 6') #make VW the subset of interest and set index to question 6
                    filter = vw[vector['question']] #isolate the column of the desired question
                    plt.title('VW') #set title to the subplot as VW
                else:
                    pass
                map = filter.value_counts().reset_index() #count the values of each element of the desired column and reset index to reframe into a dataframe
                values =  map[vector['question']].tolist() #transform into the list
                labels = map['index'].tolist() #extract a list of lables from the index
                labels = [int(i) for i in labels] #cast values to integer           
                total = sum(values) #sum the total value for computing the absolute values out of the automatic percentage
                labels_tst = vector['labels'] #read labels from dictionary
                color_map_local = color_map[:len(labels)] #use the same amout of colors as the number of labels
                color_map_local = [color_map[ii] for ii in labels] # place colors in the same order as labels so one color always goes to the same label
                for idx in labels:
                    labels[labels.index(idx)] = labels_tst[int(idx)] #replace numerical labels by the string labels of the dictionary     
                draft = plt.pie(values, colors = color_map_local, autopct=lambda(p): '{:.0f}'.format(p * total / 100)) #plot the chart using autopct (automatic percetage) and transformit into absolute values using the total 
                plt.suptitle(vector['supertitle']) #set supertitle according to the value read from the dictionary
                plt.legend(labels, loc = 'lower right') #set legend with the labes and position it
                figManager = plt.get_current_fig_manager() #make the plot maximized on the screen
                figManager.window.showMaximized()
                plt.show() #show the plot   
            else: 
                pass

            if flag[1] == 1: #check if the second option was select and perform the same instructons as the first plot in this session
                if aufteilung == 'Frage 1':
                    tier1 = tier1.set_index('Frage 1')
                    filter = tier1[vector['question']]
                    plt.title('Tier 1')    
                elif aufteilung == 'Frage 6':
                    bmw = bmw.set_index('Frage 6')
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

            if flag[2] == 1: #check if the third option has been select and perform the same instructions as the first plot in this session
                if aufteilung == 'Frage 1':
                    tier2 = tier2.set_index('Frage 1')
                    filter = tier2[vector['question']]
                    plt.title('Tier 2')    
                elif aufteilung == 'Frage 6':
                    others = others.set_index('Frage 6')
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


            if flag[3] == 1: #check if the fourth option has been selected and perform the same instructions as the first plot in this session
                if aufteilung == 'Frage 1':
                    na = na.set_index('Frage 1')
                    filter = na[vector['question']] 
                    plt.title('Non-automotive')   
                elif aufteilung == 'Frage 6':
                    notrelevant = notrelevant.set_index('Frage 6')
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
        
        elif ii == 2 or ii == 3: #case the number of selected plot is 2 or 3
            fig, axes = plt.subplots(1, ii) #create a figure with ii subplot in a horizontal fashion
            if ii == 2: #case it is two, set the following layout configuration
                plt.subplots_adjust(top=0.91, bottom=0.0, left=0.06, right=0.94, hspace=0.18, wspace=0.0)
            elif ii == 3: #case it is two, set the follwing layout configuration
                plt.subplots_adjust(top=0.83, bottom=0.17, left=0.01, right=0.98, hspace=0.0, wspace=0.0)
            else:
                pass                                    
            plt.suptitle(vector['supertitle']) #set the overall title of the plot as the supertitle in the dictionary
 
            kk = 0 #interation variable
            if flag[0] == 1: #case the first option has been selected, plot the first plot accordingly (same as the previous session)         
                if aufteilung == 'Frage 1': 
                    oem = oem.set_index('Frage 1')
                    filter = oem[vector['question']]
                    axes[kk].set_title('OEM')   #plot the current data onto the fist subplot              
                elif aufteilung == 'Frage 6':
                    vw = vw.set_index('Frage 6')
                    filter = vw[vector['question']]
                    axes[kk].set_title('VW')   #plot the current data onto the fist subplot              
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
                axes[kk].pie(values, colors = color_map_local,  autopct=lambda(p): '{:.0f}'.format(p * total / 100)) #plot the data onto the current subplot with the same configurations as the previous session
                axes[kk].legend(labels, loc = 'lower right')  #set legend with labels and position onto the current plot                   
                kk = kk + 1 #increment the iteration variable
            else: 
                pass

            if flag[1] == 1: #check if the second option has been selected and perform the same instructions as the first plot in this session
                #plt.subplot(the_grid(0,1), aspect = 1)
                if aufteilung == 'Frage 1':
                    tier1 = tier1.set_index('Frage 1')
                    filter = tier1[vector['question']] 
                    axes[kk].set_title('Tier 1')   
                elif aufteilung == 'Frage 6':
                    bmw = bmw.set_index('Frage 6')
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

            if flag[2] == 1: #check if the third option has been selected and perform the same instructions as the first plot in this session
                if aufteilung == 'Frage 1':
                    tier2 = tier2.set_index('Frage 1')
                    filter = tier2[vector['question']]
                    axes[kk].set_title('Tier 2')     
                elif aufteilung == 'Frage 6':
                    others = others.set_index('Frage 6')
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

            if flag[3] == 1:  #check if the fourth option has been selected and perform the same instructions as the first plot in this session
                #plt.subplot(the_grid(1, 1), aspect = 1)
                if aufteilung == 'Frage 1':
                    na = na.set_index('Frage 1')
                    filter = na[vector['question']] 
                    axes[kk].set_title('Non-automotive')    
                elif aufteilung == 'Frage 6':
                    notrelevant = notrelevant.set_index('Frage 6')
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


        elif ii == 4: #case the four options have been selected
            fig, axes = plt.subplots(2, 2, sharey = True) #create a figure with a matrix configuration (2,2) for the subplots                 
            plt.suptitle(vector['supertitle']) #set overall figure title as the supertitle record on the dictionary
            #fig.legend(labels, (axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1]), 'center') 
            plt.tight_layout() #use tight layout configuration
            if flag[0] == 1:    #plot each subplot one by one and set custom configuration similarly to the previous sessions       
                if aufteilung == 'Frage 1':
                    oem = oem.set_index('Frage 1')
                    filter = oem[vector['question']]
                    axes[0, 0].set_title('OEM')                 
                elif aufteilung == 'Frage 6':
                    vw = vw.set_index('Frage 6')
                    filter = vw[vector['question']]
                    axes[0 ,0].set_title('VW') #use explicitly the subplots for plotting the data               
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

            if flag[1] == 1: #plot the second option similarly to the previous sessions
                #plt.subplot(the_grid(0,1), aspect = 1)
                if aufteilung == 'Frage 1':
                    tier1 = tier1.set_index('Frage 1')
                    filter = tier1[vector['question']] 
                    axes[0, 1].set_title('Tier 1')   
                elif aufteilung == 'Frage 6':
                    bmw = bmw.set_index('Frage 6')
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

            if flag[2] == 1: #plot the third option similarly to the previous sessions
                # plt.subplot(the_grid(1,0), aspect = 1)
                if aufteilung == 'Frage 1':
                    tier2 = tier2.set_index('Frage 1')
                    filter = tier2[vector['question']]
                    axes[1 ,0].set_title('Tier 2')     
                elif aufteilung == 'Frage 6':
                    others = others.set_index('Frage 6')
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

            if flag[3] == 1: #plot the fourth option similarly to the previous sessions
                #plt.subplot(the_grid(1, 1), aspect = 1)
                if aufteilung == 'Frage 1':
                    na = na.set_index('Frage 1')
                    filter = na[vector['question']] 
                    axes[1, 1].set_title('Non-automotive')    
                elif aufteilung == 'Frage 6':
                    notrelevant = notrelevant.set_index('Frage 6')
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
            plt.subplots_adjust(top=0.89, bottom=0.0, left=0.19, right=0.80, hspace=0.07, wspace=0.83)
            figManager = plt.get_current_fig_manager()
            figManager.window.showMaximized()         
            plt.show()

        else: 
            pass         
                    

    else:
        pass
    return  



def main():
    app = QApplication(sys.argv)
    main = AppWindow1()
    main.show()
    sys.exit(app.exec_())
   
    print flag
if __name__ == '__main__':
    main()
