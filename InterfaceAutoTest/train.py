import os, re
import torch
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image


# 定义数据集类
class MosaicDataset(Dataset):
    def __init__(self, root_dir, transform):
        self.root_dir = root_dir
        self.filenames = [f for f in os.listdir(root_dir) if f.endswith('.jpg')]
        self.transform = transform

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir, self.filenames[idx])
        image = Image.open(img_name).convert('RGB')
        # target = Image.open(os.path.join('data/original', self.filenames[idx].replace('_mosaic_', '.'))).convert('RGB')
        target = Image.open(os.path.join('data/original', re.sub(r'_mosaic_\d+\.', '.', self.filenames[idx]))).convert(
            'RGB')
        # print(target)
        sample = {'image': image, 'target': target}
        if self.transform:
            sample['image'] = self.transform(sample['image'])
            sample['target'] = self.transform(sample['target'])

        return sample


# class MosaicNet(torch.nn.Module):
#     def init(self):
#         super(MosaicNet, self).init()
#         self.encoder = torch.nn.Sequential(
#             # 卷积层 1
#             torch.nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1),
#             torch.nn.BatchNorm2d(32),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 2
#             torch.nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1),
#             torch.nn.BatchNorm2d(64),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 3
#             torch.nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1),
#             torch.nn.BatchNorm2d(128),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 4
#             torch.nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1),
#             torch.nn.BatchNorm2d(256),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 5
#             torch.nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1),
#             torch.nn.BatchNorm2d(128),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 6
#             torch.nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),
#             torch.nn.BatchNorm2d(64),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 7
#             torch.nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
#             torch.nn.BatchNorm2d(32),
#             torch.nn.ReLU(inplace=True),
#             # 卷积层 8
#             torch.nn.ConvTranspose2d(32, 3, kernel_size=3, stride=1, padding=1),
#             torch.nn.BatchNorm2d(3),
#             torch.nn.ReLU(inplace=True),
#         )
class MosaicNet(torch.nn.Module):
    def __init__(self):
        super(MosaicNet, self).__init__()

        self.conv1 = torch.nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(128, 256, kernel_size=3, stride=2, padding=1)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(32, 3, kernel_size=3, stride=1, padding=1)
        self.relu = torch.nn.ReLU(inplace=True)
        self.batchnorm2d = torch.nn.BatchNorm2d

    def forward(self, x):
        x = self.conv1(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv4(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv_transpose1(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv_transpose2(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv_transpose3(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        x = self.conv_transpose4(x)
        x = self.batchnorm2d(x)
        x = self.relu(x)
        return x


def forward(self, x):
    x = self.encoder(x)
    return x


def train():
    # 定义超参数
    lr = 0.001
    epoches = 10

    # 定义自己的数据集类
    class CustomDataset(Dataset):
        def __init__(self, file_list, transform=None):
            self.file_list = file_list
            self.transform = transform

        def __len__(self):
            return len(self.file_list)

        def __getitem__(self, idx):
            img = Image.open(self.file_list[idx]['image_path'])
            target = Image.open(self.file_list[idx]['target_path'])
            if self.transform is not None:
                img = self.transform(img)
            if self.transform is not None:
                target = self.transform(target)
            return {'image': img, 'target': target}

    # 定义自己的变换
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    data_path = 'data'
    image_dir = 'original'
    target_dir = 'mosaic'

    # 获取所有标签文件的文件名
    target_files = os.listdir(os.path.join(data_path, target_dir))

    # 构造图像和标签的路径，并将它们存储在一个字典中
    data_dict = {}
    image_path = os.path.join(data_path, image_dir, '12.jpg')
    for target_file in target_files:
        target_path = os.path.join(data_path, target_dir, target_file)
        data_dict[image_path] = data_dict.get(image_path, []) + [target_path]

    # 将字典转换为 train_list 列表
    train_list = [{'image_path': k, 'target_path': v} for k, vs in data_dict.items() for v in vs]
    # print(train_list)
    # 加载训练数据
    train_data = CustomDataset(file_list=train_list, transform=transform)
    train_loader = DataLoader(train_data, batch_size=16, shuffle=True)

    # 创建模型实例并将其移动到 GPU 上
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = MosaicNet().to(device)

    # 定义损失函数和优化器
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    total=0
    correct=0
    # 训练模型
    for epoch in range(epoches):
        # print(epoch)
        for i, data in enumerate(train_loader, 0):
            # print(i, data)
            # 获取训练数据和目标数据，将它们移动到 GPU 上
            images = data['image'].to(device)
            targets = data['target'].to(device)

            # print(images)
            # 模型前向传播和计算损失
            outputs = model(images)
            loss = criterion(outputs, targets)

            # 梯度清零、反向传播计算梯度、更新参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 打印训练日志
            if i % 10 == 0:
                print(f'Epoch [{epoch + 1}/{epoches}], Step [{i + 1}/{len(train_loader)}], Loss: {loss.item():.4f}')

    # 保存模型
    if not os.path.exists('models'):
        os.makedirs('models')
    torch.save(model.state_dict(), 'models/mosaic_net.pth')
