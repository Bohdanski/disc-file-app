:: Assign current working directory (root directory) to variable X
set X=%CD%

:: #Change file name here
::python tests.py
python disc_file_app.py



:: #Transfer file to w-drive for SQL Server Import
MOVE "C:\Users\tubxt2p\Documents\Python\python-projects\disc-file-app\MfDiscItems*txt" "W:\DecisionSupport\SQL\MfDiscItems\"