import pandas as pd
from prettytable import from_csv

class Highscore:
    def __init__(self):
        try:
            self.highscore_df = pd.read_csv('highscores.csv', index_col='user', sep='|')
            self.new = False
        except:
            self.new = True

    def save(self, user, score):
        df = pd.DataFrame([[score]], columns=['high_score'], index=[user])
        if self.new:
            self.highscore_df = df.index.name = 'user'
            print('Score pertama telah terdaftar')
        else:
            if (user in self.highscore_df.index):
                if(score > self.highscore_df.loc[user].high_score):
                    self.highscore_df.loc[user].high_score = score
                    print('High Score sudah diupdate!')
                else:
                    print('Score tidak disimpan karena tidak melebihi highscore sebelumnya!')
            else:
                new_highscore = self.highscore_df.append(df, verify_integrity=True)
                new_highscore.index.name = 'user'
                self.highscore_df = new_highscore
                print('User telah ditambahkan ke High Score!')

        self.highscore_df.to_csv('highscores.csv', sep='|')

    def show(self):
        if self.new : print('Belum ada Highscore')
        else:
            ranked = self.highscore_df.sort_values(by='high_score', ascending=False)
            ranked['rank'] = ranked['high_score'].rank(ascending=False).astype('int')
            ranked.head(10).to_csv('ranked.csv')
            with open('ranked.csv') as csv:
                table = from_csv(csv)
            print(table)

