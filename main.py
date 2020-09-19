from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import random
import praw
from wid import Ui_Form

reddit = praw.Reddit(client_id="client_id",
                         client_secret="client_secret of bot",
                         username="redditbotname",
                         password="redditbotpassword",
                         user_agent="user_agent")

all_subs = []

class Ui_redditdw(object):
    def setupUi(self, redditdw):
        redditdw.setObjectName("redditdw")
        redditdw.resize(594, 560)
        self.centralwidget = QtWidgets.QWidget(redditdw)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 180, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 270, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 300, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        redditdw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(redditdw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 21))
        self.menubar.setObjectName("menubar")
        redditdw.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(redditdw)
        self.statusbar.setObjectName("statusbar")
        redditdw.setStatusBar(self.statusbar)

        self.retranslateUi(redditdw)
        QtCore.QMetaObject.connectSlotsByName(redditdw)

        self.pushButton.clicked.connect(self.create_sub_list)


    def retranslateUi(self, redditdw):
        _translate = QtCore.QCoreApplication.translate
        redditdw.setWindowTitle(_translate("redditdw", "MainWindow"))
        self.pushButton.setText(_translate("redditdw", "start"))
        self.label.setText(_translate("redditdw", "Reddit forum name: "))
        self.label_2.setText(_translate("redditdw", "list generate how namy will be generate more = bigger list so less repeated"))
        self.label_3.setText(_translate("redditdw", " images takes longer time 100 recomended for small batche"))
        self.lineEdit_2.setText(_translate("redditdw", "100"))


    def create_sub_list(self):

        limit_prep = self.lineEdit_2.text()
        reddit_name_prep = self.lineEdit.text()
        reddit_name = str(reddit_name_prep)
        limit = int(limit_prep)


        subreddit = reddit.subreddit(reddit_name)

        top = subreddit.top(limit=limit)

        for submission in top:
            all_subs.append(submission)
        Ui_redditdw.meme(self)

    def meme(self):
        random_sub = random.choice(all_subs)
        img_url_scraped = random_sub.url
        Ui_redditdw.download(self, img_url_scraped)

    def download(self, img_url_scraped):
        try:
            name = random.randint(1, 10000)
            file_name = str(name)
            output_path = "destination here" + file_name + ".png"
            response = requests.get(img_url_scraped)
            file = open(output_path, "wb")
            file.write(response.content)
            file.close()
            print("saved image in", output_path)
            Ui_redditdw.meme(self)
        except:
            Ui_redditdw.meme(self)






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    redditdw = QtWidgets.QMainWindow()
    ui = Ui_redditdw()
    ui.setupUi(redditdw)
    redditdw.show()
    sys.exit(app.exec_())
