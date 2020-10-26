import matplotlib.pyplot as plt
fig = plt.figure()
fig.suptitle("Hello world!")

text = fig.texts[0].get_text()
print(text)