from moviepy.editor import AudioFileClip, VideoFileClip
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    #通过添加参数运行
    parser.add_argument('--adPath', type=str, default='')
    parser.add_argument('--vdPath', type=str, default='')
    parser.add_argument('--outPath', type=str, default='')
    args = parser.parse_args()


    #使用moviepy
    ad = AudioFileClip(args.adPath)
    vd = VideoFileClip(args.vdPath)

    vd2 = vd.set_audio(ad)
    vd2.write_videofile(args.outPath,threads = 32)