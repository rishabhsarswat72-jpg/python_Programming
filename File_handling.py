# # #question 1
# def write_lines(filename,lines):
#     with open(filename,'w')as file:
#         for line in lines:
#             file.write(f"{line}\n")
# names=["rishabh","ronak","ashok"]
# write_lines("names.txt",names)

# # #question 2
# import os
# def count_lines(filename):
#     if os.path.exists(filename):
#         with open(filename,'r') as file:
#            return sum(1 for line in file)
#     else:
#         return "error:file not found"
# print(count_lines("rishabh.txt"))

# # question 3
# with open("source.txt",'r')as file1:
#     with open("dest.txt",'w')as file2:
#         for line in file1:
#             file2.write(line)

# #question 4
import os

entry = "new entry\n"
mode = "a" if os.path.exists("data.txt") else "w"

with open("rishabh.txt", mode) as file:
    file.write(entry)
    
#question 5
# import csv

# def read_csv_rows(filename):
#     with open(filename, mode= 'r') as file:
#         reader = csv.reader(file)
#         next(reader, None)  
#         return  list(reader)
# print(read_csv_rows("source.csv"))
# question 6
# import csv

# def average_score(filename):
#     with open(filename, mode='r') as file:
#         scores = [float(row['Score']) for row in csv.DictReader(file)]     
#     if not scores:
#         return 0.0 
#     return round(sum(scores) / len(scores), 1)
# print(average_score("source.csv"))
#question 7
# import datetime

# def append_log(message, logfile="app.log"):
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open(logfile, mode='a', encoding='utf-8') as file:
#         file.write(f"[{timestamp}] {message}\n")
# append_log("hello my name is rishabh","app.log")
# append_log("this is a python file handling program","app.log")

#question 8
# total_sum = 0

# with open("numbers.txt", mode="r") as file:
#     for line in file:
#         clean_line = line.strip()
#         if clean_line:  # Skip blank lines
#             total_sum += int(clean_line)

# print(total_sum)

#question 9
# import csv

# def write_students_csv(filename, data):
#     with open(filename, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
# student_data = [
#     ["Name", "Age", "Grade"],
#     ["rishabh", "15", "10"],
#     ["nikhil", "16", "11"]
# ]
# write_students_csv("students.csv", student_data)
#question 10
import os

def safe_read(filename):
    if os.path.exists(filename):
        with open(filename, mode="r") as file:
            return file.read()
    return "FILE NOT FOUND"
print(safe_read("dest.txt"))
#question 11
import csv
with open("students.csv", mode="r", newline="") as infile, \
     open("top_students.csv", mode="w", newline="") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        if float(row["Score"]) >= 90:
            writer.writerow(row)
#question 12

with open("data.txt", "r") as f:
    print((f.read()))

with open("data.txt", "r") as f:
    print((f.readline()))

with open("data.txt", "r") as f:
    print(f.readlines())
    
#question 13
def word_count(filename):
    counts = {}
    with open(filename, mode="r") as file:
        for line in file:
            for word in line.split():
            
                clean_word = word.strip(".,!?;:\"'()[]{}").lower()
                if clean_word:  
                    counts[clean_word] = counts.get(clean_word, 0) + 1
    return counts
#question 14
with open("data.txt", mode="w+") as file:
    file.write("First line\nSecond line\nThird line\n")
    file.seek(0)

    print(file.read())

#question 15
def merge_files(file_list, output_filename):
    with open(output_filename, mode="w") as outfile:
        for filename in file_list:
            outfile.write(f"--- {filename} ---\n")
            
            with open(filename, mode="r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                
            outfile.write("\n")
merge_files(["source.txt", "dest.txt"], "combined.txt")



    






