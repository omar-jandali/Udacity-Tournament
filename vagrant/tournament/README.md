There are a few ways to run the code that will display the tournament and results.

The best way to do so is to first download the following:
  VirtualBox - https://www.virtualbox.org/
  Vagrant - https://www.udacity.com/wiki/ud088/vagrant?_ga=1.171014112.191927602.1462383533

2_Then once you have those donwloaded throght your terminal or gitbash redirect to the directory
  in which you save the vagrant file.

3_Once you get to the vagrant file, type the following in and run it "vagrant up"
  you will see a bunch of actions and installations going on within the folder

4_once that is complete simply type "vagrant ssh" which will activate the virtual machine server

5_once it has worked redirect to the tournament folder
    [cd /vagrant/tournament]

6_Once in the folder, type "psql -f tosurnament.sql" and hit enter, followed by"python tournament-test.py" which will run and create the neccessary
  database and tables that are needed for you to run the project.

7_ repeat step 6 and then you will be able to see that the project is running thorugh a port on your local machine

8_you will receive the http portal which will allow you to acces the local files

9_in the browser, type localhost and the portal number that you earlier to run the code
