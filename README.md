# course_ds
math for data science

# Configure
I recommend use to VSCode, cause convinience for adjusting project for DataScience. 

## Describe



Visual Studio Code and the Python extension provide a great editor for data science scenarios. With native support for Jupyter notebooks combined with Anaconda, it's easy to get started. In this section, you will create a workspace for the tutorial, create an Anaconda environment with the data science modules needed for the tutorial, and create a Jupyter notebook that you'll use for creating a machine learning model.

1. Begin by creating an Anaconda environment for the data science tutorial. Open an Anaconda command prompt and run conda create -n myenv python=3.9 pandas jupyter seaborn scikit-learn keras tensorflow to create an environment named myenv. For additional information about creating and managing Anaconda environments, see the Anaconda documentation.

2. Next, create a folder in a convenient location to serve as your VS Code workspace for the tutorial, name it hello_ds.

3. Open the project folder in VS Code by running VS Code and using the File > Open Folder command. You can safely trust opening the folder, since you created it.

4. Once VS Code launches, create the Jupyter notebook that will be used for the tutorial. Open the Command Palette (Ctrl+Shift+P) and select Create: New Jupyter Notebook.

Creating a new Jupyter Notebook

![create-notebook](https://user-images.githubusercontent.com/34602478/213167614-36833ead-e99a-430e-accb-c309e88e8dad.png)

Note: Alternatively, from the VS Code File Explorer, you can use the New File icon to create a Notebook file named hello.ipynb.

5. Save the file as hello.ipynb using File > Save As....

6. After your file is created, you should see the open Jupyter notebook in the notebook editor. For additional information about native Jupyter notebook support, you can read the Jupyter Notebooks topic.

![notebook-editor](https://user-images.githubusercontent.com/34602478/213168162-8cfd84e6-227a-422f-b720-d0bb1c42d67c.png)

Viewing a new Jupyter Notebook

7. Now select Select Kernel at the top right of the notebook.

Selecting a Jupyter Notebook Kernel

![select-kernel](https://user-images.githubusercontent.com/34602478/213168331-8666fa79-0b98-4079-963c-7c48828f38f5.png)

8. Choose the Python environment you created above in which to run your kernel.

![choose-myenv](https://user-images.githubusercontent.com/34602478/213168441-a5713c84-5c9f-4c7f-a1ae-abb2cfc882be.png)

