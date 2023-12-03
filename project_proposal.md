# Project Proposal

Once the proposal is complete, please let your mentor know that this is ready to be reviewed.

## Get Started

|            | Description                                                                                                                                                                                                                                                                                                                                              | Fill in |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Tech Stack | What tech stack will you use for your final project? It is recommended to use the following technologies in this project: Python/Flask, PostgreSQL, SQLAlchemy, Heroku, Jinja, RESTful APIs, JavaScript, HTML, CSS. Depending on your idea, you might end up using WTForms and other technologies discussed in the course.                               | I plan on using Python, Flask, PostgreSQL, SQLAlchemy, RESTful APIs, HTML, WTForms, and Bcrypt         |
| Type       | Will this be a website? A mobile app? Something else?                                                                                                                                                                                                                                                                                                    | Only website for now        |
| Goal       | What goal will your project be designed to achieve?                                                                                                                                                                                                                                                                                                      | Search for or find recipes using categories or ingredients. Using a couple ingredients as filters and something that acts like "your refrigerator". The user can show recipes that include only items in the fridge or recipes that involve the ingredients and add the missing ingredients to a "shopping cart." The user can also take a recipe and alter/modify it to their liking (substitute ingredients to be gluten-free) and save it as their own. They can also share their link/recipe with others.       |
| Users      | What kind of users will visit your app? In other words, what is the demographic of your users?                                                                                                                                                                                                                                                           | People who have a bunch of ingredients at home but don't know what to cook with them can use this to find something to cook. Home cooks that want to expand their recipe list can search among a category or specific ingredient they want to experiment with and can use this as well.        |
| Data       | What data do you plan on using? How are you planning on collecting your data? You may have not picked your actual API yet, which is fine, just outline what kind of data you would like it to contain. You are welcome to create your own API and populate it with data. If you are using a Python/Flask stack, you are required to create your own API. | [spoonacularAPI](https://spoonacular.com/food-api/docs) is the API I plan on using.        |

# Breaking down your project

- Determining user flow(s)
- Setting up the backend and database
- Setting up the frontend
- What functionality will your app include?
  - User login and sign up
  - Uploading a user profile picture

| Task Name                   | Description                                                                                                   | Difficulty | Type      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- | --------- |
| Design Database schema      | Determine the models and database schema required for your project.                                           | Medium     | Backend   |
| Source Your Data            | [spoonacularAPI](https://spoonacular.com/food-api/docs) is the API I plan on using.                           | Easy       | Backend   |
| User Flows                  | Determine user flow(s) - think about what you want a user’s experience to be like as they navigate your site. | Medium     | Frontend  |
| Set up backend and database | Configure the environmental variables on your framework of choice for development and set up database.        | Easy       | Backend   |
| Set up frontend             | Set up frontend framework and link it to the backend with an API call.                                        | Easy       | Frontend  |
| User Authentication         | Fullstack feature - ability to authenticate (login and sign up) as a user.                                    | Medium     | Backend   |
| Recipe Search               | Search using categories or ingredients as filters.                                                            | Easy       | Fullstack |
| Filter owned ingredients    | Display recipes that only include the ingredients(minus simple things like salt/water/ect.)                   | Hard       | Fullstack |
| User Profile/Recipes saved  | Set up a way to save and view recipes.                                                                        | Easy       | Fullstack |
| Recipe Modification         | User can save recipes as their own and change or update for example ingredients.                              | Medium     | Fullstack |
| Meal Prep/Plan              | Create a plan for breakfast/lunch/dinner if desired for over the week.                                        | Medium     | Frontend  |
| Shopping list               | User can create a list for shopping ingredients for a recipe they plan on making.                             | Medium     | Frontend  |

## Labeling

Labeling is a great way to separate out your tasks and to track progress. Here’s an [example](https://github.com/hatchways/sb-capstone-example/issues) of a list of issues that have labels associated.

| Label Type    | Description                                                                                                                                                                                                                                                                                                                     | Example                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Difficulty    | Estimating the difficulty level will be helpful to determine if the project is unique and ready to be showcased as part of your portfolio - having a mix of task difficultlies will be essential.                                                                                                                               | Easy, Medium, Hard           |
| Type          | If a frontend/backend task is large at scale (for example: more than 100 additional lines or changes), it might be a good idea to separate these tasks out into their own individual task. If a feature is smaller at scale (not more than 10 files changed), labeling it as fullstack would be suitable to review all at once. | Frontend, Backend, Fullstack |
| Stretch Goals | You can also label certain tasks as stretch goals - as a nice to have, but not mandatory for completing this project.                                                                                                                                                                                                           | Must Have, Stretch Goal      |
