import matplotlib.pyplot as plt

def plot_loss(history, title = None):
    fig = plt.figure()
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title(f'Loss for DEMO')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    _ = plt.legend(["Train", "Validation"], loc='upper right')
    plt.show()