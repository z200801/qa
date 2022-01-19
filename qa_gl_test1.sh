#!/bin/sh

# Test tasks
# 1. Identify the current logged in user in a shell.
# 2. Identify the full name (the full path) of the current/working directory.
# 3. If the current/working directory is not current user's home directory, then go to the current user's home directory.
# 4. Create a directory there with the name of "My Test1".
# 5. Give permissions to "My Test1" directory so that the owner had full permissions, 
#   the owner's group had permissions to just read and write, and all others had permissions to just read.
# 6. Go to the "My Test1" directory and create a file there with the name of "step1".
# 7. List all files or directories in the current directory so that to be sure there is just 1 file, 
#   and its access permissions are the same as for the parent's directory.
# 8. Edit the file "step1", write the text "Your first step" there, and save the file.
# 9. Display the text of the "step1" file.
# 10. Copy file "step1" to the new file with the name of "step2".
# 11. Replace the word "first" with the word "second" in the file "step2".
# 12. Search and display all files inside the current directory that have the word "Your" in their text.
# 13. Substitute the word "Your" with the word "My" in all files inside the current directory.
# 14. Verify that the substitution was successful.
# 15. Go to the user's home directory.
# 16. Copy the entire directory "My Test1" with all the files inside to the new directory "My Test2".
# 17. List all files or directories in the current directory.

# The result of the task should be provided as a text copy of the command line with all input commands and their 
#   outputs (where applicable), or the screenshot of the console so that the commands input and output could be seen.

tt_4_dir="My Test1"
tt_5_perm="u+rwx-s,g+rw-s,o+r-t"
tt_5_fl1="step1"
tt_8_text="Your first step"
tt_10_fl1="step2"
tt_11_w1="first"
tt_11_w2="second"
tt_12_w1="Your"
tt_13_w1="Your"
tt_13_w2="My"
tt_16_dir='My Test2'

#clear
########################################################################
# Test task 1 
# Identify the current logged in user in a shell.
echo "#1 Task"
tt_1_logged_user=$USER
echo "Current logged user is:[$tt_1_logged_user]";echo


########################################################################
# Test task 2 
# Identify the full name (the full path) of the current/working directory.
#tt_2_cur_dir=`pwd`
echo "#2 Task"
tt_2_cur_dir=$PWD
echo "Current directory is:[$tt_2_cur_dir]";echo


########################################################################
# Test task 3
# If the current/working directory is not current user's home directory, then go to the current user's home directory.
echo "#3 Task"
# tt_3_user_home_dir=`cat /etc/passwd|grep "$tt_1_logged_user:"|awk -F : '{print $6}'`
# tt_3_user_home_dir=`getent passwd "$tt_1_logged_user" | cut -d: -f6`
tt_3_user_home_dir=$HOME
echo "Current directory is:[$tt_2_cur_dir]";echo
echo "User home directory is:[$tt_3_user_home_dir]";echo
if [ "$tt_2_cur_dir" != "$tt_3_user_home_dir" ]; then
    echo "User home directory is:[$tt_3_user_home_dir]"
    echo "Current directory is not user home directory"; 
    echo "Change directory to:[$tt_3_user_home_dir]";echo
    cd "$tt_3_user_home_dir"
fi


########################################################################
# Test task 4
# Create a directory there with the name of "My Test1".
echo "#4 Task"
echo "Make directory:[$tt_3_user_home_dir/$tt_4_dir]";echo
mkdir "$tt_3_user_home_dir/$tt_4_dir"

########################################################################
# Test task 5
# Give permissions to "My Test1" directory so that the owner had full permissions, 
# the owner's group had permissions to just read and write, and all others had permissions to just read.
# 1=Execute, 2=Write, 4=Read
echo "#5 Task"
echo "Change permission [$tt_5_perm] on directory:[$tt_3_user_home_dir/$tt_4_dir]";echo
#chmod u+rwx-s,g+rw-s,o+r-t "$tt_4_dir"
#chmod 00764 "$tt_4_dir"
chmod $tt_5_perm "$tt_3_user_home_dir/$tt_4_dir"

########################################################################
# Test task 6
# Go to the "My Test1" directory and create a file there with the name of "step1".
echo "#6 Task"
echo "Change directory to [$tt_4_dir] and create file [$tt_5_fl1]";echo
cd "$tt_4_dir"
touch $tt_5_fl1

########################################################################
# Test task 7
# List all files or directories in the current directory so that to be sure there is just 1 file, 
#   and its access permissions are the same as for the parent's directory.
echo "#7 Task"
tt_7_files=$(ls)
tt_7_files_n=$(echo $tt_7_files|wc -w)
echo "Files in directory is:[$tt_7_files_n], and name is: ["$tt_7_files"]"
echo "Number of files in directory is:[$tt_7_files_n]"
echo "Listing directory [$tt_3_user_home_dir/$tt_4_dir]"
ls -Al "$tt_3_user_home_dir/$tt_4_dir";echo
if [ "${tt_7_files_n}" -eq 1 ]; then
    echo "Files in directory is [${tt_7_files_n}], and name is: [$tt_7_files]"
    tt_7_dir_perm=$(stat -L -c "%a" $tt_3_user_home_dir/"$tt_4_dir")
    tt_7_file_perm=$(stat -L -c "%a" $tt_3_user_home_dir/"$tt_4_dir"/$tt_7_files)
    echo "Dir permissions [$tt_7_dir_perm] [$tt_3_user_home_dir/$tt_4_dir]"
    tt_7_f_name=$(echo $tt_3_user_home_dir/$tt_4_dir/$tt_7_files|sed 's/\.\///')
    echo "File permissions [$tt_7_file_perm] [$tt_7_f_name]"
    if [ ${tt_7_dir_perm} -eq ${tt_7_file_perm} ]; then echo "Directory and files is same permissions"
     else echo "Directory and files are not equivalent permissions";echo
    fi
else echo "Files in directory is:[$tt_7_files_n] and is over of 1";echo
fi


########################################################################
# Test task 8
# 8. Edit the file "step1", write the text "Your first step" there, and save the file.
echo "#8 Task"
echo "Editing file:[$tt_3_user_home_dir/$tt_4_dir/$tt_5_fl1]"
echo "Copy text:[$tt_8_text] in to file";echo
echo $tt_8_text>>"$tt_3_user_home_dir/$tt_4_dir/$tt_5_fl1"


########################################################################
# Test task 9
# 9. Display the text of the "step1" file.
echo "#9 Task"
echo "File contains:"
cat "$tt_3_user_home_dir/$tt_4_dir/$tt_5_fl1";echo

########################################################################
# Test task 10
# 10. Copy file "step1" to the new file with the name of "step2".
echo "#10 Task"
echo "Copy file [$tt_5_fl1] to [$tt_10_fl1]";echo
cp $tt_5_fl1 $tt_10_fl1


########################################################################
# Test task 11
# 11. Replace the word "first" with the word "second" in the file "step2".
echo "#11 Task"
echo "Replace in file:[$tt_10_fl1] word:[$tt_11_w1] to [$tt_11_w2]"
sed "s/$tt_11_w1/$tt_11_w2/g" -i $tt_10_fl1
echo "Check visual:"
cat $tt_10_fl1;echo


########################################################################
# Test task 12
# 12. Search and display all files inside the current directory that have the word "Your" in their text.
echo "#12 Task"
echo "Search all files contain word:[$tt_12_w1] on a current directory:[$PWD]"
grep -Rl "$tt_12_w1" "$PWD"
echo

########################################################################
# Test task 13
# 13. Substitute the word "Your" with the word "My" in all files inside the current directory.
echo "#13 Task"
echo "Change word:[$tt_13_w1] to [$tt_13_w2] on a all files inside current directory";echo
find "$PWD" -name "*" -type f ! -path "." -exec sed "s/$tt_13_w1/$tt_13_w2/g" -i {} \;

########################################################################
# Test task 14
# 14. Verify that the substitution was successful.
echo "#14 Task"
tt_14_f1_w1_f=$(grep -Rl "$tt_13_w1" "$PWD")
tt_14_f1_w1_c=$(echo $tt_14_f1_w1_f|wc -w)
if [ ${tt_14_f1_w1_c} -ne 0 ]; then
    echo "Not at all files is substitudes"
    echo "Files can't be substitides is:[$tt_14_f1_w1_f]";echo
else echo "Files contains word:[$tt_13_w1] inside directory is:[$tt_14_f1_w1_c]";echo
fi


########################################################################
# Test task 15
# 15. Go to the user's home directory.
echo "#15 Task"
echo "Change directory to user home directory:[$HOME]";echo
cd "$HOME"

########################################################################
# Test task 16
# 16. Copy the entire directory "My Test1" with all the files inside to the new directory "My Test2".
echo "#16 Task"
echo "Copy recursive directory:[$tt_4_dir] to [$tt_16_dir]";echo
cp -R "$tt_4_dir" "$tt_16_dir"


########################################################################
# Test task 17
# 17. List all files or directories in the current directory.
echo "#17 Task"
echo "Lists directory $PWD"
echo "The contents of the directory are the property of others.";echo
#ls -la
echo "List directory $tt_4_dir"; ls -lA "$HOME/$tt_4_dir";echo
echo "List directory $tt_16_dir"; ls -lA "$HOME/$tt_16_dir"

########################################################################
echo
echo "Remove directory: [$HOME/$tt_4_dir]"; rm -rf "$HOME/$tt_4_dir"
echo "Remove directory: [$HOME/$tt_16_dir]"; rm -rf "$HOME/$tt_16_dir"
