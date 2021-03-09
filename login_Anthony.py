import pandas as pd


class Credentials:

    def __init__(self):
        try:
            self.df = pd.read_csv('data_user.csv', index_col='username', sep='|')
            self.new = False
        except:
            print('Belum ada data user, mohon daftar terlebih dahulu')
            self.new = True

    def daftar(self, username, password):
        username = username
        df = pd.DataFrame([[password]], columns=['password'], index=[username])
        if self.new:
            df.index.name = 'username'
            df.to_csv('data_user.csv', sep='|')
            self.df = df
            print('Username pertama berhasil dibuat!')
        else:
            try:
                new_credentials = self.df.append(df, verify_integrity=True)
                new_credentials.index.name = 'username'
                new_credentials.to_csv('data_user.csv', sep='|')
                self.df = new_credentials
                print('Username berhasil dibuat!\nSilahkan menggunakan akun tersebut saat bermain :)')
            except Exception as e:
                print(e)

    def login(self, username, password):
        username = username
        if self.new:
            print('mohon membuat user terlebih dahulu')
            return False
        else:
            if username in self.df.index and password == self.df.loc[username].password:
                return True
            else:
                print('Login Gagal, silahkan coba lagi')
                return False
