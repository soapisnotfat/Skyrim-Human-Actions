import os


all_videos = ('archery', 'breaststroke', 'crossbow', 'dance', 'dodge', 'fly', 'horse_riding', 'run', 'skydiving',
              'waving_weapon')

ucf_videos = ('archery', 'horse_riding', 'run', 'breaststroke', 'skydiving')

new_videos = ('crossbow', 'dance', 'dodge', 'fly', 'waving_weapon')


def process_videos(video_list=all_videos):
    if not os.path.exists('./frames'):
        os.makedirs('./frames')
    for video in video_list:
        if os.path.exists('./' + video):

            for i in range(1, 11):
                video_name = './' + video + '/' + video + '_' + str(i) + '.mp4'
                destination = './frames/' + video + '/'
                if not os.path.exists(destination):
                    os.makedirs(destination)
                get_frame(video_name, destination)


def get_frame(video, directory):
    """
    extract frames from videos with given FPS 15
    """

    FFMPEG_BIN = "ffmpeg"

    dest_directory = directory
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    fps = '20'

    # The folder that the frame images will end up in
    dest = video[-5:-4]

    # Run the parser to generate the frame images
    # resize images to 240p
    os.system(FFMPEG_BIN + " -i " + video + " -vf scale=240:240" + " -r " + fps + " " + dest_directory + dest + "-%03d.png")


if __name__ == '__main__':
    process_videos()
