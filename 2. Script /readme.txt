1. Using the perf tool in Linux terminal, we have execute a command to extract the performance counter values and store it in the text file.Command script is present in 4.ExtractPC directory.

2. All text files of different benchmarks are stored in the 3.Input Data directory.

3. Open the link https://colab.research.google.com/ to run the script or you can use      Jupyter notebook to run the script.

4. Using the 1.data_cleaning.py file in 2.Script directory. Clean the above generated text files to csv file. So, that we can train our model.

5. Run the generated csv file on the 2.linearmodel.py script in 2.Script directory for respective benchmarks. Change the respective benchmark csv file name in the script to get the CPI components for that benchmark.

6. Read the report in 1.Report directory to know all benchmarks quality parameters and CPI stack. We have also concluded some key observations based on the CPI stack components of different benchmarks.     