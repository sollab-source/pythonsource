import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton('클릭하세요', self)
        # 이벤트 연결
        self.button.clicked.connect(self.showMessage)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.setWindowTitle('PyQt 버튼 클릭 예제')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showMessage(self):
        # 메시지 박스 표시
        QMessageBox.information(self, "알림", "버튼을 클릭했습니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
