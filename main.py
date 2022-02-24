import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread, Qt
from ui_mainwindow import Ui_MainWindow
from time import sleep


class Rename_Tool(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle("批量重命名")  # 窗口标题
        self.setCentralWidget(self.ui.centralwidget)
        self.ui_widgets = [self.ui.prefi_text, self.ui.preconnector_text, self.ui.name_text,
                           self.ui.suffix_connecto_text, self.ui.suffix_text, self.ui.file_suffix_text]

    def rename_func(self, list, pattern):
        pass

    def process_file_list(self, list):
        self.rename_file = WorkThread(self.rename_func, '')
        self.rename_file.start()
        self.rename_file.trigger.connect(lambda x: x)

    @pyqtSlot(bool)
    def on_start_button_clicked(self):
        self.read_file = WorkThread(self.file_list, './')
        self.read_file.start()
        self.read_file.trigger.connect(lambda x: self.process_file_list(x))

        # self.ui.progressBar.setTextVisible(True)
        # for x in range(0, 101, 100 // 33):
        #     if x >= 98:
        #         self.ui.progressBar.setValue(100)
        #     else:
        #         self.ui.progressBar.setValue(x)
        #     sleep(1)

        # if not state:
        #     for widgets in self.ui_widgets:
        #         widgets.setDisabled(True)

    def file_list(self, path):
        file_list = os.listdir(path)
        res = []
        for each in file_list:
            temp = each.split('.')
            if len(temp) < 2:
                file_list.remove(each)
            elif temp[0] == '':
                file_list.remove(each)
            else:
                res.append(each)
        return res


class WorkThread(QThread):
    trigger = pyqtSignal(list)

    def __init__(self, fun, par):
        super(WorkThread, self).__init__()
        self.par = par
        self.fun = fun

    def run(self):
        res = self.fun(self.par)
        # print(res)
        self.trigger.emit(res)


def main():
    app = QApplication(sys.argv)  # 创建GUI应用程序
    main_win = Rename_Tool()  # 创建窗体

    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":  # 用于当前窗体测试
    main()
