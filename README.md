# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY : CODTECH IT SOLUTIONS

NAME : HIMANSHU RAWAT

INTERN ID : CT04DH2741

DOMAIN : PYTHON PROGRAMING

DURATION : 4 WEEKS

MENTOR NAME : NEELA SANTOH

# DISCRIPTION ABOUT THIS PROJECT
---- Title: Weather Data Visualization Dashboard Using Python ----

This project, titled “Weather Data Visualization Dashboard”, is a practical Python-based application designed to fetch live weather forecast data from a public API and represent it visually using popular data visualization libraries — Matplotlib and Seaborn. The objective of this project is to provide users with an easy-to-understand graphical dashboard of temperature and humidity trends for any given city using real-time data from OpenWeatherMap.

The application connects to the OpenWeatherMap API, which provides weather data in JSON format. The forecast used in this project is the 5-day forecast API, which provides temperature, humidity, wind speed, and other environmental metrics for every 3-hour interval. The API is accessible freely after registration and is suitable for learning, experimentation, and small projects. I obtained the API key by signing up at the official OpenWeatherMap website: 🔗 https://openweathermap.org/api

After obtaining the API key, the Python script makes a GET request to the OpenWeatherMap endpoint using the requests library. The JSON response is parsed to extract timestamps, temperatures, and humidity values, which are then stored in Python lists. These lists are further processed to generate a clean and professional weather dashboard.

To create the dashboard, I used Matplotlib for plotting and Seaborn for enhanced visual styling. The final output consists of two line plots displayed in a single figure:

The first graph shows the temperature forecast (in °C) over time.

The second graph shows humidity levels (%) over the same timeline.

The x-axis represents time (in 3-hour intervals), and the y-axis represents either temperature or humidity depending on the chart. The visualizations are clean, labeled properly, and easy to interpret. The dashboard is saved as an image file (weather_dashboard.png) using plt.savefig(), which allows it to be submitted in reports or shared digitally.

--- Learning Sources and Credits:-----

I would like to acknowledge the following sources of help and guidance that contributed to the successful completion of this project:

ChatGPT ChatGPT provided consistent, step-by-step support during project development, from helping understand the OpenWeatherMap API structure to writing clean and structured Python code. It also guided in formatting the visualizations using Matplotlib and Seaborn, and helped create exportable dashboards.

YouTube Tutorials Several YouTube tutorials helped me understand API integration with Python, especially for beginners. These videos gave visual demonstrations on how to use the requests library and how to process JSON data. I referenced videos by creators like Tech With Tim, Programming Hero, and freeCodeCamp for general API and data visualization concepts.

OpenWeatherMap API Special thanks to OpenWeatherMap for offering free access to a robust and easy-to-use weather data API. Their clear documentation made it simple to construct proper API requests and extract the required data.

# OUTPUT
<img width="1456" height="832" alt="Image" src="https://github.com/user-attachments/assets/7fbad54e-b22e-40f8-82fc-e301c8f5eea5" />
