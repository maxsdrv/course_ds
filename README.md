# course_ds
math for data science

# Configure
I recommend use to VSCode, cause convinience for adjusting project for DataScience. 

## Describe



Visual Studio Code and the Python extension provide a great editor for data science scenarios. With native support for Jupyter notebooks combined with Anaconda, it's easy to get started. In this section, you will create a workspace for the tutorial, create an Anaconda environment with the data science modules needed for the tutorial, and create a Jupyter notebook that you'll use for creating a machine learning model.

    Begin by creating an Anaconda environment for the data science tutorial. Open an Anaconda command prompt and run conda create -n myenv python=3.9 pandas jupyter seaborn scikit-learn keras tensorflow to create an environment named myenv. For additional information about creating and managing Anaconda environments, see the Anaconda documentation.

    Next, create a folder in a convenient location to serve as your VS Code workspace for the tutorial, name it hello_ds.

    Open the project folder in VS Code by running VS Code and using the File > Open Folder command. You can safely trust opening the folder, since you created it.

    Once VS Code launches, create the Jupyter notebook that will be used for the tutorial. Open the Command Palette (Ctrl+Shift+P) and select Create: New Jupyter Notebook.

    Creating a new Jupyter Notebook

        Note: Alternatively, from the VS Code File Explorer, you can use the New File icon to create a Notebook file named hello.ipynb.

    Save the file as hello.ipynb using File > Save As....

    After your file is created, you should see the open Jupyter notebook in the notebook editor. For additional information about native Jupyter notebook support, you can read the Jupyter Notebooks topic.

    Viewing a new Jupyter Notebook

    Now select Select Kernel at the top right of the notebook.

    Selecting a Jupyter Notebook Kernel

    Choose the Python environment you created above in which to run your kernel.
