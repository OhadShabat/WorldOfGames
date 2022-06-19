import Utils
import os

def clear_score():
    if os.path.exists(Utils.SCORES_FILE_NAME):
        os.remove(Utils.SCORES_FILE_NAME)

def add_score(score):
    fname = Utils.SCORES_FILE_NAME
    try:
        f = open(fname, "r")
        cur_score = int(f.read())
        f.close()
        new_score = score + cur_score
        f = open(fname, "w")
        f.write(str(new_score))
        f.close()
    except OSError:
        print("Failed to open file")
        f = open(fname, "w")
        f.write(str(score))
        f.close()

def get_score():
    fname = Utils.SCORES_FILE_NAME
    try:
        f = open(fname, "r")
        score = int(f.read())
        f.close()
        return score
    except OSError:
        return -1


def main():
    add_score(3)

if __name__ == '__main__':
    main()