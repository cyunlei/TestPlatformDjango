import cv2
import subprocess

def remove_watermark(input_file, output_file):
    # 使用OpenCV读取视频文件
    cap = cv2.VideoCapture(input_file)
    # 获取视频FPS
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 获取视频尺寸
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 定义输出视频编码格式
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # 创建输出视频对象
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # 帧计数器
    i = 0

    # 循环读取每一帧
    while(cap.isOpened()):
        # 读取一帧
        ret, frame = cap.read()

        if ret:
            # 修改帧，去除水印
            processed_frame = remove_watermark_from_frame(frame)

            # 把处理过的帧写入输出视频
            out.write(processed_frame)

            i += 1
            print("Progress: ", i)

        else:
            break

    # 关闭输入输出视频对象
    cap.release()
    out.release()

    # 获取输入视频的元数据
    meta_data_cmd = "ffprobe -v error -show_streams -select_streams v:0 {}".format(input_file)

    meta_data = subprocess.check_output(meta_data_cmd.split())

    meta_data = meta_data.decode().split("\n")

    # 获取输入视频的编码参数
    in_params = ""

    for line in meta_data:
        if "codec_name" in line:
            codec_name = line.split("=")[1]

            in_params += "-c:v {} ".format(codec_name)

        elif "width" in line:
            width = line.split("=")[1]

            in_params += "-s {}x{} ".format(width, height)

        elif "sample_aspect_ratio" in line or "display_aspect_ratio" in line:
            aspect_ratio = line.split("=")[1].replace(":", "/")

            in_params += "-aspect {} ".format(aspect_ratio)

    # 获取输出视频的编码参数
    out_params = "-c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p"

    # 执行FFmpeg编码命令将无水印的视频写出
    cmd = "ffmpeg -i {} {} {} -y".format(output_file, in_params, out_params)

    subprocess.call(cmd.split())

    print("Done!")


def remove_watermark_from_frame(frame):
    # 在这里编写去除视频水印的算法
    # 这里只提供一个简单的示例，将帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 返回原始帧或加处理的帧
    return gray_frame


# 调用去除水印函数，传入输入视频文件和输出视频文件名
remove_watermark("D:\素材\原材料\情义千秋.mp4", "D:\素材\原材料\情义千秋1.mp4")