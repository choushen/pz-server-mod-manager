import sys
from typing import List
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QMainWindow)



class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__() 

        self.setWindowTitle("Project Zomboid Mod Loader")

        # Create the main widget
        main_widget: QWidget = QWidget()

        # Create the layout
        self.setCentralWidget(central_widget)

        layout: QVBoxLayout = QVBoxLayout()
        main_widget.setLayout(layout)
        

class WorkshopLinkInputBox(QLineEdit):
    def __init__(self) -> None:
        super().__init__()
        self.setPlaceholderText("Enter the workshop link here")


class EditFileButton(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setText("Edit File")

class OutputModListButton(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setText("Output Mod List")


def main():
    print("Hello World")
    MainWindow()
    app: QApplication = QApplication(sys.argv) # Creates the application event loop



if __name__ == "__main__":
    main()