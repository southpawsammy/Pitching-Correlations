# Pitching-Correlations
Quick look at correlation between MLB pitchers swing and miss rates and the average break (inches) on their pitches

So I ran a pearson, spearman, and kendall correlation coefficient equations on the csv file. The relationship 
(zone swing and miss rates vs avg break) should be logarithmic so the spearman or kendall equation should be the most accurate results.

I also created linear regression lines on the scatter plots for the 273 pitchers in the csv. There are three plots that show the relationship
between swing and miss rates and each of the average breaks in a pitcher's arsenal (fastball, breaking ball, offspeed). If a pitcher
didn't have an offspeed or breaking ball pitch I just input the average break of that pitch to make the dataset uniform. 

The results as far as I can tell back up the numbers in the correlation analysis and show that strongest relationship for swing and miss rates
in the MLB is movement in a pitcher's fastball.   
