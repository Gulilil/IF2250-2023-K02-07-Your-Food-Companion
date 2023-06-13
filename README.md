## Overview
Your Food Companion is a desktop application that aims to assist you in keeping track of your food supplies and minimizing domestic waste due to expired food.
It's a personal food waste tracker that allows you to store information about your food items and manage them efficiently.
The application comes with two primary features: tracking your food supplies and maintaining your shopping list.
You can store data about your food items and the application will help you generate a directory that will provide you with essential information to manage your supplies effectively. 
Additionally, the application allows you to create a shopping list and keep track of your purchase history.
With Your Food Companion, you can easily manage your food supplies and avoid wasting food.

## Table of Contents
* [Requirements and Prerequisites](#requirements-and-prerequisites)
* [How to Run](#how-to-run)
* [Modules](#modules)
* [Database](#database)
* [Project Structure](#project-structure)
* [Branching Notes](#branching-notes)
* [Authors](#authors)

## Requirements and Prerequisites
Here are the required programs you need to prepare to run this desktop application:
* [Python](https://www.python.org/downloads/)
* Required packages as specified
  in [`requirements.txt`](https://gitlab.informatika.org/noelsimbolon/your-food-companion/-/blob/main/requirements.txt)

## How to Run
1. Clone this repository

   Using HTTPS:

   ```sh
   git clone https://gitlab.informatika.org/noelsimbolon/your-food-companion.git 
   ```

   Using SSH:

   ```sh
   git clone git@gitlab.informatika.org:noelsimbolon/your-food-companion.git 
   ```
2. Change the current directory into the cloned repository </br>
 
   ```sh
    cd your-food-companion
    ```
3. [Create and activate](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) the virtual environment in which you want to install packages
4. Install required packages using `pip`

   ```shell
   pip install -r requirements.txt
   ```
5. Run the desktop application using `python`

   ```shell
   python -m src.main
   ```

## Modules
| Module           | Author                    | Done    | Image                                                                                                                   |
|------------------|---------------------------|---------|-------------------------------------------------------------------------------------------------------------------------|
| Dashboard        | Enrique Alifio Ditya      | &check; | [Dashboard](https://gitlab.informatika.org/noelsimbolon/your-food-companion/-/blob/dev/doc/dashboard.png)               |
| Food Inventory   | Juan Christopher Santoso  | &check; | [Food Inventory](https://gitlab.informatika.org/noelsimbolon/your-food-companion/-/blob/dev/doc/food_inventory.png)     |
| Shopping List    | Antonio Natthan Krishna   | &check; | [Shopping List](https://gitlab.informatika.org/noelsimbolon/your-food-companion/-/blob/dev/doc/shopping_list.png)       |
| Shopping History | Noel Christoffel Simbolon | &check; | [Shopping History](https://gitlab.informatika.org/noelsimbolon/your-food-companion/-/blob/dev/doc/shopping_history.png) |
| Report           | Rinaldy Adin              | &check; | [Report](https://gitlab.informatika.org/noelsimbolon/your-food-companion/-/blob/dev/doc/report.png)                     |

## Database
| Table          | Attributes                                                                 |
|----------------|----------------------------------------------------------------------------|
| food           | <u>id</u>, name, category                                                  |
| stored_food    | <u>id</u>, quantity, unit, price, expiration_date, storing_location, notes |
| eaten_food     | <u>id</u>, quantity, unit, eaten_date                                      |
| expired_food   | <u>id</u>, quantity, unit, price, expiration_date                          |
| grocery_food   | <u>id</u>, priority                                                        |
| purchased_food | <u>id</u>, quantity, unit, purchase_date                                   |

## Project Structure
    .   
    ├─ assets                           # Contains asset (fonts, icons, and images) needed by the application
    ├─ doc                              # Contains screenshots of the application
    ├─ src                              # Contains the source code of the application
    ├─ LICENSE
    ├─ README.md
    └─ requirements.txt                 # Contains required Python packages to run the application

## Branching Notes

### Branches Explanation
Deployed program will be stored in the `main` branch. Every fixed development regarding the program will be merged into this specific branch. However, **need to be noted** that merging to main will only be done when the **program is done and tested**.

Every progress during the development of the program will be constructed inside the `dev` branch. This specific branch will be the primary branch to be used while the program is being developed.

### Making a Branch
Before making a specific module, please mind to make a new branch **from `dev` branch, don't make from `main` branch.** To check which branch you are in, try

```shell
git branch
# or
git status
```

To make a new branch, try:

```shell
git branch <branch-name>
```

Don't forget to move to the new branch. Making new branch does not automatically move you into that constructed branch.

```shell
git checkout <branch-name>
```

### Pull and push in a Branch
When you are in a specific branch, adding 'origin' keyword when pulling or pushing might help.

```sh
git pull origin <branch-name>
# and
git push origin <branch-name>
```

### Merging a Branch
To merge a branch, you need to make sure that you are in the parent branch. In this case, `dev` branch will be the parent branch. Make sure to commit the progress first before changing to any branches.

```sh
git checkout dev
```

After changing the current branch into `dev` branch, to merge, try:

```sh
git merge <branch-name>
```

## Authors
| Name                      | ID       |
|---------------------------|----------|
| Noel Christoffel Simbolon | 13521096 | 
| Juan Christopher Santoso  | 13521116 | 
| Rinaldy Adin              | 13521134 |
| Enrique Alifio Ditya      | 13521142 |
| Antonio Natthan Krishna   | 13521162 |
