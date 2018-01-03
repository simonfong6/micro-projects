import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
# Force matplotlib to not use any Xwindows backend.


def plot(datas, title, xlabel, yabel, file_name):
    plt.figure()
    for key,value in datas.iteritems():
        plt.plot(value, label=key)
    plt.legend(loc='upper right')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(yabel)
    
    plots_dir = 'plots'
    file_name + '.png'
    plot_path = os.path.join(plots_dir,file_name)    
    plt.savefig(plot_path)
    

ID = 'caltech_10_50_40_5_55'
history = {'acc': [0.095817676483805791, 0.28957686741242822, 0.50555464665283278, 0.65299788031716732, 0.74530305436498456, 0.80370853962296074, 0.84732886239840033, 0.88098349488067818, 0.90238522583510128, 0.92337852995918768], 
'loss': [5.151904587261896, 3.923175798757971, 2.6185036073652599, 1.7853670797790504, 1.2673070805366085, 0.95775675836915852, 0.74024970485988428, 0.59082167490579163, 0.4680911758730486, 0.38887816197102687], 
'val_acc': [0.25555555600356433, 0.52287582069440608, 0.68300653945386802, 0.75555555415309328, 0.78692810169232441, 0.7986928099900289, 0.81503267537534629, 0.82222221879398116, 0.82810457002103721, 0.83267973295224262], 
'val_loss': [4.4289246478111917, 2.9293855467652965, 1.8749079003053553, 1.3586791734290278, 1.0995942599633162, 0.95542762676874793, 0.88733452870175733, 0.82226065366096746, 0.77731363095489203, 0.75763174053890259]}
[0.91508775230313211, 0.80134259643511063]

train_acc = history['acc']
train_val_acc = history['val_acc']
train_loss = history['loss']
train_val_loss = history['val_loss']

data = { 'Training': train_acc,
         'Validation': train_val_acc
        }

plot(data,'Accuracy','Epoch','Accuracy','acc_vs_val_acc_1{}'.format(ID))

