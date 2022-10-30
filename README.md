#Install virtual environment
	
		py -m venv myenv 

#Install all additional packages from requirements.txt. You should write:
	
		pip install -r requirements.txt 

#Done! You can turn on server 

		py manage.py runserver

#In order to peruse you may write below code in yout CLI 
	
		curl http://127.0.0.1:8000/

#Many developers forget to test a project, so we will not !. I've added some codes in test.py. You can check

		py manage.py tests.py

#Enjoy