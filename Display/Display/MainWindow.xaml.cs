using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Display {
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window {

        public static ViewModel data = new ViewModel();
        public MainWindow() {
            InitializeComponent();
            this.DataContext = MainWindow.data;
            new Task(() => {
                string[] args = { "" };
                HttpServerProgram.Main(args);
            }).Start();
        }

    }


    public class ViewModel : INotifyPropertyChanged {

        private string heartRateCurrent = "0";
        public string HeartRateCurrent {
            get {
                return heartRateCurrent.ToString();
            }
            set {
                heartRateCurrent = value;
                OnPropertyChanged("HeartRateCurrent");
            }
        }
        private string oxygenCurrent = "0";
        public string OxygenCurrent {
            get {
                return oxygenCurrent.ToString();
            }
            set {
                oxygenCurrent =value;
                OnPropertyChanged("OxygenCurrent");
            }
        }
        /*
        private int bloodPressureLower = 0;
        private int bloodPressureUpper = 0;

        public int BloodPressureLower {
            get {
                return bloodPressureLower;
            }
            set {
                this.bloodPressureLower = value;
                OnPropertyChanged("BloodPressure");

            }
        }
        public int BloodPressureUpper {
            get {
                return bloodPressureUpper;
            }
            set {
                this.bloodPressureUpper = value;
                OnPropertyChanged("BloodPressure");

            }
        }

        public string BloodPressure {
            get {
                return bloodPressureUpper.ToString() + "/" + bloodPressureLower.ToString() ;
            }
        }*/

        private string bloodPressure = "0/0";
        public string BloodPressure {
            get {
                return bloodPressure;
            }
            set {
                bloodPressure = value;
                OnPropertyChanged("BloodPressure");
            }
        }
        private string awRR = "0";
        public string AwRR {
            get {
                return awRR.ToString();
            }
            set {
                awRR = value;
                OnPropertyChanged("AwRR");
            }
        }
        public event PropertyChangedEventHandler PropertyChanged;
        protected void OnPropertyChanged(string name = null) {
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        }
    }
}
