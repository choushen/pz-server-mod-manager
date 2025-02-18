import sys
from typing import List
import requests
from requests_html import HTMLSession, HTMLResponse
from lxml import html
from lxml.html import HtmlElement
from PySide6.QtWidgets import (QApplication, QWidget, QComboBox, QDialog, QDialogButtonBox, QGridLayout, QGroupBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit, QVBoxLayout, QMainWindow, QMessageBox)
from PySide6.QtGui import QTextOption
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__() 

        # Set the window title
        self.setWindowTitle("Project Zomboid Mod Loader")

        # Create the main widget
        main_widget: QWidget = QWidget()

        # Main window config
        self.resize(800, 600)

        # Create the main layout
        self.setCentralWidget(main_widget)
        layout: QVBoxLayout = QVBoxLayout()
        main_widget.setLayout(layout)

        # Textbox and buttons layout
        row_1_layout: QHBoxLayout = QHBoxLayout()

        # Button layout
        button_layout: QVBoxLayout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        button_layout.setSpacing(5)

        # Load components
        self.workshop_link_input_box: WorkshopLinkInputBox = WorkshopLinkInputBox()
        self.edit_file_btn: EditFileButton = EditFileButton()
        self.edit_file_btn.resize(50, 30)
        self.output_mod_list_btn: OutputModListButton = OutputModListButton()

        # Add components to the button layout
        button_layout.addWidget(self.edit_file_btn)
        button_layout.addWidget(self.output_mod_list_btn)

        # Add components to the row layout
        row_1_layout.addWidget(self.workshop_link_input_box)
        row_1_layout.addLayout(button_layout)

        # Create the titles label
        title_label: QLabel = QLabel()
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")  
        title_label.setText("Project Zomboid Mod Loader v0.2")

        # Create the instructions label
        instructions_label: QLabel = QLabel()
        instructions_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instructions_label.setStyleSheet("font-size: 14px; margin: 10px;")
        instructions_label.setText("""
            <div style="font-size: 16px; font-weight: bold; text-align: center; margin-bottom: 8px;">
                Instructions
            </div>
            
            <p><b>First</b>, paste the workshop links in the text box below, separate them by a new line.</p>
            <p>After you paste the links of the mods you want, decide what you want to do by pressing one of the buttons.</p>

            <p><b>**IN DEVELOPMENT**Editing the .ini file:</b></p>
            <ul>
                <li>Click <b>"Upload and Edit .ini File"</b> to upload and edit the .ini file.</li>
                <li>The .ini file will be modified and saved in its current location.</li>
            </ul>

            <p><b>Outputting the mod list:</b></p>
            <ul>
                <li>Click <b>"Output Mod List"</b> to generate a list of mod names and workshop IDs.</li>
                <li>You can copy and paste this list for further use.</li>
            </ul>
        """)

        # Label for displaying the output
        self.output_box: QTextEdit = QTextEdit()
        self.output_box.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.output_box.setText("Output will be displayed here.")
        self.output_box.setReadOnly(True)
        self.output_box.setStyleSheet("background-color: #f0f0f0; padding: 10px; border-radius: 8px; color: black;")
        self.output_box.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.output_box.setMaximumHeight(75)  # Limits vertical expansion


        # Construct the main layout
        layout.addWidget(title_label)
        layout.addWidget(instructions_label)
        layout.addLayout(row_1_layout)
        layout.addWidget(self.output_box)


        # Connect the buttons to their respective functions
        #self.edit_file_btn.clicked.connect(self.extract_links)
        self.output_mod_list_btn.clicked.connect(self.extract_links)


    def extract_links(self) -> None:
            headers: dict  = {"User-Agent": "Mozilla/5.0"}  # Avoid bot detection
            links: list[str] = self.workshop_link_input_box.get_lines()
            workshop_id_str: str = "WorkshopItems="
            mod_name_str: str = "Mods="
            vehicle_id_str: str = "VehicleIDs="
            mod_id_xpath: str =  "//div[@class=\"workshopItemDescription\"]//br//following-sibling::text()[contains(., \"Mod ID:\")]"
            vehicle_id_xpath: str = "//div[@class=\"workshopItemDescription\"]//br//following-sibling::text()[contains(., \"Vehicle IDs:\")]"
            
            for link in links:
                # Get workshop IDs
                workshop_id: str = link.split("/")[5].strip("?id=")
                workshop_id_str += workshop_id + ";"
                # Get mod IDs
                response: requests.Response = requests.get(link, headers=headers)
                tree: HtmlElement = html.fromstring(response.content)
                mod_id: list[str] = tree.xpath(mod_id_xpath)
                mod_name_str += mod_id[0].split("Mod ID: ")[-1] + ";"
                # Get vehicle IDs
                vehicle_id: list[str] = tree.xpath(vehicle_id_xpath)
                if vehicle_id:
                    vehicle_id_str += vehicle_id[0].split("Vehicle IDs: ")[-1].replace(', ', ";") + ";"
                else:
                    print("No vehicle IDs found.")


            self.output_box.setText(f"{vehicle_id_str}\n{workshop_id_str}\n{mod_name_str}")
        

class WorkshopLinkInputBox(QTextEdit):
    def __init__(self) -> None:
        super().__init__()
        self.setPlaceholderText("e.g. https://steamcommunity.com/sharedfiles/filedetails/?id=3413150945\n       https://steamcommunity.com/sharedfiles/filedetails/?id=3409287192")
    
    def get_lines(self) -> List[str]:
        my_string_list: list[str] = self.toPlainText().strip().split("\n")
        return my_string_list


class EditFileButton(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setText("Upload and Edit .ini File")


class OutputModListButton(QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setText("Output Mod List")

def main():
    app: QApplication = QApplication(sys.argv)  # Creates the application event loop

    app.setStyleSheet("""
    QPushButton {
        background-color: #355E3B;
        color: white;
        padding: 10px;
        border-radius: 8px;
        font-size: 16px;
    }
    QPushButton:hover {
        background-color: #006400;
    }
    QPushButton:pressed {
        background-color: #00563B;
    }
    """)

    window: MainWindow = MainWindow()  # Create the main window
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the event loop






if __name__ == "__main__":
    main()