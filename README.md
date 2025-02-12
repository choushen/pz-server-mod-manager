# Project Zomboid Mod Loader

---

## **Important Notes**

This project is still in the early stages of development.

I created this because I wanted to automate adding mods to the `server.ini` file for Project Zomboid. I know an in-game mod manager exists, but for my use-case I needed something that could do exactly what this program does. I didn't bother checking if anything else existed because I just wanted to practice making something with PyQT as it had been a while.  

I will be updating this project as I work on it. The code currently lives in **one file** (`main.py`) and is not yet organized into separate files. I will be working on that as well.

It does what I want it to do for now. I might revisit the project to clean it up a bit and add functionality to the button that updates the .ini file. 

---

## **TODO**

### **Must Do**
- [x] Add support for scraping vehicle IDs
- [ ] Remove unused packages
- [ ] Deadwood the codebase
- [x] Output mod names **(Done)**
- [ ] Error handling for duplicate links
- [ ] Error handling for invalid links
- [ ] Error handling for invalid entries
- [ ] Error handling for empty entries

### **Should Have**
- [ ] Edit the `.ini` file directly, copy the existing file, append `"backup"` to the name, and drop the new file in the same location
- [ ] Add some caching (?)
- [ ] Make it easier to paste multiple links
- [ ] Highlight the links that are invalid/empty
- [ ] Highlight the links that are duplicates

### **Could Have**
- [ ] A way to look up mods using the Steam API
- [ ] A way to add mods by clicking a button next to the mod in the list

### **Won't Have**
- [ ] Placeholder

---

## **How to Launch**

### Windows

Click [here](https://github.com/choushen/pz-server-mod-manager/releases) and download the .exe, then run it 

### **Clone, Build, and Run the Project**

Follow these steps to **pull your repository, install dependencies, and run the application**.

### **1. Clone the Repository**
Open a terminal (Command Prompt, PowerShell, or macOS/Linux terminal) and run:

```bash
git clone git@github.com:choushen/pz-server-mod-manager.git
```
This will create a folder named `pz-server-mod-manager`.

### **2. Navigate into the Project Directory**
```bash
cd pz-server-mod-manager
```

### **3. Create a Virtual Environment (Recommended)**
To isolate dependencies, create a virtual environment:

#### **Windows (PowerShell)**
```powershell
python -m venv venv
venv\Scripts\activate
```

#### **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **4. Install Dependencies**
Ensure you have all required packages installed:

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn’t exist, install manually:

```bash
pip install requests requests-html lxml PySide6
```

### **5. Run the Application**
Execute the main script:

```bash
python main.py
```

---

## **How to Use**

### **Instructions**
1. **Paste workshop links** into the text box below, separating them by a new line.
2. **Decide what you want to do** and press one of the buttons.

### **Editing the `.ini` File (In Development)**
- Click **"Upload and Edit .ini File"** to upload and modify the `.ini` file.
- The `.ini` file will be modified and saved in its current location.

### **Outputting the Mod List**
- Click **"Output Mod List"** to generate a list of mod names and workshop IDs.
- You can copy and paste this list for further use.

![Demo](demo_01.png)

---

## **How It Works (Logic)**

### **Step 1: Scrape Workshop Links**
- The user pastes workshop links into the textbox.
- The scraper extracts:
  ```xpath
  //div[text()='Mod ID: ModManager']
  //div[text()='Workshop ID: 2694448564']
  ```

### **Step 2: Extract Data**
- Extract `Mod ID` and `Workshop ID` from the HTML.
- Store them in two separate lists:
  - `Mods=[]`
  - `WorkshopItems=[]`

### **Step 3: Modify the `.ini` File**
- Read the selected `.ini` file.
- Locate these lines:

  ```ini
  Mods=Name1;Name2;Name3;
  WorkshopItems=123456;789101112;
  ```

- Append the extracted mod names and workshop IDs.

---

## **GUI Layout**
- **Textbox** for pasting workshop links.
- **Button** to start the process.
- **File upload** button for selecting the `.ini` file.
- **Textbox** to display the output.
- **Progress bar** to show the process progress.
