from google.colab import drive
drive.mount('/content/drive')

#@title 从谷歌云盘加载打包好的数据集进行预处理
#@markdown **sovits3.0的数据集不再需要特定的文件结构，将数据集的所有wav文件放在同一个文件夹下压缩为zip后上传至谷歌云盘即可，该处理脚本可以一次性预处理多个数据集，处理多个数据集时请依次解压每一个数据集**

#@markdown 数据集名称（**人物的英文/拼音名**，与建数据文件夹时统一；不带zip。）
DATASETNAME = "test"  #@param {type:"string"}
#@markdown 压缩包路径（谷歌盘路径，传到dataset的就不改这个，没有dataset文件夹就新建一个）
ZIP_PATH = "/content/drive/MyDrive/dataset/"  #@param {type:"string"}
ZIP_NAME = ZIP_PATH + DATASETNAME

# !unzip -d /content/so-vits-svc/dataset_raw {ZIP_NAME}.zip