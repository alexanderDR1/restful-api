
import time

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 0

while True:
        print ("choose difficulty from 1 - 5: ")
        difficulty = int(input())
        if (difficulty > 5 or difficulty < 1):
            print("iligal command. try again ")
            continue
        else:
            break

points_of_winning = (difficulty * 3) + 5


score_file = open(SCORES_FILE_NAME, "w+")
score_file.write("the score is: ")
score_file.write(str(points_of_winning))
time.sleep(3)
score_file.close()


def add_score(difficulty):
    #this function need read text file with info about score of gamer 
    #after that save it and open that or not
    #if file wiil close\fail that you need build new score and put him to score.txt 
     
     

    try:
        score_file = open(SCORES_FILE_NAME, "r")
        print(score_file.read(points_of_winning))
        score_file.clsoe()
    except:
        print('Something worng. the system fix that ')
        score_file = open(SCORES_FILE_NAME, 'w')
        print(score_file.write(str(points_of_winning)))
        score_file.close()