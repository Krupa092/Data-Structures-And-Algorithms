import os 

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path == None:
        return None
    elif not os.path.exists(path):
        print("Invalid input path")
    else:
        files = [] 
        directory = os.listdir(path)
        #to walk in to the folder
        for i in directory:
            #To store built list temporary
            list_path = os.path.join(path,i)
            #used recursion 
            if os.path.isfile(list_path) and list_path.endswith(suffix):
                files.append(list_path)
            if os.path.isdir(list_path):
                files +=find_files(suffix,list_path)
        return files 
        

#*****************************Test Case 1*****************************
print("Testing Function With Given Library")      
print(find_files(".c","C:/Users/KDAVE7/Desktop/Udacity/Python/Data_Structure_and_Algorithms/Data_structures/Project2/Project2/testdir")) #static path

#*****************************Test Case 2*****************************
print("Testing Function With Given Library")      
print(find_files(".c","C:/Users/KDAVE7/Desktop/Python/Data_Structure_and_Algorithms/Project2/testdir")) #Invalid Path

#*****************************Test Case 3*****************************
print("Testing Function With Given Library")      
print(find_files(".w","C:/Users/KDAVE7/Desktop/Udacity/Python/Data_Structure_and_Algorithms/Data_structures/Project2/Project2/testdir")) #blank return