import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class Rename_Tool(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建窗体
        self.ui = Ui_MainWindow()  # 创建UI对象
        self.ui.setupUi(self)  # 构造UI界面
        self.setWindowTitle("批量重命名")  # 窗口标题
        self.setCentralWidget(self.ui.centralwidget)


def main():
    app = QApplication(sys.argv)  # 创建GUI应用程序
    main_win = Rename_Tool()  # 创建窗体

    main_win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":  # 用于当前窗体测试
    main()

