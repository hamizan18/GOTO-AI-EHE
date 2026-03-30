from pytube import Playlist, YouTube
import os

playlist_url = input("Masukkan URL Playlist YouTube: ")
download_folder = "Inii Playlist Hasil Downloads"

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Ambil playlist
playlist = Playlist(playlist_url)

print(f"\nTotal video: {len(playlist.video_urls)}\n")

# Loop semua video
for index, video_url in enumerate(playlist.video_urls):
    try:
        print(f"Downloading ({index+1}/{len(playlist.video_urls)})")

        yt = YouTube(video_url)
        
        stream = yt.streams.filter(progressive=True, res="720p").first()
        
        stream.download(output_path=download_folder)
        
        print(f"✔ {yt.title} selesai\n")

    except Exception as e:
        print(f"❌ Gagal: {video_url}")
        print(e)