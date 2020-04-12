import datetime
import sys
import os

def create_timestamp():

    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    
    timestamp = str(year)+str(month)+str(day)
    
    return timestamp

def main(in_file,out_file):
    
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    timestamp = str(year)+str(month)+str(day)
    
    if not os.path.isfile(in_file):
        print("File path {} does not exist. Exiting...".format(in_file))
        sys.exit()
    
    with open(in_file) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            out_file.write(line.strip()+"\n")
            cnt += 1
        
    in_file.close()
    out_file.close()

if __name__ == "__main__":

    in_file = r"C:\Users\tubxt2p\Documents\Python\python-projects\disc-file-app\tops_disc_items.lst"
    out_file = open(f"MfDiscItems_{create_timestamp()}.txt", "w")
    
    main(in_file,out_file)
    