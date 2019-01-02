# Science News Segmentation
Science News Segmentation Project with Segment Prediction Model and Web App

## Project Overview
Using PEW Research Center Data, I built a custom consumer segmentation based on the different types of Science News Consumers. I analyzed and profiled the differences among the segments in order to understand potential ad or marketing targeting strategies. To simulate how an advertising agency would target these segments, I built a predictive model using primarily demographic and behavioral variables to predict new consumers into one of uncovered segments. An overview of the methodology, full analysis and interactive prediction model are hosted on a web app which can be viewed at: segmentscinews.com

## Motivation
A very common marketing strategy is to segment the market and identify certain segments of the market that are more or less attractive to a brand trying to motivate certain people to buy or use their product. It is sometimes easy to imagine the different attitudinal and behavioral consumers who are likely to use a certain product, but not as easy to understand how big they are, or to identify them when it comes to building marketing strategies to target them. You can imagine in the science news world, there are people more likely to enjoy and actively follow science in the news, and people who are just averse to news in general. But how do you find and target the more attractive segment (high science news consumer) over the other (non-news follower)? Advertising agencies can identify these people using certain demographic or behavioral attributes, which is what I have tried to simulate in this project.

## Methodology
### Design
***Relevant files:** pipeline.py, DataExploration.ipynb, files in the 'data' folder*<br>
The key to a creating a good consumer segmentation is having a well-designed questionnaire which contains variables to answer the business question at hand. Since this project took course over only a couple of weeks, and it was out of scope to create a questionnaire from scratch and collect my own data, I used a questionnaire and dataset that was readily available. I sifted through many questionnaires and datasets from PEW Research Center to select the one with the richest dataset and most interesting consumer types. When reading through the questionnaires I was looking for the following criteria:
- Clear and defining attitudinal and behavioral questions to be used as 'segmentation variables'
- Interesting and defining demographic and behavioral questions to be used as 'profiling variables'
- Enough variables in the questionnaire to play around with multiple segmentations, using a combination of a few different segmentation variables
- A questionnaire that could yield interesting, and well-defined consumer segments

After careful assessment I chose to move forward with the 2017 PEW Research Center Science and News Survey. It is a robust questionnaire which gets at the attitudes and behaviors towards science in the news as well as general news attitudes and behaviors. It also has a very extensive battery of demographic variables which could be used for rich profiling and the prediction model, which will be explained further later.

### Segment
***Relevant files:** ClusterModels.ipynb, SelectingBestClusterModel.ipynb*<br>
The first step in creating my segmentation was to analyze the questionnaire from PEW Research and split the questions into Segmentation Variables and Profiling Variables. Segmentation Variables are the variables in the dataset that are inputs into the segmentation. In a good segmentation, these variables are ones that should pull respondents apart the most, meaning they have a wide variety of responses and are the ones that define the consumers we are looking to find. In my case, I was looking to uncover different Science News Consumers. I tried many variations of variables in my segmentation but landed on the following:
- **ENJOY**: 'How much would you say you enjoy following news about science compared with other kinds of news?' (4-point scale: 'A lot more than other news' - 'A lot less than other news')
- **KNOWLEDGE**: 'How much would you say you know about science?' (4-point scale: 'A lot' - 'Nothing at all')
- **SCIOFTEN**: 'Thinking just about science news, how often do you read, watch or listen to news about science?' (4-point scale: 'Nearly everyday' - 'Less often')
- **TOPICS1**: 'Which statement best describes how you get science news?' (2-point scale: 'I get science news on just a couple of topics' - 'I get science news on a lot of different topics'

During the segmentation process I tested 3 clustering and mixture models including: KMeans Clustering, Agglomerative (Hierarchical) Clustering, and Gaussian Mixture Model. I used the following criteria in selecting the 'best' clustering model with the optimal number of segments:
- Assessed the within-cluster sum of squares score (KMeans Only) and Silhouette Score (All Models) to select the optimal number of segments
- Looked at the sizes of the segments resulting from the different number of 'k's chosen to make sure there weren't any that were too small to analyze
- Analyzed how the different segments pulled apart in their responses to the segmentation variables as well as some key profiling variables. Made sure that, when profiled, the segments made sense- could I imagine each segment as a group of people that really existed outside of the data? 

I quickly eliminated the Hierarchical Clustering Model from my analysis because it yielded a solution with segments that were too small to analyze (i.e. were 1% or 2% the population) and two segments that made up 90% of the respondents together.

I then analyzed the KMeans Clustering 3- and 4- and 8-segment solutions which yielded the highest silhouette scores. I also assessed and analyzed the Gaussian Mixture Models using different covariance types. My final 3- segment segmentation solution was created using the Gaussian Mixture Model, with covariance type: Spherical and 100 Max Iterations. It yielded the highest silhouette score of .46, and a segment solution which was easy to analyze and understand. My next step was to fully analyze the solution and bring the segments to life using the Profiling variables

### Analyze
***Relevant files:** ProfilingSegments.ipynb, Seg0Charts.ipynb, Seg1Charts.ipynb, Seg2Charts.ipynb, BuildDatabase.ipynb, pipeline.py, database_col_names.py, savemodel.py*<br>
To assist in my analysis I created a database to easily compare and contrast the differences and similarities among the segments. The Database was created by generating a dataset that was binary for every variable, adding the labels generated by the Gaussian Mixture Model to the records of the original dataset, grouping respondents by their segment and summing across the variables to get a count of the number of respondents within each segment which responded to each variable. I then divided each segment row by the total size of the segment to get the % or respondents from each segment which responded a certain way to the question. This gave me a database which I could easily see the differences in responses among the segments. 

I used the Database described above to profile the segments. The Profiling Variables in a segmentation are any variable not included as a Segmentation Variable. These variables are used to understand the segments outside of just how they are defined. For example, demographic variables are often good profiling variables. In a good segmentation, the segments differ across age, gender and income even though they weren't used in the creating the segments. Other behavioral variables like the different types of news the segments watch are good profiling variables to really help understand the essence and full profile of the segments. 

Once the segments were fully profiled and I felt that I truly understood each segment individually, I created charts for each segment individually to show their responses to different demographic, science news, general news, and other behavioral variables. 

### Predict
***Relevant files:** PredictingSegments.ipynb, model.py*<br>
As my final step of this project I built a classification model which predicts the segment of a new consumer using primarily demographic and behavioral data to simulate the way that advertising agencies target different consumer segments. Using 10 non-segmentation variables, I was able to predict a new consumer segment with 68% accuracy. I trained and tested a Logistic Regression, Random Forest Classifier and Gradient Boosting Classifier Model. The Gradient Boosting Model performed the best, with the highest accuracy and was optimized using a Grid Search to find the best parameters. 

## Next Steps
There a few additional steps I would take if I were to re-run this project or run a different segmentation in the future:
- If I had more time I would like to explore different segmentation solutions. Since my project had a deadline and relied on my segmentation step being completed in a timely fashion, I had to choose a final segmentation solution in the first couple of days. I would have liked to explore more with different Segmentation Variables used and different clustering methods used and try to uncover a segmentation solution that segmented the general news consumer, with the hopes of finding the science news consumer within that universe, rather than the universe being defined as the 'Science News Consumer'
- I also would have liked to explore a segmentation with more than just three segments. Typically as a marketer you want more than just three segments to build marketing strategies off of.
- Typically segmentations are done for a specific brand or product with a specific business question in mind. If I were to replicate the full process of a segmentation, I would have started with a business question, built a questionnaire and collected my own data, however this was not feasible with the given time constraint
- Finally, if I had created this segmentation with a specific business question and marketing strategies in mind, I would then like to A/B test on the different marketing targeting strategies for each of the segments, once I uncovered the segments which were most attractive for the brand/product.