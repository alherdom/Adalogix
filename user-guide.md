# Adalogix - User Guide

## Introduction
This application is designed to cover different functionalities in order to facilitate the logistics management of a company, covering modules related to issues such as inventory management, user management, delivery route management.

## User Login
Allows users to authenticate to the application by providing their credentials. There will be three types of users with different permission levels; Super Admin, Admin, and Courier.

SuperAdmin will exist as a single account, which will be used mainly to generate other Admins who will be able to generate other admin users, change permissions and create Courier users.

Courier users will only have access to view the roadmap assigned to them.

![User Login](img/screenshot1.png)

## Welcome
Displays an initial view after login to welcome the user.

![Welcome](img/screenshot2.png)

## Menu
Provides main menu options to access the different functions of the application depending on the role of the user, in the image it is an admin.

![Menu](img/screenshot3.png)

## Inventory Table
Displays a table containing the list of available products, with options for managing them.

![Inventory Table](img/screenshot4.png)

## Edit Product
If we click on the pencil inside the row of each product respectively, we can access a form to edit the fields of the same product and update it in the table.

![Edit Product](img/screenshot5.png)

## Delete Products
To delete one or more products, click on the checkboxes, if you do not select any product, an error message will appear.

![Delete Products](img/screenshot9.png)

## Detail Product
Clicking on the product row view icon will open a pop-up window to view more product details.

![Detail Product](img/screenshot7.png)

## Load Products
By clicking on the upload icon, a multitude of products can be uploaded into the application through a CSV document with the same fields as in the table and in the same order, except for the product ID.

![Load Products](img/screenshot11.png)

## Export Products
By clicking on the download icon you will be able to download a CSV with all the products, if you do not select any product all of them will be downloaded, and if you select one or more than one, only those will be downloaded.

![Export Products](img/screenshot10.png)

## User Table
Displays a table containing the list of users, with options for managing them.

![](img/screenshot24.png)

## Register User
By clicking on the add users icon, you will be able to add new users through a form, the password and user will be automatically generated and this information will be sent to the user's email address.

![](img/screenshot13.png)

## Delete User
Like the inventory they can also be deleted by selecting them before.

## Edit User
As in the inventory, users can also edit themselves by clicking on the pencil icon in the corresponding row and editing the form with the data. 

![](img/screenshot12.png)

## Export User
As in the inventory, users can also be edited by clicking on the pencil icon of the corresponding row and editing the form with the data.

## Router
Module to calculate the most optimal route within the different dropoff points and start points of the warehouses, it is calculated, saved and assigned to the previously selected courier and deleted to generate a new one. First select the employee, select the courier to generate his route.

![](img/screenshot15.png)

## Set Start Point Pick Up
The sidebar has a drop-down menu where you can select the warehouse from where the route will start. Just select a warehouse and it will be directly added to the map.

![](img/screenshot16.png)

## Set DropOff
To set the dropoff points the application has a search engine, once an approximate or exact address has been entered, just click on the "+" button to add it to the route. It should be noted that in order to add a dropoff point you must first have the pick-up/start point.

![](img/screenshot16.png)

## Calculate Route
Once the dropoff points and the starting points of the stores have been established, the optimal route must be calculated, click on the calculate button. Once calculated, it will be displayed on the map with the dropoff points sorted and a legend with the dropoff points and addresses of each point respectively.

![](img/screenshot17.png)

## Save Route
To save the route, it will be necessary to have previously calculated the route and click on the "save" button.  It will automatically be added to the currently selected courier.

![](img/screenshot18.png)

## Delete Route
If you wish to delete a route, the delete button will delete both the route assigned to a courier and the route currently painted on the map.

![](img/screenshot19.png)

## Show Route Points Map in the courier application
In the courier part, once a route has been assigned from the administrator part, it will be possible to visualize this route as well as a legend with the order of the addresses where it will have to make the deliveries (the first point will always be the warehouse from where the route starts). If no route exists, only the map will be shown.

![](img/screenshot21.png)

## Complete Route
To finish the route, just click on the "finish" button at the bottom of the map. Once the button is pressed, the route associated with the courier will be deleted and the map will be empty.

![](img/screenshot22.png)

## Application Screenshots

You can see all the screenshots of the application at this [LINK](img/).
