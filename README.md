# Project Zomboid Mod Loader

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
