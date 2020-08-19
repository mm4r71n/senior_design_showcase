# Final-Project
Construction App: This application allows property owners to upload and modify their listings information and images,
and displays this information to the clients dynamically.
Built using Python, Django, PostgreSQL, JavaScript, Bootstrap ,HTML, CSS

Directory set up:

>Contruction_App- Name of the project and inside cotains all the necessary files for the project. This projet containes 3 installed apps. contacts, listings, and pages. EVERY APP contains a models.py, views.py, and urls.py. 
  >ContructionApp: Contains the settings.py file where you will be able to add any other apps you wish to install, as well as the static    folder which contains all of the styling and images for the project. 
  
    >contacts: The contacts app takes care of the logic(views), models, and urls for when users want to make an inquiry about a certain property listing.
    
    >listings: The listings app takes care of the logic(views),models, and urls to display proper information from the database. 
    
    >media: A folder dedicated to organizing images uploaded to the admin side. 
    
    >pages: App dedicaed to the home page of the website. Views file dictates the number of current listings shown on the home page. 
    
    >static: This folder is for production purposes. When this app is ready to be used in production all of the static files will be read  from this folder.
    
    >templates: This folder contains all the HTML templates used to render the views.py data in. You can add new html files here. 


