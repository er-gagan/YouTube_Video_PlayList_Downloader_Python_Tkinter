import pafy

def playlistURL(URL):
    plurl = URL
    playlist = pafy.get_playlist(playlist_url=plurl)
    length=int(len(playlist['items']))
    Title = []
    for i in range(0,length):
        Title.append(playlist['items'][i]['playlist_meta']['title'])
    return length,Title

def set360(URL,destinationPath):
    plurl = URL
    playlist = pafy.get_playlist(playlist_url=plurl)
    length=int(len(playlist['items']))
    VideoID = []
    for i in range(0,length):
        ll=str(playlist['items'][i]['pafy'])
        startIndex = ll.index(":")
        endIndex = ll.index('[')
        VideoID.append(ll[startIndex+2:endIndex-1])
        video = pafy.new(VideoID[i]) 
        streams = video.streams
        for i in streams:
            if '640x360' in i.resolution and 'mp4' in i.extension:
                print("\n\nVideo Title:",i.title)
                print("Video Size:",(int(i.get_filesize())//1024)//1024,"MB")
                print("Video Resolution:",i.resolution)
                print("Video Extension:",i.extension)
                print("Downloading Progress...")
                i.download(filepath=destinationPath)
                print("Download Complete...")
      
def set720(URL,destinationPath):
    plurl = URL
    playlist = pafy.get_playlist(playlist_url=plurl)
    length=int(len(playlist['items']))
    VideoID = []
    for i in range(0,length):
        ll=str(playlist['items'][i]['pafy'])
        startIndex = ll.index(":")
        endIndex = ll.index('[')
        VideoID.append(ll[startIndex+2:endIndex-1])
        video = pafy.new(VideoID[i]) 
        streams = video.streams
        for i in streams:
            if '1280x720' in i.resolution and 'mp4' in i.extension:
                print("\n\nVideo Title:",i.title)
                print("Video Size:",(int(i.get_filesize())//1024)//1024,"MB")
                print("Video Resolution:",i.resolution)
                print("Video Extension:",i.extension)
                print("Downloading Progress...")
                i.download(filepath=destinationPath)
                print("Download Complete...")