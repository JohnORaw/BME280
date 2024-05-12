
#!/bin/bash

#clear
echo "**********************************************"
echo This batch file will create a project directory
echo "**********************************************"
echo "*** press [ctrl][c] to exit or [return] to continue ***"
read
echo "Enter the name of the project, then press [return]"
read NAME
echo "Creating directory" $NAME
if [ -d $NAME ]; then
   cd $NAME
else
  mkdir $NAME
  cd $NAME
  mkdir Documentation
  mkdir Tests
  mkdir Examples
  mkdir Source
  ls -l 
fi

echo "**********************************************"
echo "Finished creating project $NAME"
echo "**********************************************"  
