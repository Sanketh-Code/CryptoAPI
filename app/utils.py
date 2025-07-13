from io import BytesIO
import matplotlib.pyplot as plt

def create_plot(x_data, y_data, title, xlabel, ylabel):

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x_data, y_data)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plt.close(fig) 
    return buf