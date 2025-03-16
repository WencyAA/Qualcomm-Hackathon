# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QLabel, QProgressBar, QPushButton, QVBoxLayout, QHBoxLayout


class ProgressBar(QDialog):
    def __init__(self, parent=None):
        super(ProgressBar, self).__init__(parent)

        self.resize(350, 100)
        self.setWindowTitle(self.tr("Save progress"))

        self.TipLabel = QLabel(self.tr("current frame/All:0/0"))
        self.FeatLabel = QLabel(self.tr("Save progress:"))

        self.FeatProgressBar = QProgressBar(self)
        self.FeatProgressBar.setMinimum(0)
        self.FeatProgressBar.setMaximum(100)
        self.FeatProgressBar.setValue(0)

        TipLayout = QHBoxLayout()
        TipLayout.addWidget(self.TipLabel)

        FeatLayout = QHBoxLayout()
        FeatLayout.addWidget(self.FeatLabel)
        FeatLayout.addWidget(self.FeatProgressBar)

        self.cancelButton = QPushButton('no save', self)

        buttonlayout = QHBoxLayout()
        buttonlayout.addStretch(1)
        buttonlayout.addWidget(self.cancelButton)

        layout = QVBoxLayout()
        layout.addLayout(FeatLayout)
        layout.addLayout(TipLayout)
        layout.addLayout(buttonlayout)
        self.setLayout(layout)
        self.cancelButton.clicked.connect(self.onCancel)

    def setValue(self, start, end, progress):
        self.TipLabel.setText(self.tr("current frame/All:" + "   " + str(start) + "/" + str(end)))
        self.FeatProgressBar.setValue(progress)

    def onCancel(self, event):
        self.close()