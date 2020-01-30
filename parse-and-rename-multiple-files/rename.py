import os

# Change directory to that which holds the files
os.chdir('/Users/maxbigbudget/Work/Projects/pythonic-concepts/parse-and-rename-multiple-files/music-files')
# print (os.getcwd()) - shows am in the said directory

# Loop thru all files like in current dir() like: Walker - Playlist - #1.mp3
for f in os.listdir():
    # split extension using path.splitext in tuple like ('Walker - Playlist - #1', '.mp3')
    filename, file_ext = os.path.splitext(f)

    # split filename on '-' into a list like ['Walker ', ' Playlist ', ' #1']
    f_artist, f_title, f_number = filename.split('-')

    f_artist = f_artist.strip()
    f_title = f_title.strip()

    # remove whitespace, then change #2 to 2, also use zfill() to add zeros at the begining eg 001
    # zfill(n: int), n is how wide (in digits) should a string be with a zero?
    # Eg. zfill(2) means 01, zfill(3) - 001,
    # if a digit is 10, then it will remain, zfill() will only try to fill up for those that don't...
    # make 'n' digits, like 1, to keep 1 but in 2 digits, it adds a zero like 01
    f_number = f_number.strip()[1:].zfill(2)

    # Generate new file name
    new_filename = f'{f_number}-{f_artist}-{f_title}{file_ext}'

    # rename the file
    os.rename(f, new_filename)
