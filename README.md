# PDI-Capstone-Weather-Dashboard
Python app that looks up the weather.

## Capstone Notes

For this project option you will write a command-line application that allows users to get the current weather for a specified city using an API.

### Features:

Get Weather: User can enter a city name and get the current weather.

Here's where to start with your code:

Display a prompt for the user to enter a city name.

Use the requests library to make a GET request to the weather API with the city name.

Parse the response and display the weather data (temperature, humidity, etc.).

Please note that this application requires using an API to retrieve the weather data, which involves understanding how to interact with APIs and parse JSON responses.

So you'll have to sign up for a service like [OpenWeather](https://openweathermap.org/) to get an API, and work with the [requests library](https://codechalleng.es/tips/requests-module) to retrieve data from the API.

Work closely with your coach to implement this app.




## Bonus Requirements (OPTIONAL)

If you happen to move fast through your capstone project you have two options:

1. Do another one. In that case go through the previous sections.

2. Go deeper implementing more advanced features. In that case, here are 3 things you can do:

### 1. Data Persistence

Currently, the data for each application is stored in memory and is lost when the program ends. To make the applications more realistic and useful, students could implement data persistence using a simple database or file system.

Pseudo Code:

Define a function to save data to a file or database when a task is added, deleted, or completed (for the Todo List or Budget Tracker) or when a city's weather is retrieved (for the Weather Dashboard).

Define a function to load data from the file or database when the program starts.

### 2. Data Visualization

Data visualization can provide a more intuitive understanding of data and make the applications more engaging.

Pseudo Code:

Todo List: Display a pie chart showing the percentage of completed vs. remaining tasks.

Budget Tracker: Display a bar chart showing each expense category and its value.

Weather Dashboard: Display a line chart showing the temperature changes throughout the day for a specified city.

### 3. Improved User Interface

While the command-line interface (CLI) is simple and straightforward, it might not be the most user-friendly or appealing way to interact with an application. Students could improve the user experience by creating a graphical user interface (GUI) for their applications.

Pseudo Code:

Use a library such as [Rich](https://github.com/Textualize/rich) / [PySimpleGUI](https://www.pysimplegui.org/en/latest/) / [Textual](https://textual.textualize.io/) to create a simple GUI for each application. This GUI could include input fields for adding tasks or expenses, buttons for performing actions, and display areas for showing tasks, expenses, or weather data.

### 4. Write tests

A trademark of a good developer is that they always ship their code with tests. So another option we provide here is to write tests for your project using [pytest](https://docs.pytest.org/en/7.3.x/).

---

Please note that these tasks are optional and more complex. They involve using external libraries so we will provide extra resources based on your needs as well as live 1:1 coaching to get through this. Just discuss this with your coach ...