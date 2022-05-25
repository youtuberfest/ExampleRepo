from pytube import YouTube as yt

video = input("Video URL: ")
d = yt(video)

dl = d.streams.filter(progressive=True,                      file_extension='mp4').order_by('resolution')[-1] 


dl.download('./')

print('download complete')
