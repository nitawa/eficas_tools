# Copyright (C) 2007-2023   EDF R&D
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#
# See http://www.salome-platform.org/ or email : webmaster.salome@opencascade.com
#
# Modules Python


# Modules Eficas

#from InterfaceQT.groupe import Groupe
from UiQT5.desWidgetProfile  import Ui_ProfileVP
from Accas.extensions.eficas_translation import tr
# Import des panels

from PyQt5.QtWidgets import QCheckBox, QWidget, QGraphicsView, QGraphicsEllipseItem
from PyQt5.QtCore    import Qt, QSignalMapper, QPoint, QRectF, QTimer
from PyQt5.QtChart   import QLineSeries, QChart, QChartView, QValueAxis, QCategoryAxis, QScatterSeries
from PyQt5.QtGui     import QColor, QBrush, QPen, QPainter


tabCouleur={ 0 : (41,128,185),   1 : (46,64,83),    2 : (255,87,51),    3 : (199,00,57),
             4 : (144,12,63),    5 : (125,60,152),  6 : (249,231,159),  7 : (127,140,141),
             8 : (255,195,0),    9 : (127,179,213), 10: (204,255,0),   11 : (204, 255, 204),
            12 : (204,255,255), 13 : (204,204,255), 14: (255,204,255), 15 : (255, 204, 51),
            16 : (255,153,51),  17 : (102,0,102),   18: (255, 0, 51),  19 : (102,153,204)
           }

class MonPoint(QPoint):
#-----------------------
    def __init__(self, X,Y, laSerie, laCouleur ):
    #--------------------------------------------
    # laSerie est de type MaSerie
        debug = 0
        if debug : print ('initialisation de MonPoint avec', X, Y, laSerie)
        QPoint.__init__(self,X,Y)
        self.X=X
        self.Y=Y
        self.laSerie=laSerie
        self.selectionne=False
        self.laCouleur=laCouleur
        self.item = None
        if self.laSerie.maxY < Y :  self.laSerie.maxY = Y

        
    def affichePoint(self):
    #---------------------
        debug = 0
        if debug : print ('affiche Point',  self.X, self.Y)
        #laCouleur = QColor(130, 1, 1, 210)
        laCouleur = Qt.cyan
        if not self.item :
           self.item = QGraphicsEllipseItem(QRectF(-3, -3, 6, 6))
           #self.item.setZValue(0)
           pen =QPen(laCouleur)
           pen.setWidth(3);
           self.item.setBrush(laCouleur)
           self.item.setPen(pen)
           pos = self.laSerie.parent.graphe.mapToPosition(self)

           if not(self.item.scene()) : 
              self.laSerie.parent.graphique.scene().addItem(self.item)
              self.item.setPos(pos)
              self.selectionne=True
        else :
          self.laSerie.parent.graphique.scene().removeItem(self.item)
          self.item=None
          self.selectionne=False

    def reaffiche(self):
    #---------------------
         self.laSerie.parent.graphique.scene().removeItem(self.item)
         self.item = None
         self.affichePoint()

class MaSerie:
#-------------

    def __init__(self, lesDonnees, label, parent):
    #---------------------------------------------
        debug = 0
        #if label == 'A4' : debug = 1 
        if debug : print ('--------------------------------------------------------------')
        if debug : print ('init de MaSerie')
        if debug : print ('donneesBrutes', lesDonnees)
        if debug : print ('label', label)
        self.donneesBrutes=lesDonnees
        self.label=label
        self.parent=parent
        self.QLSerie=QLineSeries()
        self.listePoints=[]
        self.listeClicked=[]
        self.maxY = -1
        self.parent.dictLabelIdValue[label] = {}

        if lesDonnees == [] : 
           self.parent.editor.afficheMessage('pb sur les donnees de {}'.format(label), 'prevenir la maintenance')
           return
        donneesTriees=sorted(self.donneesBrutes, key = lambda donneesBrutes: donneesBrutes[0])

        if debug : print ('donneesTriees', donneesTriees)
        if debug : print ('liste des id', self.parent.listeId)

        self.indexCouleur=self.parent.chercheIndiceCouleur()
        self.couleur = QColor(tabCouleur[self.indexCouleur][0], tabCouleur[self.indexCouleur][1], tabCouleur[self.indexCouleur][2])

        if debug : print ('debut du for')
        if debug : print ('------------')

        # les labels manquants ne sont  pas dans le .comm

        rangDansLaSerie=0
        for i in range(len(self.parent.listeId)) :
            id=self.parent.listeId[i]
            if debug : print ('traitement id', id, i, rangDansLaSerie)
            if debug : print (len(donneesTriees), donneesTriees)
            if rangDansLaSerie > len(donneesTriees) -1:
               valeurDsLaSerie = 0
               if debug : print ('point manquant:', label , 'pour id', id)
               if debug : print ('plus de point dans les donnees')
            else :
               if debug : print (donneesTriees[rangDansLaSerie][0])
               if donneesTriees[rangDansLaSerie][0] == str(id) : 
                   valeurDsLaSerie=donneesTriees[rangDansLaSerie][1]
                   rangDansLaSerie=rangDansLaSerie+1
               else :
                   valeurDsLaSerie=0
                   if debug : print ('point manquant:', label , 'pour id', id)
            monPoint = MonPoint(i+1,valeurDsLaSerie,self,self.couleur)
            self.parent.dictLabelIdValue[label][id] = valeurDsLaSerie 
            self.QLSerie.append(monPoint)
            self.listePoints.append(monPoint)
            if debug : print ('point:', rangDansLaSerie, valeurDsLaSerie, 'pour Id', id)

        self.donneesTriees = donneesTriees
        newPen=QPen(self.couleur, 2)
        self.QLSerie.setPen(newPen)
        self.QLSerie.setPointsVisible(True)
        self.QLSerie.setName(label)
        self.QLSerie.clicked.connect(self.pointClicked)
        self.QLSerie.setPointLabelsVisible(True)
        self.QLSerie.setPointLabelsFormat("@yPoint");
        

    def pointClicked(self,point):
    #___________________________
        debug = 0
        index = round(point.x())
        index = index - 1
        if debug : print (index)
        if debug : print (self.listeClicked)
        if debug : print  ('pointClicked', index, index in self.listeClicked)
        if debug : print ('index clique ', index, ' sur la QLSerie ', self.label)
        if index in self.listeClicked : 
           self.listeClicked.remove(index) 
        else : 
           self.listeClicked.append(index) 
           self.parent.afficheInfosForId(index)
        if debug : print (self.listePoints) # self.QLSerie.pointsVector contient des QPoint 
        self.listePoints[index].affichePoint()
        if self.listePoints[index].selectionne  : self.parent.displaySelectedInBar()

        

         
class MonWidgetProfile(QWidget,Ui_ProfileVP):
#--------------------------------------------
    def __init__(self, editor, jdc, listeId, listeLabels):
    #---------------------------------------------------
        QWidget.__init__(self,None)
        self.setupUi(self)
        self.editor=editor
        self.jdc=jdc
        self.couleurUtilisee=-1
        self.maxY=-1
        self.widgetBar=None
        #self.listeLabels = self.editor.getValuesOfAllMC(self.jdc,('MyProfileResultat','fonction','label'))
        self.listeLabels=listeLabels
        self.dictLabelIdValue = {}
        self.listeId=listeId
        self.listeId.sort()
        self.initGraphique()
        self.inTimer=False

        

    def resizeEvent(self,event):
    #---------------------------
        if not self.inTimer:
            self.inTimer = True
            self.reaffichePoints()
            # Attention si timer trop lent l affichage est mauvais
            QTimer.singleShot(50, lambda: setattr(self, "inTimer", False))
        super().resizeEvent(event)

    def reaffichePoints(self):
    #-------------------------
        for laSerie in self.dictSerie.values():
            for ind in laSerie.listeClicked:
                laSerie.listePoints[ind].reaffiche()


    def initGraphique(self):
    #------------------------
    # on considere que la serie CPU est complete on s en sert pour creer
    #   - la liste des sha1 
    #   - les indices de l axe des X
        debug = 0
        self.dictSerie={}
        self.graphe = QChart()
        self.minY=-1

        self.axisX = QCategoryAxis()
        self.axisY = QCategoryAxis()
        self.axisX.setLabelsPosition(QCategoryAxis.AxisLabelsPositionOnValue)
        self.axisX.append('0',0)
        for i in range(len(self.listeId)):
           self.axisX.append(str(self.listeId[i]),i+1)

        aChercher='cpuTime'
        
        donneesCpuBrutes=self.editor.selectXY(('MyProfileResultat','sha1Id'),('MyProfileResultat','cpuTotalTime'))
        if donneesCpuBrutes == [] : return
        maSerieCpu = MaSerie(donneesCpuBrutes,'cpuTotalTime',self)
        if debug : print ('serie cpu', maSerieCpu.donneesTriees)
        self.dictSerie['cpuTotalTime']=maSerieCpu
        self.graphe.addSeries(maSerieCpu.QLSerie)
        # Il sera possible d affiner l echelle quand on enlevra des series
        self.maxY = maSerieCpu.maxY

        # on change les labels de l axe des x
        self.axisX.setMin(0)
        self.axisX.setMax(len(donneesCpuBrutes)+1)

        for label in self.listeLabels:
            if debug : print ('traitement de ', label)
            donneesBrutes=self.editor.selectXYWhereCondition(('MyProfileResultat','sha1Id'),('MyProfileResultat','fonction'),aChercher,'label', label)
            if debug : print ('donneesBrutes ', donneesBrutes )
            maSerie = MaSerie(donneesBrutes,label,self)
            self.dictSerie[label]=maSerie
            self.graphe.addSeries(maSerie.QLSerie)
            self.graphe.setAxisX(self.axisX, maSerie.QLSerie);
            self.graphe.setAxisY(self.axisY, maSerie.QLSerie);

        # petite preparation pour l affichage eventuel du nb de call
        if aChercher=='cpuTime' :
           if debug : print ('self.maxY', self.maxY)
           self.axisY.setMin(-2)
           self.axisY.setMax(self.maxY+30)
           pas=round(((self.maxY+20)/10) -0.5)
           self.axisY.append('0',0)
           y=0
           while y < self.maxY :
             self.axisY.append(str(y),y)
             y+=pas
        else : 
           self.axisY.setMin(-2)
           self.axisY.setMax(110)
           self.axisY.append('0',0)
           self.axisY.append('25',25)
           self.axisY.append('50',50)
           self.axisY.append('75',75)
           self.axisY.append('100',100)
          
        self.axisY.setLabelsPosition(QCategoryAxis.AxisLabelsPositionOnValue)
        self.graphe.setAxisX(self.axisX, maSerieCpu.QLSerie);
        self.graphe.setAxisY(self.axisY, maSerieCpu.QLSerie);
        self.graphe.setTitle("Profiling")

        # les legendes clicables
        self.dictMarkers={}
        self.monMapper=QSignalMapper()
        self.monMapper.mapped[int].connect(self.markerClicked)
        markers = self.graphe.legend().markers()
        k=0
        for m in markers :
            m.clicked.connect(self.monMapper.map)
            self.monMapper.setMapping(m,k)
            self.dictMarkers[k]=m
            k+=1

        self.graphique = QChartView(self.graphe)
        self.GraphLayout.addWidget(self.graphique)
        self.graphique.setRenderHint(QPainter.Antialiasing)



    def chercheIndiceCouleur(self):
    #------------------------------
        if self.couleurUtilisee < 9 :
           self.couleurUtilisee += 1
           return self.couleurUtilisee
        self.editor.afficheMessage('Pas assez de couleurs definies',
                                    'Prevenez la maintenance',critique=False)
        return 1

    def markerClicked(self,index):
    #-----------------------------
    # cache ou affiche la QLSerie selon le click sur la legende
        debug = 0
        if debug : print ('in markerClicked')
        marker=self.dictMarkers[index]
        if debug : print ('index', index)

        if debug : print ('Visible : ',marker.series().isVisible())
        if marker.series().isVisible() : marker.series().setVisible(False)
        else :  marker.series().setVisible(True)
        marker.setVisible(True)
        if not (marker.series().isVisible()): alpha = 0.5
        else : alpha = 1.0

        brush = marker.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush);

        brush = marker.brush();
        color = brush.color();
        color.setAlphaF(alpha);
        brush.setColor(color);
        marker.setBrush(brush);

        pen = marker.pen();
        color = pen.color();
        color.setAlphaF(alpha);
        pen.setColor(color);
        marker.setPen(pen);
                                                         

    def afficheInfosForId(self,index):
    #---------------------------------
        id=self.listeId[index]
        self.editor.afficheInfosForId(id)

    def displaySelectedInBar(self):
    #------------------------------
       
       if self.widgetBar == None :
          from InterfaceGUI.VisuProfile.monWidgetBar import MonWidgetBar
          self.widgetBar=MonWidgetBar(self)
          self.widgetBar.adjustSize()
          self.widgetBar.show()
          self.widgetBar = None
       else :
          print ('on ajoute une serie')
