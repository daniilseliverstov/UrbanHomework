def watch_video(self, movie: str):
    if self.current_user and self.current_user.age < 18:
        print('Вам нет 18 лет, пожалуйста покиньте страницу')
    elif self.current_user:
        for video in self.videos:
            if movie in video.title:
                for i in range(1, ):
                    print(i, end=' ')
                    time.sleep(1)
                print('Конец видео')
    else:
        print('Войдите в аккаунт, чтобы смотреть видео')
