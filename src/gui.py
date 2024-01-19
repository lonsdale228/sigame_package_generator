import sys
import threading

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QSlider, QLabel
)
from PyQt6.uic import loadUi

from MainWindow import Ui_MainWindow
from entities.generate import Generate
from entities.anime import Anime
from main import main

genres = sorted(
    ['Drama', 'Game', 'Psychological', 'Adventure', 'Music', 'Gourmet', 'Action', 'Comedy', 'Demons', 'Police', 'Space',
     'Ecchi', 'Fantasy', 'Hentai', 'Historical', 'Horror', 'Magic', 'Mecha', 'Parody', 'Samurai', 'Romance', 'School',
     'Erotica', 'Shounen', 'Vampire', 'Yaoi', 'Yuri', 'Harem', 'Slice of Life', 'Shoujo Ai', 'Josei', 'Supernatural',
     'Thriller', 'Sci-Fi', 'Shoujo', 'Super Power', 'Military', 'Mystery', 'Kids', 'Cars', 'Martial Arts', 'Dementia',
     'Sports', 'Work Life', 'Seinen', 'Shounen Ai'])


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.ui = Ui_MainWindow()
        self.btnGenerate.clicked.connect(self.on_btn_click)

        self.threads_slider.valueChanged.connect(lambda value: self.attach_to_tick(value,self.threads_slider,self.lbl_slider_value))
        self.image_quality_slider.valueChanged.connect(lambda value: self.attach_to_tick(value,self.image_quality_slider,self.lbl_image_val,'%'))
        self.audio_quality_slider.valueChanged.connect(lambda value: self.attach_to_tick(value,self.audio_quality_slider,self.lbl_audio_val,'kb'))


    def change_content(self):
        self.listGenres.addItems(genres)

    def set_progress(self, value):
        self.progressBar.setValue(value)

    def on_btn_click(self):
        try:
            settings = Generate()
            with settings as s:
                s.num_of_getting = int(self.edGettingNum.text())
                s.num_of_total = int(self.edTotalNum.text())
                s.op_duration = int(self.edOPDuration.text())
                s.downloading_thread = int(self.threads_slider.value())
                s.progress_bar = int(self.progressBar.value())

                s.nickname = self.edNickname.text()

                s.selected_genres = [genre.text() for genre in self.listGenres.selectedItems()]

                s.scr_round = self.cbScrRound.isChecked()
                s.op_round = self.cbOPRound.isChecked()
                s.desc_round = self.cbDescRound.isChecked()
                s.gpt_round = self.cbChatGPTRound.isChecked()

                s.remove_duplicates = self.cbRemoveDuplicates.isChecked()
                s.shuffle_lines = self.cbShuffleLines.isChecked()
                s.shuffle_questions = self.cbShuffleQuestions.isChecked()
                s.limit_theme = self.cbLimitToOne.isChecked()

                s.ona = self.cbONA.isChecked()
                s.ova = self.cbOVA.isChecked()
                s.specials = self.cbSpecials.isChecked()
                s.movie = self.cbMovie.isChecked()

                s.dont_use_genres = self.rbDontUseGenres.isChecked()
                s.rb_req_genres = self.rbReqGenres.isChecked()
                s.rb_included_genres = self.rbIncludedGenres.isChecked()

                s.image_compress_percent = self.image_quality_slider.value()
                s.audio_compress_bitrate = self.audio_quality_slider.value()

                s.compress_after = int(self.ed_compress_after.text())

            main_thread = threading.Thread(target=main, args=(settings, win))
            main_thread.start()

        except Exception as e:
            print("Gui exception: ", e)

    # def roundToNearestTick(self,value):
    #     # Get the tick interval
    #     tick_interval = 10  # Change this to match the tick interval you set
    #     # Calculate the nearest tick value
    #     nearest_tick = round(value / tick_interval) * tick_interval
    #     slider.setValue(nearest_tick)  # Set the slider value to the nearest tick

    def attach_to_tick(self, value, slider: QSlider, lbl: QLabel = None, modifier: str = ''):
        if lbl is not None:
            lbl.setText(str(slider.value()) + modifier)

        tick_interval = slider.tickInterval()
        nearest_tick = round(value / tick_interval) * tick_interval
        slider.setValue(nearest_tick)

    # def show_thread_value(self, value):
    #     tick_interval = self.threads_slider.tickInterval()
    #     nearest_tick = round(value / tick_interval) * tick_interval
    #     self.lbl_slider_value.setText(str(self.threads_slider.value()))
    #     self.threads_slider.setValue(nearest_tick)
    #
    # def show_image_value(self):
    #     self.lbl_image_val.setText(str(self.image_quality_slider.value()) + '%')
    #
    # def show_audio_value(self):
    #     self.lbl_audio_val.setText(str(self.audio_quality_slider.value()) + 'kb')


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
