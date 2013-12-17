using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

using Accord.Statistics.Analysis;
using Accord.Math;

namespace MPRIEvaluation
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {       
        public string inputFolder; //The selected path of the input folder containing the results.txt files
        public string outputFolder; //The selected path for the output folder
        public string gtFile; //The path of the Ground Truth File
       
        public Dictionary<int, int> resultData; //A dictionary containing the fileID and the respective class as labeled by the classifier
        public Dictionary<int, int> gTData = new Dictionary<int, int>(); //A dictionary containing the fileID and the respective class as retrived from the ground truth
        
        private List<int> incompleteID; //List of fileIDs that could not be found in both resultData and gtData (should not happend and corresponds to *errors*)

        public MainWindow()
        {
            InitializeComponent();
            if (Properties.Settings.Default.inputFolder_path != null)
            {
                tb_InputFolder.Text = Properties.Settings.Default.inputFolder_path;
            }
            if (Properties.Settings.Default.outputFolder_path != null)
            {
                tb_Output_Folder.Text = Properties.Settings.Default.outputFolder_path;
            }
            if (Properties.Settings.Default.GTFile_Path != null)
            {
                tb_GTFile.Text = Properties.Settings.Default.GTFile_Path;
            }
        }

        /// <summary>
        /// When the user clicks on process button
        /// Starts the evluation procedure:
        ///     - Load GTData
        ///     - Get all results files
        ///     - For each result file:
        ///         - Load and parse it
        ///         - Compute and save the results
        /// </summary>
        private void but_process_Click(object sender, RoutedEventArgs e)
        {
            if (inputFolder != null && outputFolder != null && gtFile != null)
            {

                //Load GTData
                gTData = loadGTData(gtFile);

                //Get all files
                List<string> filePaths = new List<string>();
                filePaths = Directory.GetFiles(inputFolder).ToList();

                foreach (string file in filePaths)
                {
                    //Load resultData
                    string groupName = "";
                    string algoName = "";

                    resultData = new Dictionary<int, int>();
                    using (StreamReader sr = new StreamReader(file))
                    {
                        String line;
                        while ((line = sr.ReadLine()) != null)
                        {

                            if (line.StartsWith("#GroupName"))
                            {
                                groupName = line.Split('\t')[1];
                            }
                            if (line.StartsWith("#AlgoName"))
                            {
                                algoName = line.Split('\t')[1];
                            }
                            if (!line.StartsWith("#") && !line.StartsWith("\t") && !line.StartsWith(" "))
                            {
                                resultData.Add(int.Parse(line.Split('\t')[0]), int.Parse(line.Split('\t')[1]));
                            }
                        }
                    }
                    //Check that list contains all elements.
                    if (checkCompleteness(resultData, gTData))
                    {
                        computeNGenerateEvaluationData(groupName, algoName, resultData);
                        tb_Info.AppendText("- Completed the evaluation for " + groupName + " " + algoName + "\n");
                    }
                    else
                    {
                        tb_Info.AppendText("ERROR (skipping): " + groupName + " " + algoName + " missed samples " + string.Join((", "), incompleteID.ToArray()) + "\n");
                    }
                }
            }
        }

        /// <summary>
        /// Compares the resultData given in parameter with the GTData previously loaded and save the data
        /// We use the F1-score at a macro level, see references for more details
        /// We use the Accord.Net library to contruct the Confusion matrix but this could have been done manually
        /// The resulting evaluation data is written in two files: 
        ///     - The first file contains the detailed evaluation for the algorithm and is unique for each group-algo
        ///     - The second file should resumes the f1-score and will contain the result of all evaluations
        /// </summary>
        private void computeNGenerateEvaluationData(string groupName, string algoName, Dictionary<int, int> results)
        {
            /*
             * Definiton of F1-Score Macro: 
             * 
             * See ref http://www.cs.odu.edu/~mukka/cs495s13/Lecturenotes/Chapter5/recallprecision.pdf
             * See ref http://rali.iro.umontreal.ca/rali/sites/default/files/publis/SokolovaLapalme-JIPM09.pdf
             * 
             * Precision_i = ii/sum(column_i)
             * Recall_i = ii/sum(row_i)
             * PrecisionM = avg(precision_i))
             * RecallM = avg(recall_i))
             * F1score_Macro = (2*PrecisionM*RecallM)/(PrecisionM+RecallM)
             * 
            */

            int[] expected = new int[resultData.Count];
            int[] predicted = new int[resultData.Count];

            for (int i = 0; i < gTData.Count; i++)
            {
                expected[i] = gTData.ElementAt(i).Value - 1;  //(the confusion matrix needs number [0-N] numbering for the classes)
                predicted[i] = results[gTData.ElementAt(i).Key] - 1; //(the confusion matrix needs number [0-N] numbering for the classes)
            }

            //GeneralConfusion is generated 
            GeneralConfusionMatrix cm = new GeneralConfusionMatrix(10, expected, predicted);

            int numberOfClasses = cm.Classes;
            double[] precision = new double[numberOfClasses];
            double[] recall = new double[numberOfClasses];

            for (int i = 0; i < numberOfClasses; i++)
            {
                int[] col = cm.Matrix.GetColumn(i);
                int[] row = cm.Matrix.GetRow(i);
                precision[i] = (cm.Diagonal[i]) / (double)((cm.Matrix.GetColumn(i)).Sum());
                recall[i] = (cm.Diagonal[i]) / (double)((cm.Matrix.GetRow(i)).Sum());
                if ((cm.Diagonal[i]) == 0) { //Treat special cases (empty classes, division by zero, ...)
                    precision[i] = 0;
                    recall[i] = 0;
                    if(((cm.Matrix.GetColumn(i)).Sum()) == 0){
                        precision[i] = 1;
                    }
                    if (((cm.Matrix.GetRow(i)).Sum()) == 0)
                    {
                        recall[i] = 1;
                    }
                }
            }

            double precisionMacro = precision.ToList().Average();
            double recallMacro = recall.ToList().Average();
            double f1ScoreMacro = (2 * precisionMacro * recallMacro) / (precisionMacro + recallMacro);

            //Write the results of the algorithm in a file specific to the group-algo
            using (System.IO.StreamWriter file = new System.IO.StreamWriter(outputFolder + "\\" + groupName + "_" + algoName + " .txt"))
            {
                file.WriteLine("F1Score (Macro) = " + f1ScoreMacro);
                file.WriteLine("Precision (Macro) = " + precisionMacro);
                file.WriteLine("Recall (Macro) = " + recallMacro);
                file.WriteLine("Confusion Matrix");
                for (int i = 0; i < cm.Matrix.GetColumn(0).Length; i++)
                {
                    file.WriteLine(string.Join("\t", cm.Matrix.GetRow(i)));
                }
            }

            //Append the result of the current algorithm to the Result file
            using (System.IO.StreamWriter file = new System.IO.StreamWriter(outputFolder + "\\" + "Results.txt", true))
            {
                file.WriteLine(groupName + " " + algoName + " " + f1ScoreMacro + " " + precisionMacro + " " + recallMacro);
            }
        }

        /// <summary>
        /// Compare two dictionary 
        /// Check the they both have the same numbers and every element
        /// The resData must have the same fileIDs as the ones in GTData otherwise it means that the algo missed some samples
        /// </summary>
        private bool checkCompleteness(Dictionary<int, int> resultDataTemp, Dictionary<int, int> gTDataTemp)
        {

            bool complete = true;
            incompleteID = new List<int>();

            foreach (int id in gTDataTemp.Keys)
            {
                if (resultDataTemp.Count != gTDataTemp.Count)
                {
                    complete = false;
                }

                if (!resultData.ContainsKey(id))
                {
                    //Problem
                    incompleteID.Add(id);
                    complete = false;
                }
            }
            
            return complete;
        }

        /// <summary>
        /// Load the Ground truth data from a file 
        /// The dictionary contains <FileID, classID>
        /// </summary>
        private Dictionary<int, int> loadGTData(string pathName)
        {
            using (StreamReader sr = new StreamReader(gtFile))
            {
                Dictionary<int, int> tempDic = new Dictionary<int, int>();
                String line;
                while ((line = sr.ReadLine()) != null)
                {
                    if (!line.StartsWith("#"))
                    {
                        tempDic.Add(int.Parse(line.Split('\t')[0]), int.Parse(line.Split('\t')[1]));
                    }
                }
                return tempDic;
            }
        }

        private void but_InputFolder_Click(object sender, RoutedEventArgs e)
        {
            using (FolderBrowserDialog dialog = new FolderBrowserDialog())
            {
                dialog.Description = "Open the folder which contains the results files";
                dialog.ShowNewFolderButton = false;
                dialog.RootFolder = Environment.SpecialFolder.MyComputer;
                if (Properties.Settings.Default.inputFolder_path != null) {
                    try
                    {
                        dialog.SelectedPath = Properties.Settings.Default.inputFolder_path;
                    }
                    catch (Exception ef) { }
                }
                if (dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                {
                    //inputFolder = dialog.SelectedPath;
                    tb_InputFolder.Text = dialog.SelectedPath;
                    Properties.Settings.Default.inputFolder_path = dialog.SelectedPath;
                    Properties.Settings.Default.Save();
                }
            }
        }

        private void but_InputFileGT_Click(object sender, RoutedEventArgs e)
        {
            using (OpenFileDialog dialog = new OpenFileDialog()) {
                dialog.Multiselect = false;
                if (Properties.Settings.Default.GTFile_Path != null)
                {
                    try
                    {
                        dialog.InitialDirectory = Directory.GetParent(Properties.Settings.Default.GTFile_Path).FullName; ;
                    }
                    catch (Exception ef) { }
                }
                if (dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                {
                    //inputFolder = dialog.SelectedPath;
                    tb_GTFile.Text = dialog.FileName;
                    Properties.Settings.Default.GTFile_Path = dialog.FileName;//Directory.GetParent(dialog.FileName).FullName;
                    Properties.Settings.Default.Save();
                }
            }
        }

        private void but_OutputFolder_Click(object sender, RoutedEventArgs e)
        {
            using (FolderBrowserDialog dialog = new FolderBrowserDialog())
            {
                dialog.Description = "Select the desired output folder";
                dialog.ShowNewFolderButton = false;
                dialog.RootFolder = Environment.SpecialFolder.MyComputer;
                if (Properties.Settings.Default.outputFolder_path != null)
                {
                    try
                    {
                        dialog.SelectedPath = Properties.Settings.Default.outputFolder_path;
                    }
                    catch (Exception ef) { }
                }
                if (dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                {
                    //inputFolder = dialog.SelectedPath;
                    tb_Output_Folder.Text = dialog.SelectedPath;
                      Properties.Settings.Default.outputFolder_path = dialog.SelectedPath;
                    Properties.Settings.Default.Save();
                }
            }
        }

        private void tb_dataInputFolder_TextChanged(object sender, TextChangedEventArgs e)
        {
            inputFolder = tb_InputFolder.Text;
        }

        private void tb_GTFile_TextChanged(object sender, TextChangedEventArgs e)
        {
            gtFile = tb_GTFile.Text;
        }

        private void tb_Output_Folder_TextChanged(object sender, TextChangedEventArgs e)
        {
            outputFolder = tb_Output_Folder.Text;
        }

       

    

 



    }
}
