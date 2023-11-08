
# Random Memes App using Flask
It gives you random memes from reddit using the reddit memes api(not Official)

Api repo link : https://github.com/D3vd/Meme_Api





## How to use the project

1.Setup virtual environment :

    pip install virtualenv
    
    
    virtualenv {your environment name}

    e.g - 
    virtualenv env

2.Activate the virtual environment:

    {environment_name}\Scripts\activate.bat
                    
                    or
                    
    {environment_name}\Scripts\activate.ps1

    e.g-

    env\Scripts\activate.bat                

3.Install the required packages:

    pip install -r requirements.txt

    #this will install all the required packages

4.Add these 2 lines if you are using it as a project and not for deployment:

    if __name__ == "__main__":
        app.run(debug=True)

5.Now run the flask application:


    python app.py


    
    
