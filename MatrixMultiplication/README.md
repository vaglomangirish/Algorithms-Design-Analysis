Requirements: Python 2.7 installed.

How to run the program:-
python MatrixMultiplication.py \<MAXSIZE\>  

For Example:-  
python MatrixMultiplication.py 128  
For Matrix Size: 1  
Time for standard: 0.00395774841309 milliseconds  
Time for standard recursive: 0.00262260437012 milliseconds  
Time for strassens: 0.00231266021729 milliseconds  
For Matrix Size: 2  
Time for standard: 0.00779628753662 milliseconds  
Time for standard recursive: 0.0367164611816 milliseconds  
Time for strassens: 0.0818490982056 milliseconds  
For Matrix Size: 4  
Time for standard: 0.0324249267578 milliseconds  
Time for standard recursive: 0.235199928284 milliseconds  
Time for strassens: 0.34008026123 milliseconds  
For Matrix Size: 8  
Time for standard: 0.162816047668 milliseconds  
Time for standard recursive: 2.59456634521 milliseconds  
Time for strassens: 4.00774478912 milliseconds  
For Matrix Size: 16  
Time for standard: 1.13899707794 milliseconds  
Time for standard recursive: 15.895485878 milliseconds  
Time for strassens: 16.6929244995 milliseconds  
For Matrix Size: 32  
Time for standard: 4.55331802368 milliseconds  
Time for standard recursive: 110.559082031 milliseconds  
Time for strassens: 130.939817429 milliseconds  
For Matrix Size: 64  
Time for standard: 35.1504564285 milliseconds  
Time for standard recursive: 754.813671112 milliseconds  
Time for strassens: 825.767660141 milliseconds  
For Matrix Size: 128  
Time for standard: 268.47743988 milliseconds  
Time for standard recursive: 6027.02052593 milliseconds  
Time for strassens: 5991.11263752 milliseconds  

Also find the product_times.csv generated once the program is executed.  

How to view the graph:-  

Start a Simple HTTP Server in python in the project directory:-  
python -m SimpleHTTPServer 8000  
  
Run linechart.html in browser which would be hosted on the HTTP Server:-  
google-chrome http://localhost:8000/linechart.html  

