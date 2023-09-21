# BOSSDesk API Integration

This script provides a simple integration with the BOSSDesk API, specifically targeting the Configuration Management Database (CMDB) endpoint to fetch and count available laptops.

## Prerequisites
- Python 3.x
- **requests** library: For making HTTP requests.
- **python-dotenv** library: For loading environment variables from a .env file.

## Installation

1. Clone this repository:
```powershell
git clone [URL of your repo]
```
2. Navigate to the project directory:
```powershell
cd [project-directory]
```
3. Install the required packages:
```powershell
pip install requests python-dotenv
```
## Usage

1. Ensure that you have set up your *.env* file as described in the Configuration section.
2. Run the script:
   
```powershell
python [script-name].py
```
The script will output the number of available laptops based on the API's response.

## Configuration

Configuration is managed through a **.env** file. Create a **.env** file in the root directory of the project and specify the required environment variables:
```powershell
BOSSDESK_API_TOKEN=your_token
API_ENDPOINT=https://mycompany.bossdesk.io/api/v1/cmdb
```
- **BOSSDESK_API_TOKEN**: Your BOSSDesk API token for authentication
- **API_ENDPOINT**: The endpoint URL of the BOSSDesk API you are targeting.

*Note: Ensure that you never commit the .env file to the version control to keep sensitive data secure*

## Contributing 

1. Fork the repository.
2. Create a new branch for you changes
3. Make your changes and commit them with meaningful commit messages
4. Open a pull request

Remember to replace placeholders like [URL of your repo] and [script-name].py with appropriate values for your repository and script.
