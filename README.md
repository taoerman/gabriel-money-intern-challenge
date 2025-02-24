# Backend Intern Challenge
This repo is for the backend intern challenge at Gabriel Money.

The API is written in Python and is deployed to AWS using API Gateway and Lambda. Data is stored in MongoDB.

## Instructions to call API
**Base URL**: https://0q4kallc56.execute-api.us-west-1.amazonaws.com/v1/  
**API Key**: JtzlG77Taj2KOSNpJHGiBAOh3xyVwc32Gf9w8DH5

Please add ```{x-api-key: JtzlG77Taj2KOSNpJHGiBAOh3xyVwc32Gf9w8DH5}``` to the request header to access the API. For example, use the command below to send a POST request:

```
curl --location --request POST 'https://0q4kallc56.execute-api.us-west-1.amazonaws.com/v1/users/?first_name=John&last_name=Doe' \
--header 'x-api-key: JtzlG77Taj2KOSNpJHGiBAOh3xyVwc32Gf9w8DH5'
```

[Here](https://www.postman.com/speeding-flare-720130/gabriel-money/request/571jg0s/test-api?tab=overview) is an example in Postman.

## Bonus Challenges
### Serverless Architecture
The API has been deployed using AWS API Gateway and Lambda. All requests are routed to a single lambda function, since this challenge is about a single resource (i.e., user). The lambda function ```src/handle_user_operation.py``` will decide which handler to call based on the path and HTTP method.

This GitHub repo has been configured to deploy code changes to AWS lambda automatically for pushes into the main branch using GitHub Action. The ```.github/workflows/lambda-deploy.yaml``` file lists all steps to automate the deployment, including:
- Create Python virtual env
- Install dependencies
- Run tests
- Zip code and dependent libraries
- Deploy to AWS Lambda

### Clean Code
Steps taken to ensure the code readability and maintainability:
- Added tests for each file. Tests are written in the Arrange-Action-Assert pattern.
- Automated deployment to AWS Lambda.
- Added pre-commit config that runs hooks like black and isort to fix code format issues automatically before committing.

### Architecture Diagram
![diagram](https://github.com/user-attachments/assets/2b2c60cb-d0a6-4e5b-8f0d-5d931e021286)

### MongoDB
The data is stored into MongoDB.
