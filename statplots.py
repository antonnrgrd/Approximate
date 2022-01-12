
class StatPlots(Solution):
    def __init__(self,log_scale = False):
        self.log_scale = log_scale
        def plot_vals(self,value_frame,writer):
            if value_frame.values.ndims > 3:
                tkinter.messagebox.showerror("Data dimension error","Error: cannot plot data of dimension greater than 3")
                return
            writer.write('\begin{tikzpicure}[scale=0.5]')
            writer.write('\datavisualization [school book axes, visualize as smooth line]')
            writer.write('data {')
            writer.write('x,y')
            for index, rowid in value_frame.iterrtows():
                writer.write(str(rowid) + ',' + str(rowid.values))
            writer.write('}')
            writer.write('\end{tikzpicure}')
        
