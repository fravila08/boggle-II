# You should re-use and modify your old BoggleBoard class to support the new requirements
import random
class BoggleBoard:
      chosen=[]
      def __init__(self):
            print("____")
            print("____")
            print("____")
            print("____")

      def shake(self):
            dice = {
                  1:['R ', 'I ', 'F ', 'O ', 'B ', 'X '],
                  2:['I ', 'F ', 'E ', 'H ', 'E ', 'Y '],
                  3:['D ', 'E ', 'N ', 'O ', 'W ', 'S '],
                  4:['U ', 'T ', 'O ', 'K ', 'N ', 'D '],
                  5:['H ', 'M ', 'S ', 'R ', 'A ', 'O '],
                  6:['L ', 'U ', 'P ', 'E ', 'T ', 'S '],
                  7:['A ', 'C ', 'I ', 'T ', 'O ', 'A '],
                  8:['Y ', 'L ', 'G ', 'K ', 'U ', 'E '],
                  9:['Qu', 'B ', 'M ', 'J ', 'O ', 'A '],
                  10:['E ', 'H ', 'I ', 'S ', 'P ', 'N '],
                  11:['V ', 'E ', 'T ', 'I ', 'G ', 'N '],
                  12:['B ', 'A ', 'L ', 'I ', 'Y ', 'T '],
                  13:['E ', 'Z ', 'A ', 'V ', 'N ', 'D '],
                  14:['R ', 'A ', 'L ', 'E ', 'S ', 'C '],
                  15:['U ', 'W ', 'I ', 'L ', 'R ', 'G '],
                  16:['P ', 'A ', 'C ', 'E ', 'M ', 'D ']
            }
            choose_from = []
            counter = 0
            for i in dice:
                  choose_from.append(dice[i][random.randint(0,5)])
                  if counter < 3:
                        print(choose_from[-1], end = " ")
                        counter += 1
                  else:  
                        print(choose_from[-1])
                        counter=0
            
            BoggleBoard.chosen=BoggleBoard.chosen+choose_from
      
      def include_word(self,word):  
            self.word=word .upper()  
            #print(BoggleBoard.chosen)
            leftSide=BoggleBoard.chosen[0::4]
            leftRSide=BoggleBoard.chosen[1::4]
            rightLSide=BoggleBoard.chosen[2::4]
            rightSide=BoggleBoard.chosen[3::4]
            diagonalL=BoggleBoard.chosen[0::5]
            diagonalR=BoggleBoard.chosen[3::3]
            diagonalR.pop(4)
            top=BoggleBoard.chosen[:4]
            topM=BoggleBoard.chosen[4:8]
            bottomM=BoggleBoard.chosen[8:12]
            bottom=BoggleBoard.chosen[12:]
            inspect=(leftSide,leftRSide,rightLSide,rightSide,diagonalL,diagonalR,top,topM,bottomM,bottom)
            for list in inspect:
                  list=''.join(list)
                  list=list.replace(" ", "")
                  if list == self.word:
                        return True
                  elif list[::-1] == self.word:
                        return True
                  else:
                        continue
            return False

game = BoggleBoard()
#game.shake()
game.shake()
print(game.include_word('hello'))

  
