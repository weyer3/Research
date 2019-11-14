import pandas as pd
url = 'https://raw.githubusercontent.com/weyer3/Research/master/11_13_19_Callibration.csv'
df = pd.read_csv(url)

def plot_thermistors(df, row_min,row_max, apparatus_type,title ):
    #-----------------------------------------------------------------
    #Plotting
    #-----------------------------------------------------------------
    import matplotlib.pyplot as plt
    plt.clf()
    if apparatus_type == "Inplane":
        df_cut = df.iloc[row_min: row_max ,1:25]
    if apparatus_type == "Throughplane":
        df_cut = df.iloc[row_min: row_max, 26:]
    fig = plt.figure()
    ax = fig.add_subplot(111)    # The big subplot
    # Turn off axis lines and ticks of the big subplot
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)
    
    
    
    heating = fig.add_subplot(311)
    cooling = fig.add_subplot(312)
    both = fig.add_subplot(313)
    ax.set_xlabel("Time (sec)")
    ax.set_ylabel("Temperature (C)")
    colors = ['#FF3333','#FF6733','#FF8333','#FFA833','#FFBE33','#FFE333','#33CFFF','#33B7FF','#339BFF','#337FFF','#3357FF','#3344FF']
    num_thermistors = len(df_cut.columns)
    x = 0
    i = 0
    while x < num_thermistors:
        both.plot(df_cut.iloc[:,x+1],df_cut.iloc[:,x], color= colors[i])
        if x < 12:
            heating.plot(df_cut.iloc[:,x+1],df_cut.iloc[:,x], color= colors[i])
        else:
            cooling.plot(df_cut.iloc[:,x+1],df_cut.iloc[:,x], color= colors[i])

        x+=2
        i+=1
    plt.show()
    mytitle = format("%s.png" % (title))
    plt.savefig(mytitle)
    
    
df_cut = df.iloc[40:80,1:25]
i = 0
while i < len(df_cut.columns):
    if i == 0:
        print("HOT")
    if i == 12:
        print("COLD")
    print("%s average temperature: %f C" % (df_cut.columns[i], df_cut.iloc[:,i].mean()))
    i+=2    
