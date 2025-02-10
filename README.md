# Project Zomboid Mod Loader

## Important Notes

This project is still in the early stages of development. The GUI is not yet implemented and the logic is still being worked on. I created this because I wanted to automate the process of adding mods to the `server.ini` file for Project Zomboid. I will be updating this project as I work on it. The code currently lives in 1 file (`main.py`) and is not yet organized into separate files. I will be working on that as well.

## TODO

### Must Have

- [ ] Error handling for duplicate links
- [ ] Error handling for invalid links
- [ ] Error handling for invalid entries
- [ ] Error handling for empty entries

### Should Have

- [ ] Make it easier to paste multiple links
- [ ] Highlight the links that are invalid
- [ ] Highlight the links that are duplicates
- [ ] Highlight the links that are empty

### Could Have

- [ ] A way to look up mods using the steam api
- [ ] A way to add the mods by clicking a button next to the mod in the list

### Won't Have

- [ ] placeholder

## Description

Just paste the workshop links of the mods you want to install, select your *.ini file and click the 'Go' button. It will automatically add the mod IDs and workshop IDs to the selected *.ini file.

---

## How it works (Logic)

### Step 1

- textbox to paste workshop links

- scrape workshop link for:  

```xpath
//div[text()='Mod ID: ModManager']
//div[text()='Workshop ID: 2694448564']
```

### Step 2

Parse the returned data and extract the Mod ID and Workshop ID from the HTML and then add them to two separate lists. One for Mod IDs and one for Workshop IDs.

### Step 3

Read the selected *.ini file, find the following lines:

```ini
Mods=Name1l;Name2;Name3;
WorkshopItems=123456;789101112;
```

Append the list of Mod IDs to the `Mods` line and the list of Workshop IDs to the `WorkshopItems` line.

## GUI Layout

- Textbox for pasting workshop links
- Button to start the process
- File upload button to select the *.ini file
- Textbox to display the output
- Progress bar to show the progress of the process
