# Tool
## GUI
### Install
For the GUI, QT designer was used.
`sudo apt-get install qt4-designer`

### Files
The first file `dialog1.ui` is the main Gui and devides the dataset
the `dialog2.ui` is the output of INVClients and the `dialog3.ui` is the output of the EXTClients.

### Logic
The starting GUI is `dialog1.ui`. The user can select via the drop down menu which dependency shall be displayed. In function of the selection `dialog2.ui` or `dialog3.ui` will replace the `dialog1.ui` and give some more filter options. The plot button shall trigger the plots and the back button shall replace the current window with the `dialog1.ui` window.

## Linking
Linking the python code with the QT GUI was implemented with PyQt
### Install
QT4 `sudo apt-get install qt4-default`
[SIP](http://pyqt.sourceforge.net/Docs/sip4/installation.html)
[PyQt4](http://pyqt.sourceforge.net/Docs/PyQt4/installation.html)
## Code
## Data