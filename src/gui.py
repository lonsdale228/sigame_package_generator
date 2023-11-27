import sys
import threading

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt6.uic import loadUi

from MainWindow import Ui_MainWindow
from entities.generate import Generate
from entities.anime import Anime
from main import main

genres=sorted(['Drama', 'Game', 'Psychological', 'Adventure', 'Music', 'Gourmet', 'Action', 'Comedy', 'Demons', 'Police', 'Space', 'Ecchi', 'Fantasy', 'Hentai', 'Historical', 'Horror', 'Magic', 'Mecha', 'Parody', 'Samurai', 'Romance', 'School', 'Erotica', 'Shounen', 'Vampire', 'Yaoi', 'Yuri', 'Harem', 'Slice of Life', 'Shoujo Ai', 'Josei', 'Supernatural', 'Thriller', 'Sci-Fi', 'Shoujo', 'Super Power', 'Military', 'Mystery', 'Kids', 'Cars', 'Martial Arts', 'Dementia', 'Sports', 'Work Life', 'Seinen', 'Shounen Ai'])

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ui = Ui_MainWindow()
        self.btnGenerate.clicked.connect(self.on_btn_click)
        self.threads_slider.valueChanged.connect(self.show_value)
    def change_content(self):
        self.listGenres.addItems(genres)
    def set_progress(self,value):
        self.progressBar.setValue(value)
    def on_btn_click(self):
        try:
            settings = Generate()
            with settings as s:
                s.num_of_getting=int(self.edGettingNum.text())
                s.num_of_total=int(self.edTotalNum.text())
                s.op_duration=int(self.edOPDuration.text())
                s.downloading_thread=int(self.threads_slider.value())
                s.progress_bar=int(self.progressBar.value())

                s.nickname=self.edNickname.text()

                s.selected_genres=[genre.text() for genre in self.listGenres.selectedItems()]

                s.scr_round=self.cbScrRound.isChecked()
                s.op_round=self.cbOPRound.isChecked()
                s.desc_round=self.cbDescRound.isChecked()
                s.gpt_round=self.cbChatGPTRound.isChecked()

                s.remove_duplicates=self.cbRemoveDuplicates.isChecked()
                s.shuffle_lines=self.cbShuffleLines.isChecked()
                s.shuffle_questions=self.cbShuffleQuestions.isChecked()
                s.limit_theme=self.cbLimitToOne.isChecked()
                s.use_more_scr=self.cbUseMoreScr.isChecked()

                s.ona=self.cbONA.isChecked()
                s.ova=self.cbOVA.isChecked()
                s.specials=self.cbSpecials.isChecked()
                s.movie=self.cbMovie.isChecked()

                s.rb_req_genres=self.rbReqGenres.isChecked()
                s.rb_included_genres=self.rbIncludedGenres.isChecked()



        except Exception as e:
            print("Boba: ",e)

        beba=threading.Thread(target=main,args=(settings,win))
        beba.start()
        ...
    def show_value(self):
        self.lbl_slider_value.setText(str(self.threads_slider.value()))
        print(self.threads_slider.value())
class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/find_replace.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    win.change_content()

    sys.exit(app.exec())