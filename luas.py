import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QLabel,
                            QHBoxLayout, QVBoxLayout, QGridLayout, QFrame, QDesktopWidget)
#import liblary matematika
import math



class Luas(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500,100)
        self.setCenter()
        self.setWindowTitle('Program Kerucut')

    #fungsi menengahkan frame
    def setCenter(self):
        desktop = QDesktopWidget()
        screenwidth = desktop.screen().width()
        screenheight = desktop.screen().height()

        self.setGeometry((screenwidth - self.width())//2,
                        (screenheight - self.height())//2,
                        self.width(),
                        self.height())


        #membuat nama label
        self.labelNama = QLabel()
        self.labelNama.setText('<b><center> Program Hitung Bilangan Ruang Kerucut</center></b>')
        self.label1 = QLabel()
        self.label1.setText('<b>Jari-jari : </b>')
        self.label2 = QLabel()
        self.label2.setText('<b>Tinggi : </b>')
        self.hasil = QPushButton('Hasil')

        #membuat tombol
        self.luasAlas = QLabel('Luas Alas : ')
        self.luasSelimut = QLabel('Luas Selimut : ')
        self.luasPermukaan = QLabel('Luas Permukaan : ')
        self.volume = QLabel('Volume : ')

        #buat box edit
        self.editJari = QLineEdit()
        self.editTinggi = QLineEdit()

        #atur Horisontal layout button
        tombol = QGridLayout()
        tombol.addWidget(self.luasAlas,0,0)
        tombol.addWidget(self.luasSelimut,0,1)
        tombol.addWidget(self.luasPermukaan,1,0)
        tombol.addWidget(self.volume,1,1)

        #atur grid label isi data
        grid = QGridLayout()
        grid.addWidget(self.labelNama,0,0,1,2)
        #membuat objek garis horisontal
        horisontal = QFrame()
        #membuat garis
        horisontal.setFrameShape(QFrame.HLine)
        horisontal.setFrameShadow(QFrame.Sunken)
        grid.addWidget(horisontal,1,0,1,2)
        grid.addWidget(self.label1,2,0)
        grid.addWidget(self.label2,3,0)
        grid.addWidget(self.editJari,2,1)
        grid.addWidget(self.editTinggi,3,1)

        #satukan layout
        layout = QVBoxLayout()
        layout.addLayout(grid)
        layout.addLayout(tombol)
        #membuat objek garis horisontal
        horisontal = QFrame()
        #membuat garis
        horisontal.setFrameShape(QFrame.HLine)
        horisontal.setFrameShadow(QFrame.Sunken)
        layout.addWidget(horisontal)


        #hasil
        layout.addWidget(self.hasil)
        layout.addStretch()

        self.setLayout(layout)

        self.hasil.clicked.connect(self.hasilclick)



    def hasilclick(self):
        if len(self.editJari.text()) == 0 | len(self.editTinggi.text()) == 0:return


        jari = float(self.editJari.text())
        tinggi = float(self.editTinggi.text())

        #apotema = s
        s = (jari*jari) + (tinggi*tinggi)
        #rumus luas alas
        luasAlas = math.pi * (jari*jari)
        #luas selimut
        luasSelimut = math.pi * jari * s
        #luas permukaan
        luasPermukaan = luasAlas + luasSelimut
        #volume
        volume = 1 *( math.pi * (jari*jari) * tinggi)/3
        #proses
        self.luasAlas.setText("<b>Luas Alas : %.f %s" % (luasAlas,"</b>"))
        self.luasSelimut.setText("<b>Luas Selimut : %.f %s" % (luasSelimut,'</b>'))
        self.luasPermukaan.setText("<b>Luas Permukaan : %.f %s" % (luasPermukaan,'</b>'))
        self.volume.setText("<b>Volume : %.f %s" % (volume,'</b>'))




if __name__ == '__main__':
    a = QApplication(sys.argv)

    frame = Luas()
    frame.show()

    a.exec_()
