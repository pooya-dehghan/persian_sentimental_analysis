# OverView : 
this project is intended to give a api backed persian sentimental analysis model with accuracy of 90% .

project will be completed in few steps and for first part we train on labeled data already on hugging face , method we use will be supervised learning and we go through every data collected and kept in HF.

# Name : 
this project goes by name persian textCNN analysis.

# Api Contract : 
this project will recive a text with this body input : {text : string} , and will output something enum like output : {sentiment: positive|negative}

# limitations : 
this model is using snappfood free access sentimental data on hugging face and could have note achive a high rate of accuracy.

# input and output : 
 input : {text : چقدر این غذا بد بود} output : {sentiment : negative}
 input : {text : هوا عالیه خیلی خوبه و تمیز هست} output : {sentiment : positive}
 input : {text : یکی از چرت ترین چیزایی که دیدم} output : {sentiment : negative}