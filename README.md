# Setting up the API

NOTE: SECRET_KEY and SQLALCHEMY_DATABASE_URI are set to ENVIRONMENT variables. Modify your bashrc or other shell initializiation folder (zshrc, or set using windows commands if on that OS | you can set these values to anything at the moment, but these will be importantly hidden out of production code for security reasons when the program is deployed. we just want to make sure these values can be accessed by our code during development. see config.py)  
Example for configuring environment variables:  
<code>vi ./bashrc</code>  
Add SECRET_KEY and SQLALCHEMY_DATABASE_URI environment variables:  
<code>export SECRET_KEY='SuperSecretKey'</code>  
<code>export SQLALCHEMY_DATABASE_URI='postgresql://postgres:password@localhost/health'</code>  
Above command assumes that you have a PostgreSQL database on the localhost named 'health'  


1. This application is currently under development using Python 3.8.10. 
2. In order to launch the site, you will need to set up the virtual environment first.
3. Once you have set up/cloned the repository, navigate to the top level directory. (contains <code>health_app/</code> folder, <code>requirements.txt</code>, etc.)
4. Create a new virtual environment in the top level directory by running the command <code>python3 -m venv venv/</code>, which will create a directory venv/ with the enviroment. 
5. Activate the virtual environment by running <code>source venv/bin/activate</code> while in api directory. 
6. Update the enviroment with the necessary dependencies from <code>requirements.txt</code> by running the command <code>pip3 install -r requirements.txt</code>
7. Once your venv is activated and the dependencies are installed, you can launch api by running <code>flask run</code> while in the top level directory.
8. Once you have set up a PostgreSQL database and configured the environment variables as necessary (see above), you can populate the database with mock data by running the script, <code>populate_db.py</code> located in <code>api/script</code> (remember to launch the api before executing the script or else the requests won't go through)

# Setting up the front end

1. Navigate to <code>frontend/</code>
2. Install dependencies: <code>npm install</code>
3. Run the application: <code>npm run dev</code>
