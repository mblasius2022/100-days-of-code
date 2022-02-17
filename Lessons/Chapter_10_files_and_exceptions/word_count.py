def count_words(file_name):
    """ count the approximate number of words in a text file"""
        # count number of words
        words = contents.split()
        num_words = len(words)
    try:
        file_path = '/home/ec2-user/environment/100-days-of-code/Lessons/Chapter_10/'
        file_location = file_path + file_name
        with open(file_location, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Could not find file {file_name}")
        pass
    else:
        print(f"File {file_name} has approximtely {num_words} words")


file_names = ['git.text','alice.txt']
for file_name in file_names:
    count_words(file_name)
