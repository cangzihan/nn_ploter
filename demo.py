import matplotlib.pylab as plt

def plot_NN(NN_Frame, input_text=None, output_text=None, save_fig=True):
  '''
  Draw a feedforward neural network
  '''
  x = []
  y = []
  y_i = []
  y_h = []
  y_o = []

  N_list = NN_Frame[:]
  for i,n in enumerate(N_list):
    if n > 5:
      N_list[i] = 5
  N_show = NN_Frame

  width = 0.05
  line1 = 1.95
  line2 = line1 + width
  line3 = line2 + width
  line0 = line1 - width/2
  height = 9

  line = [line1 - width/2, 1.95]
  for i in range(1, len(N_list)):
    line.append(line[-1]+width)
  line_1 = line[-1] + width/2

  for j in range(len(N_list)):
    x.append([])
    y.append([])
    for i in range(N_list[j]):
      x[j].append(line1)
      if j == 0 or j == len(N_list)-1:
        row = (i+(N_list[1]-N_list[j])/2 + 1)*height
      else:
        row = (i+1)*height
      y[j].append(row)

  nn_fig = plt.figure(figsize=(8,6))
  nn_ax1 = nn_fig.add_subplot(1,1,1)

  # Text & Line
  for j in range(len(N_list)):
    if j == 0:
      for i, input_y in enumerate(y[j]):
        plt.plot([line[j],line[j+1]],[input_y,input_y], color="C0")
        if i == 0:
          plt.annotate(input_text[i], xy=(line[j+1],input_y), xytext=(-50, 7), textcoords='offset points')
        else:
          plt.annotate(input_text[-N_list[0]+i], xy=(line[j+1],input_y), xytext=(-50, 7), textcoords='offset points')
    elif j == len(N_list)-1:
      for i, output_y in enumerate(y[j]):
        plt.plot([line[-1],line_1],[output_y,output_y], color="C0")
        plt.annotate(output_text[i], xy=(line_1,output_y), xytext=(-40, 7), textcoords='offset points')
    else:
      for i, hidden_y in enumerate(y[j]):
        if i == 0:
          plt.annotate("h"+str(j)+"_"+str(N_show[j]), xy=(line[j+1],hidden_y), xytext=(13, 1), textcoords='offset points')
        else:
          plt.annotate("h"+str(j)+"_"+str(len(y[j])-(i+1)), xy=(line[j+1],hidden_y), xytext=(13, 1), textcoords='offset points')
    

  # Circle
  for j in range(len(N_list)-1):
    for y1 in y[j]:
      for y2 in y[j+1]:
        plt.plot([line[j+1],line[j+2]],[y1,y2], color="C0", marker="o", 
                markerfacecolor='white', markersize=20)
    #nn_ax1.scatter(x, y, color="C0", marker="o", s=500)

  # ...
  if NN_Frame[0]>5:
    nn_ax1.scatter([line[1]]*3, 
             [((N_list[1]-N_list[0])/2 + 1)*height+height*3/8,
              ((N_list[1]-N_list[0])/2 + 1)*height+height/2,
              ((N_list[1]-N_list[0])/2 + 1)*height+height*5/8],
             color="C0", marker="o", s=5)

  for i in range(1, len(NN_Frame)-1):
    if NN_Frame[i]>5:
      nn_ax1.scatter([line[i+1]]*3, [height+height*3/8, height+height/2, height+height*5/8],
                color="C0", marker="o", s=5)
  
  plt.axis('off')
  if save_fig:
    nn_fig.savefig("figure_nn.pdf",bbox_inches='tight',dpi=nn_fig.dpi,pad_inches=0.0)


if __name__ == "__main__":
    input_text = ["x_1", "x_2", "x_3"]
    output_text = ["class_1", "class_2", "class_3", "class_4"]
    input_text.reverse()
    output_text.reverse()
    plot_NN([3,16,16,4], input_text, output_text)

