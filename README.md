# Analyzing-Conversion-Rate-Retail-Company
The main objective of this analysis is to explain why there is a 5% decrease in last week's conversion rate compared to the previous week's conversion rate for a retail company. In addition, provide a plan of action to drive an improvement in customer experience and revenue. 



## Introduction
Conversion rate is an important metric that is used to measure the performance of an e-commerce business. It is measured as the proportion of transactions (purchases) to visits that occur on the site. A widely known strategy to improve the conversion rate is conversion rate optimization, or CRO. Strategies and tactics for CRO may differ from company to company, but each follow a similar general process. Central to these processes is identifying whether the company can has accurate data to measure conversion and identifying where are the critical, high impact areas to test[1]. Most simply, if the goal is to increase performance, then you need to have clear definition of performance and ensure the data is available during testing.

A conversion funnel is widely used to model customer behaviour online in a sequence of steps. This funnel is a sequences of pages, screens, actions, and events that lead to a specific event, such as an account registration or purchase [1]. This analysis will focus on bounce rate, abandoned cart rate, and conversion, which all measure user engagement on the site.  The bounce rate, or the number of customers who end their visit after one page view, is a useful metric because it shows if users are taking the time to explore the site, or if they are leaving right away [3]. Shopping cart abandonment is when a potential customer starts a check out process for an online order but drops out of the process before completing the purchase [3]. It is generally a good idea to decrease the bounce rate and abandoned cart rate in order to improve conversions. 

After these metrics are measured and areas of opportunity are identified, a method known as A/B testing may be employed to make quantifiable changes to the website. A/B testing is an experiment, where two versions of a webpage are compared to each other to determine which one performs better [3]. In the results section, some actionable experiments are discussed. 



## Exploratory Data Analysis
There are two data tables that have been provided for analysis: a visits table and pages viewed table. For the purposes of this analysis, sample datasets have been artificially constructed and we will assume are representative of the business. In actuality, these results are not representative of the business. 

Datasets were simulated using Google Sheets, and analysis was conducted in Python 3.6.

### Part 1 - Visits
The visits table contains a sample of 150 entries between Oct 19, 2020 – Oct 25, 2020. Each entry consists of a visit, and in total there are 103 unique visitors.

#### Data columns (total 11 columns)
visitorid         150 non-null int64
visitid           150 non-null int64
visitStartTime    150 non-null object
date              150 non-null object
visits            150 non-null int64
transactions      150 non-null int64
trafficSource     150 non-null object
deviceCategory    150 non-null object
country           150 non-null object
region            150 non-null object
city              150 non-null object

<img src="https://github.com/almakaune/Analyzing-Conversion-Rate-Retail-Company/blob/main/images/1.1.png" width=60%>

The weekly conversion rate was calculated as: 

Weekly Conversion Rate = Total Transactions / Total Visits 
= 9.3% (down 5% from last week)

Daily Average Conversion Rate
=  8.4% 

Clearly the distribution of daily conversion rate is skewed to the left, as conversion rate tends to increase during the weekend. This is shown in graph 1.1.

<img src="https://github.com/almakaune/Analyzing-Conversion-Rate-Retail-Company/blob/main/images/1.2.png" width=60%>

Graph 1.2 shows a the graph of daily conversion rates segmented by country. The weekly conversion rate by country is calculated as:

CA Weekly Conversion Rate: 9.8% 
US Weekly Conversion Rate: 3.7%

It is clear that Canada is driving the majority of this week's conversions. To further investigate the performance of conversion rate, it is worthwhile to segment the data by region, device and by traffic source for both Canada and US separately. 

<img src="https://github.com/almakaune/Analyzing-Conversion-Rate-Retail-Company/blob/main/images/1.3.png" width=60%>

The results of graph 1.3 show that Region 3 and the South have the highest conversion rate for Canada and US respectively. In Canada R4 seems to have much lower (none) conversion than the other three regions, where as in the US, the south has a much higher conversion rate than the other three regions. 

<img src="https://github.com/almakaune/Analyzing-Conversion-Rate-Retail-Company/blob/main/images/1.4.png" width=60%>

The results of graph 1.4 show that social media has the highest conversion rate in Canada, while direct has the highest conversion rate in the US. And finally, graph 1.5 shows that desktop has the highest conversion rate in Canada, while mobile has the highest conversion rate in the US.

<img src="https://github.com/almakaune/Analyzing-Conversion-Rate-Retail-Company/blob/main/images/1.5.png" width=60%>

Graph 1.5 shows that social media has the highest conversions for CA, while direct has the highest conversions for the US. All other categories are relatively balanced. 


Further segmentation: by device and by traffic source:

<img src="https://github.com/almakaune/Analyzing-Conversion-Rate-Retail-Company/blob/main/images/table.png" width=60%>

Of these 6 segments, desktop/email, desktop/social media and mobile/direct are leaders of the highest conversion rate. 


### Part 2 - Pages Viewed
The pages viewed dataset consists of a sample of 625 entries between Oct 19, 2020 – Oct 25, 2020. There are 146 unique visits and 103 unique visitors, so there is a small discrepancy to the visits table. HitTime and eventLabel have been excluded from this table, as seen as not purposeful for this study.

#### Data columns (total 7 columns):
visitorid        625 non-null int64
visitid          625 non-null int64
hitNumber        625 non-null int64
hitPageUrl       625 non-null object
hitType          625 non-null object
eventCategory    79 non-null object
eventAction      79 non-null object


The bounce rate is calculated as:

Bounce Rate = (Total Visits where # page views = 1) / (Total Visits)
= 38.4%

Pages per session is calculated as:

Pages per Session = (Total pages Viewed per Session) / (Total Visits)
= 4.28

Abandoned cart rate is calculated as:
Abandoned Cart Rate = (initiated transactions – total purchases) / initiated transactions
= 55.2%



## Results
It would be very useful to be able to compare the results from the exploratory analysis to the previous week's business conversion rate, as well as to last year's conversion rates. This way we could gauge whether the 5% decrease in conversion rate could be a macro trend or a seasonal trend. For this analysis, we will look at the results on their own merit.  
 
First off, it is noticeable that Canada has a higher conversion rate than the US. It is a broad question, but could it be worth investigating why this is? In Canada, R1 and R4 have the lowest conversions and in the US the only performing region is the South. Narrowing down the research to region could be helpful. 

Another noticeable result is that email-for-desktop conversions in Canada is high. Are the email campaigns for Canada and the US similar, because if not there could be an opportunity to improve email campaigns for the US, and across mobile and tablet devices. For example, a possible course of action could be to AB test features such as changing the subject line, fonts, colors or even price [1].

Next, tablet conversions are low. Could this be a technical issue? A course of action could be testing the site on a tablet for technical issues to see if there are any improvements to be made. 

This week's bounce rate is 38.4% and the abandoned cart rate is 55.2%. Again, it would be useful to measure these metrics against last week and last year to paint a more clear pictures of the trend. If the bounce rate has increased from last week, this could pinpoint an area of opportunity in the conversion funnel. How can the site be improved such the bounce rate decreases? A similar question holds for the abandoned cart rate. A course of action could be to investigate why the bounce rate and abandoned cart rate is high, and create a testable hypothesis to improve these numbers. 

Lastly, the pages per session metric is 4.28, which means that on average a viewer looks at around 4 pages per session. Is this number on trend with last year or last week's business? If it is lower, then how can changes be made such that this metric increases? This is a broad metric, and could be an area of research for the Marketing department. 



## Areas For Further Research

Is there a way to segment bounce rate by traffic source, device and region? Segmenting the bounce rate could assist with making improvements to more specific areas.

What are popular search terms, and are these searches leading to add to carts? This might show us if visitors are finding products that are meeting their needs [2]. How can the product department utilize search results to better serve the client and thus improve conversions?

What specific website pages are leading to a high bounce rate? Is there a way to improve the functionality or appearance of these pages? Something actionable could be to make a changes to such pages and AB test it against the originals. Changes could be moving best selling products to have greater visibility, simplifying or enhancing the site's layout or marketing, etc. 



## References

[1] Ecommerce Analytics: Analyze and Improve the Impact of Your Digital Strategy, by Judah Phillips, published by Pearson, 2016

[2] 3 Essential Analytics Insights for eCommerce Businesses. https://www.youtube.com/watch?v=u0VGHfTxsNw&t=198s. Nov 3/ 2020

[3] Glossary. https://www.optimizely.com/optimization-glossary. Nov 3/ 2020
