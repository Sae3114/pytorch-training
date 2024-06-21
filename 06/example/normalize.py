import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__ == "__main__":
    image_path = "./example_data/dog_img.png"
    image = Image.open(image_path)

    # 画像をTensorに変換し、その後に正規化を行う変換を追加
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    # 変換を適用
    transformed_image = transform(image)

    # 順番入れ替え
    tensor_data_permuted = transformed_image.permute(1, 2, 0)
    # Numpy配列に変換
    numpy_array = tensor_data_permuted.numpy()

    #画像出力
    plt.imshow(image)
    plt.show()
    plt.imshow(numpy_array)
    plt.show()