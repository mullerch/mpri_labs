This Readme file describes the files provided for the MPRI Challenge

- The <Training> folder contains all the occurrences of gesture that you must use to train and validate your algorithms
	It contains both Kinect and Xsens files

- The <Sample_Evaluation> folder contains two examples of file that could be used to evaluate your result 

- The <Sample_Results> folder contains two examples of result output for the sample_evaluation set.  Your algorithm must output a file with the exact same format for the final evaluation

- The <Evaluation Program> contains the program that will be used to evaluate your results. 
	You can look into the source code to see the implementation of the F1-Score evaluation metric.  (C# implementation using Accord.NET statistics library)
	You can run this program with your output file and the ground_truth sample to check the correctness of your implementation 
	There must be the same numbers of element in the GroundTruth and in your result file
	
If you have questions or remarks, do not hesitate to send them to <simon.ruffieux@hefr.ch>