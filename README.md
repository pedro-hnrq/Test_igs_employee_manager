


<h1 align="center"> Project test IGs Employee Manager </h1>


<h2 align='center'> Preview </h2>

![test_IGs](https://user-images.githubusercontent.com/74242717/230141908-d38a1f48-397e-40d3-9543-71eef4237a85.gif)


<h2 align='center'> Run Python Project and Django REST Framework</h2>

<p align="justify"> This document describes how to run Python and Django REST Framework project professionally. But first, make sure Python is installed on your machine. Highlighting, check which operating system it is, as it may have a small difference when called in the terminal, such as: Linux(Python3) and Windows(Python). </p>

<h3>Cloning the repository</h3>
<p align="justify">Download all project files by running the following command:</p>

```Markdown
git clone git@github.com:pedro-hnrq/Test_igs_employee_manager.git
```

<h3>Installing the dependencies</h3>
<p align="justify">Navigate to the cloned project folder and install all dependencies by running the following command:</p>

```Markdown
pip install -r requirements.txt
```

<h3>Running the migrations</h3>
<p align="justify">Run the Django database migrations: </p>

```Markdown
python3 manage.py makemigrations
```
<p align="justify"> </p>

```Markdown
python3 manage.py migrate
```

<h3>Creating a superuser</h3>
<p align="justify"> Crie um superusuário para acessar o painel administrativo do Django: </p>

```Markdown
python3 manage.py createsuperuser
```

- Go to http://127.0.0.1:8000/admin, access admin, register departments and then collaborators.

<h3>Running the server</h3>
<p align="justify"> To run the Django server, run the following command: </p>

```Markdown
python3 manage.py runserver
```
<p align="justify"> The server will be available at http://127.0.0.1:8000/.</p>

<h3>Viewing the data</h3>
<p align="justify">To view all employees, run the following command in the terminal: </p>

```Markdown
curl -H "Accept: application/json" http://127.0.0.1:8000/employee/
```
<p align="justify">To view a single employee by ID, run the following command in the terminal: </p>

```Markdown
curl -H "Accept: application/json" http://127.0.0.1:8000/employee/2/
```

<p align="justify"> The data can also be accessed through the web browser at the following addresses:</p>

- All employees: http://127.0.0.1:8000/employee/
- Employee by ID: http://127.0.0.1:8000/employee/2/

<p align="justify"> You can List, add, edit and delete employees:</p>

- http://127.0.0.1:8000/employee/list

