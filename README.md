# FuelBot: Fuel Tracking System

With the rising cost of living and need to be able to easily manage one's budget, FuelBot is a simple tracking system to help vehicle users understand how much they are spending on fuel. This useful little tool can quickly analyse your average spend so that you can better manage your finances.

![Image of FuelBot](documentation/readme-images/fuelbot_logo.png)

[Visit the FuelBot live app here](https://fuelbot.herokuapp.com/)

<br>

## Contents
----

### [User Experience (UX)](#user-experience-ux-1)
- [Purpose](#purpose)
- [User Stories](#user-stories)

### [Design](#design-1)
- [Colour Scheme](#colour-scheme)
- [Programme Model](#programme-model)

### [Features](#features-1)
- [Existing Features](#existing-features)
- [Future Features](#future-features)

### [Technologies](#technologies-1)
- [3rd Party Modules](#modules)

### [Version Control](#version-control-1)

### [Deployment](#deployment-1)

### [Testing](#testing-1)
- [Pep8](#pep_8)
- [User Story Testing](#user-story-testing)
- [Bugs](#bugs)

### [Credits](#credits-1)
- [Resources](#resources)
- [Acknowledgements](#acknowledgements)

<br>

----

<br>

## User Experience (UX)
### **Purpose**

Aimed at people who want to better understand how much they are spending on their vehicles so they can be better informed when making financial decisions. 

FuelBot allows the user to log details for up to 3 vehicles. They can regularly track their fuel spend and any additional costs on general vehicle expenses.
Once they have entered a minimum of 3 entries this handy programme will be able to offer insights about their average spend per month/week/day as well as average cost per litre and mpg.

<br>

### User Stories

Users:
 - People wanting to cut their spending down and save
 - Motor enthusiasts who like to track their vehicles efficiency

 Goals:
  - I want to see my average spend on fuel per month/week/day
  - I want to be able to add multiple vehicles
  - I want to know my vehicles mpg
  - I want to be able to see my past records

<br>

----

## Design
### **Colour Scheme**
Coloured fonts were used to make the programme more visually appealing. The primary colour was used for core text, while the secondary colour was used mostly to inidicate a system message to the user.

Primary colour: Light cyan

Secondary colour: Yellow

<br>

### **Typography**
For each core screen the heading is presented in a chunky font. This has been created using [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) font "slant".
The font has a motorsport feel to it and so is in keeping with a tool based around vehicle performance.


<br>

### **Programme Model**

The below [Lucid](https://www.lucidchart.com/pages/) flowchart was created when thinking about the structure of this programme. A clear vision of the process helped to design a core model.

![Image of process Flowchart](documentation/readme-images/flowchart.png)

<br>

----

## Features
### **Existing Features**
<details>
<summary>Welcome Page</summary>
This is the entry point to the programme. It provides to the user the programme name, logo and core function information.

<br>

![Screenshot of entry point to programme](documentation/readme-images/logo_screen.png)
</details>
<details>
<summary>Login Menu</summary>
This first menu allows the user to login if they already have an account, to create an account or to view an 'About' page.

<br>

![Screenshot of login menu](documentation/readme-images/menu.png)
</details>
<details>
<summary>About</summary>
This is a straight forward information page about how FuelBot works. There is no interactivity for the user except to hit the return button when they are finished reading.

<br>

![Screenshot of the about page](documentation/readme-images/about.png)
</details>
<details>
<summary>Create Account</summary>
The sign page allows the user to create an account by setting a unique username and choosing a password. These details are saved to a google worksheet.

<br>

![Screenshot of account creation page](documentation/readme-images/sign_up.png)
</details>
<details>
<summary>Login</summary>
The below screenshot shows the login details for a dummy account.

<br>

![Screenshot of login page](documentation/readme-images/login.png)
</details>
<details>
<summary>Vehicles Choice Page</summary>
This is the first page that is displayed to the user after they have successfully logged in. It lists any already saved vehicles. If the user wants to add a new vehicle they simply select an empty slot as instructed.

<br>

![Screenshot of vehicles choice page](documentation/readme-images/vehicles.png)
</details>
<details>
<summary>Add Vehicle</summary>
The below screenshot shows an example vehicle being added

<br>

![Screenshot of add vehicle page](documentation/readme-images/add_vehicle.png)
</details>
<details>
<summary>Vehicle Account Menu</summary>
The vehicle account menu provides access to the main features of FuelBot. Here the user can select to add a fuel entry, add expenses, view previous records, or view insights.

<br>

![Screenshot of vehicle account menu](documentation/readme-images/vehicle_menu.png)
</details>
<details>
<summary>Add Fuel</summary>
The below screenshot shows an example fuel entry being completed

<br>

![Screenshot of add fuel page](documentation/readme-images/add_fuel.png)
</details>
<details>
<summary>Add Expenses</summary>
The below screenshot shows an example expense being entered

<br>

![Screenshot of add expenses page](documentation/readme-images/add_expenses.png)
</details>
<details>
<summary>Previous Records</summary>
The user will be shown a menu where they can select if they want to view records for fuel or expenses. They will then be taken to a new screen that displays all their previous records for that specific vehicle.

<br>

![Screenshot of a the records menu](documentation/readme-images/records_menu.png)

![Screenshot of a dummy accounts previous fuel records](documentation/readme-images/records_fuel.png)

![Screenshot of a dummy accounts previous expenses records](documentation/readme-images/records_expenses.png)

</details>
<details>
<summary>Insights</summary>
The user will be shown a menu where they can select if they want to view insights for fuel or expenses. They will then be taken to a new screen that displays these insights for that specific vehicle.

<br>

![Screenshot of a the insights menu](documentation/readme-images/insights_menu.png)

<br>

Fuel insights show averages for mpg, cost per litre, cost per month, week and day, and miles per month, week and day:

![Screenshot of a dummy accounts fuel insights](documentation/readme-images/insights_fuel.png)

<br>

Expense insights show averages for cost per month, week and day:

![Screenshot of a dummy accounts expenses insights](documentation/readme-images/insights_expenses.png)
</details>



<br>

### **Future Features**

There is certainly further functionality I would have liked to add to this tool given time. This includes:
 - Use of graphs via matplotlib or pandas would really enhance the visual expenerience for the user. For example it would be great to plot the change in fuel price over a period of time.
 - I would like to add the functionality to delete entries and to edit or remove vehicles attached to a persons account.


<br>

----

## Technologies
### **Languages Used**


<br>

**Frameworks, Libraries and Programs Used**

<br>

----

## Version Control
Version control has been maintained using Git. The code written for this website has been updated via regular commits to Github.

<br>

----

## Deployment

<br>

----

## Testing

### **Pep 8**

<br>

### **User Story Testing**

| User Story | Solution | Tested & Successfully Completed |
| :----| :---| :----------------------:|
| I want to  |  | Yes |
| I want to  |  | Yes |

<br>

### **Bugs**
  
  | Raised by | Bug | Solution |
  | :---      | :---| :---     |
  |  |  |  |
  |  |  |  |
 
<br>

----

## Credits
### **Resources**

<br>

### **Acknowledgements**


