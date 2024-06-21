import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__ == "__main__":
    preprocess_1 = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((224, 224)),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    preprocess_2 = transforms.Compose([
        transforms.ToTensor(),
        transforms.RandomHorizontalFlip(),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2)
    ])

    preprocess_3 = transforms.Compose([
        transforms.ToTensor(),
        transforms.RandomHorizontalFlip(),
        transforms.RandomResizedCrop(size=(224, 224), scale=(0.08, 1.0))
    ])

    # サンプル画像を読み込んで前処理を適用
    image_path = "./exercise_data/dog_img.png"
    image = Image.open(image_path)
    processed_image1 = preprocess_1(image)
    processed_image2 = preprocess_2(image)
    processed_image3 = preprocess_3(image)
    # テンソルに変換した画像を表示
    # チャンネル次元を最後に移動
    plt.imshow(processed_image1.permute(1, 2, 0))
    plt.show()
    plt.imshow(processed_image2.permute(1, 2, 0))
    plt.show()
    plt.imshow(processed_image3.permute(1, 2, 0))
    plt.show()