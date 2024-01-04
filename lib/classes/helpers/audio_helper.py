import pygame


class Audio:

    audio_convert = {
        "Netflix": 'lib/audio/Netflix.mp3',
        "Hulu": 'lib/audio/Hulu.mp3',
        "Amazon Prime Video": 'lib/audio/Prime.mp3',
        "Paramount Plus": 'lib/audio/Paramount.mp3',
        "Apple TV Plus": 'lib/audio/Apple.mp3',
        "HBO Max": 'lib/audio/HBO.mp3',
        "Disney Plus": 'lib/audio/Disney.mp3',
    }

    def play_audio(file_path):
        pygame.init()
        pygame.mixer.init()

        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(5)

        except Exception as e:
            print(f"Error: {e}")

        pygame.mixer.quit()
        pygame.quit()
