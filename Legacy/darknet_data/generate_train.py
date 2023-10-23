import os

def generate_train(path, main_path='darknet'):
    train_path = os.path.join('.', main_path, path, 'train')
    image_files = []
    filecount = 0
    for filename in os.listdir(train_path):
        if filename.endswith(".png"):
            image_files.append(os.path.join(path, filename))
            filecount += 1
    with open(os.path.join(main_path, path, 'train.txt'), "w") as outfile:
        for image in image_files:
            outfile.write(image)
            outfile.write("\n")
        outfile.close()
    print(f"Found {filecount} train images.")

    test_path = os.path.join('.', main_path, path, 'test')
    image_files = []
    filecount = 0
    for filename in os.listdir(test_path):
        if filename.endswith(".png"):
            image_files.append(os.path.join(path, filename))
            filecount += 1
    with open(os.path.join(main_path, path, 'train.txt'), "w") as outfile:
        for image in image_files:
            outfile.write(image)
            outfile.write("\n")
        outfile.close()
    print(f"Found {filecount} train images.")
