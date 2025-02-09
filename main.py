import sys
from typing import List
from PySide6.QtWidgets import (QApplication, QWidget, QComboBox, QDialog,
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
        self.setCentralWidget(main_widget)

        layout: QVBoxLayout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Load components
        self.workshop_link_input_box: WorkshopLinkInputBox = WorkshopLinkInputBox()
        self.edit_file_btn_: EditFileButton = EditFileButton()
        self.output_mod_list_btn: OutputModListButton = OutputModListButton()

        # Add components to the layout
        layout.addWidget(self.workshop_link_input_box)
        layout.addWidget(self.edit_file_btn_)
        layout.addWidget(self.output_mod_list_btn)
        

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
    app: QApplication = QApplication(sys.argv)  # Creates the application event loop
    window: MainWindow = MainWindow()  # Create the main window
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the event loop



if __name__ == "__main__":
    main()