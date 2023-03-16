# Python Software Engineer - Home coding chanllenge
Welcome to our home coding challenge! We appreciate you taking the time to complete this challenge as part of our selection process. The purpose of this challenge is to assess your skills and abilities as a developer, and to get a sense of how you approach and solve problems.

We believe that this challenge will provide you with an opportunity to showcase your knowledge and experience with API development, as well as your proficiency in working with databases, data transformation and error handling. We want to encourage you to use best practices as you work on this challenge on the same way you would do it i a real world project.

Each user story has a number that tells us how long we think it will take to finish the task. We call this number the "ETT", which stands for "Estimated Time to Task". This helps us understand how hard the task is and how long it might take to finish. Take this time just as a reference.

## Coding challenge: Problem to solve
As a Senior Python Engineer at "Lazarillo de Tormes," a successful e-commerce platform offering high-quality products at affordable prices, the company has asked for you assistance with their expansion into Asia. They see great potential for growth and success in this region and have set their sights on this new venture. As an integral member of the team, you will leverage your expertise and experience to help the company navigate the challenges of expanding into new markets.

On a typical day, you arrive at the office and check the task board to review your assigned tasks and you can see there user stories.

### LDT-1: Integrate a web server framework
As a developer working on the current code base, I want to choose and integrate a new web server framework to improve the scalability and maintainability of the application.

Acceptance Criteria:

- The new web server framework must be compatible with the current code base and its dependencies.
- The framework must have strong community support and active development.
- The integration process must not introduce any significant performance issues or breaking changes to the application.
- The framework must provide clear documentation and examples to facilitate its adoption and usage.

Tasks:
- Choose a framework that you are well-versed.
- Test the integration thoroughly, making any necessary adjustments to ensure that it works correctly and does not introduce any issues.
- Update the application's documentation and provide training to the team on how to use the new framework.

ETT: 30 min


### LDT-2: Create users
As a user of the REST API,
I want to be able to create a new user and subscribe to specific Asian countries,

Acceptance Criteria:
- The new endpoint should be called "POST /users"
- The endpoint should accept a JSON payload containing user information, including the user's name, email, and a list of Asian countries the user wants to subscribe to.
- If the user already exists, the endpoint should return a 409 Conflict error.
- If the payload is missing any required fields, the endpoint should return a 400 Bad Request error.
- If the user is successfully created, the endpoint should return a 201 Created status code and the user's ID in the response body.

Tasks:
- Create a new database table to store user information.
- Add validation to ensure the required fields are present in the payload.
- Add validation to ensure that the user doesn't already exist.
- Implement the logic for creating a new user and storing their information in the database.
- Implement the logic for updating the user's list of subscribed countries.
- Write unit tests to ensure the endpoint works as expected.
- Update the API documentation to include information about the new endpoint.

Assumptions:
- Authentication is not required for this API

ETT: 30-60 min


### LDT-3: Show country information
As a user of the REST API,
I want to be able to retrieve information about the countries I have subscribed to,

Acceptance Criteria:
- The new endpoint should be called "GET /users/{userId}/countries"
- The endpoint should accept the user's ID as a path parameter.
- The endpoint should return a list of JSON objects, each containing information about a country the user has subscribed to.
- The information returned should be based on [Lowi Institute Public API](https://power.lowyinstitute.org) data.
- For each of the countries, the response should include: the score an the power data since 2018.
- The `score` for a country in a year is the `score` in the Lowi Index
- The `power` for a country in a year is the sum of `trend`, `influence`, `resources` and `espected`
- If the user does not exist, the endpoint should return a 404 Not Found error.
- If the user has not subscribed to any countries, the endpoint should return 200 OK status code with an empty list.

Tasks:
- Add a new route to the API for the "GET /users/{userId}/countries" endpoint.
- Implement logic for retrieving the list of countries the user has subscribed to.
- Implement logic for making requests to the public API to retrieve information about each country.
- Transform the data from the public API into the required JSON format.
- Handle errors that may occur during the retrieval of the country information.
- Write unit tests to ensure the endpoint works as expected.
- Update the API documentation to include information about the new endpoint.

Assumptions:
- The required information about the countries is available from the public API.

ETT: 60 min

## Instructions
1. Fork the Gitlab repository provided to you.
2. Read the instructions provided in this README file carefully and complete the coding challenge accordingly.
3. When you have completed the challenge, please send an email to the person who assigned you the coding challenge to let them know that you have finished and provide them with a link to your repository.

## Guidelines
- This repository is specifically created for you to complete the coding challenge. It has been designed to provide you with a ready-to-use workspace that includes all the necessary files, folders and documentation to successfully complete the challenge
- There is no time limit for completing the challenge, take as much time as you need to complete it.
- Feel free to select any Python web framework that you prefer. Some well-known choices are Django, Flask and FastAPI, but don't hesitate to use any other web framework that you feel comfortable with, or even none at all.
- Make sure all commands described in the documentation are working, including the continuous integration (CI) process.
- Please keep the project folder structure as provided in the repository. This will help ensure consistency and make it easier for reviewers to navigate your code.
- Do not make any changes to the original repository provided to you. All your changes should be made in your forked repository.

## Evaluation the challenge: What we pay attention to
When evaluating the challenge, we pay attention to several factors to assess the candidate's skills and suitability for the role. Here are some of the key areas that we typically focus on:

### Functionality and completeness
We will check whether the code meets all the requirements specified in the challenge instructions.

Addtionally, we will test the code to see if it handles edge cases and error conditions correctly. This includes things like handling unexpected inputs or error conditions gracefully and ensuring that the code does not crash or produce unexpected results.

### Code quality and organization
We will assess whether the code is easy to read and understand, and whether it follows established best practices for code readability. This includes things like using consistent naming conventions, using clear and concise comments and breaking up code into logical sections.

In addition to the above criteria, we will also pay attention to whether the candidate's code follows established best practices and conventions for Python programming.

### Git and version control
We will assess whether the candidate is proficient in using Git for version control.

We will assess the frequency and granularity of the candidate's commits, and whether they are making regular and meaningful commits throughout the development process.

We will assess the quality of the candidate's commit messages, including whether they are descriptive and explain the changes made in each commit.

We will assess whether the candidate is using branching and merging effectively to manage the development process, and whether they are following established best practices for Git workflow or a similar brancking well-tested branching system.

### Documentation
We will assess the quality of the candidate's documentation, including whether it is clear, concise and comprehensive, and whether it provides useful information for other developers who may be working on the code in the future.

We will assess whether the candidate's documentation covers all relevant aspects of the code.

### Development process and decision made
We will assess the candidate's ability to design and architect software systems effectively, including making decisions about system architecture, data models and API design.

We will assess the candidate's approach to testing and quality assurance, including whether they are writing automated tests, using code reviews and other techniques to ensure code quality and taking steps to prevent and mitigate errors and bugs.


## Working with this repo

### Pre-requirements
The only requirement to get this project up and running is to have [Docker installed](https://docs.docker.com/engine/install/) on your system.

### Branches
The only branch provided in the repository is *main*. However, you are free to create and organize additional branches as necessary to complete your work.

### Commands
Run the project
```bash
docker compose up --build
```

Test with pytest
```bash
docker compose run --rm web-server python -m pytest
```
