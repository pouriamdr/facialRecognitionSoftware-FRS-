# Facial Recognition Software -FRS-
**Find someone by his/her picture in image database with python**
<h3>
Theory 
</h3>
Imagine that we have thousands of images of the faces of the employees of company x, and we are supposed to confirm the presence of employees at different hours in different departments of the company by the images recorded by the company's cameras.
<br>
The hypothesis is that the cameras take a picture of a person when they pass in front of them and save it. Now we want to prepare a report of the attendance of employees in different departments at the end of the working day.
<br>
The images are saved in the corresponding folder at the end of the working day. It is enough for our program to match the images in this folder with our image database and finally report a csv format file as output.
<br>
<h3>
Creating face database
</h3>
<hr>
We need personnel images of employees to separate their faces from the image and then store them in the faces folder.
<br>
We do this by running faceExtrator.py in terminal like this:<br><br>
Usage> Python3 faceExtrator.py pathToProfilePictures destinationOutput

```shell

python3 faceExtrator.py profilePictures faces

```

<br>
By now, we have all faces in faces folder!
<br>
<h3>
Time to action
</h3>
<hr>
It's time to findout who passed from which gate?(Imagine Camera is setup in gate input)
<br>
Now we need to run frs.py in command line:
<br><br>
Usage> Python3 frs.py cameraRollFolder facesFolder output

```shell

python3 frs.py cameraRolls/january03 faces rollcall/jan03.csv

```

output in jan03.csv will be like this:

```csv

employee,gate,time
e3,gate2,january03
e5,gate3,january03
e6,gate3,january03
e2,gate1,january03
e7,gate4,january03
e1,gate1,january03
e8,gate4,january03
e4,gate2,january03

```
<br>
<h4>
Outcome
</h4>
<hr>
To make this project more practical, we just need to write a program to save the image of people who pass in front of the camera. Therefore, I will also put the face recognition project through the camera in my repository.
<br>
## GOODLUCK
