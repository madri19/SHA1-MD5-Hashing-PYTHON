#include what we need
import hashlib

#Read File       
inputFile = open('infile.txt', 'r')   
Lines = inputFile.readlines()        
inputFile.close()              

#Ready to writing to file    
outputFile = open('outfile.txt', 'w')  

#Process the hashes and write to file   
for line in Lines:                      
md5Hash = hashlib.md5(line.strip().encode())   
outputFile.writelines(md5Hash.hexdigest() + '\t\t//md for ' + line.strip() + '\n')        
sha1Hash = hashlib.sha1(line.strip().encode())  
outputFile.writelines(sha1Hash.hexdigest() + '\t//sha1 for ' + line.strip() + '\n')     

# Close the file we were writing to      
outputFile.close()       
