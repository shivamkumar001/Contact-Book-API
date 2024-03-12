Contact Book API
The Contact Book API is a RESTful web service that allows users to manage their contacts. It provides endpoints for creating, reading, updating, and deleting contacts, as well as authentication features for secure access.

Features
User Authentication: Users can register, log in, and receive authentication tokens to access protected endpoints.
Contact Management: CRUD operations for managing contacts, including adding, viewing, updating, and deleting contacts.
Search Contacts: Search contacts by various criteria such as name, email, or group affiliation.
Grouping Contacts: Organize contacts into groups for easier management.
Secure Communication: All communication with the API is secured using HTTPS.

Installation

Clone the repository:
git clone https://github.com/shivamkumar001/Contact-Book-API.git

Install dependencies:
pip install -r requirements.txt

Set up MongoDB:
Install MongoDB on your system.
Create a MongoDB database and configure the connection settings in config/db.py.

Run the API:
uvicorn index:app --reload

Access the API:
Open your web browser and navigate to http://localhost:8000/docs to access the Swagger UI documentation and interact with the API endpoint
