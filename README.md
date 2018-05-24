# Capstone-Project
Coaching Recommendation System:
Data Sources
Inputs for phase1/phase 2 features: 
Armchair Analysis dataset: 2000-2016 play-by-play level details on every game played in NFL
 http://armchairanalysis.com/data.php
Web scraping Pro Football Reference: metadata about each team and select statistics fed into clustering. Crawl through 500+ webpages like one linked below aggregating and storing structured/unstructured data in an SQL warehouse:
https://www.pro-football-reference.com/teams/phi/2007.htm
Variables (Phase 1)
Offensive
Base Offense
Run:Pass Ratio (Overall and in Redzone)
YAC/Total Receiving Yards
Air Yards per Pass
Blocking Scheme
Average Time per Play
Proportion of plays in Shotgun formation
Run:Pass Ratio
Penalties per Game
Average Penalty Yardage
*Variables to be included, but not limited to
Defensive
Base Defense (4-3, 3-4 or multiple)
Blitz Percentage (Overall and on 3rd Down)
Primary Coverage Scheme (Man or Zone)
Aggressiveness
Fumbles Forced/Tackle
Penalties per Game
Average Penalty Yardage
*Variables to be included, but not limited to
Variables (Phase 2- Historical Trend Analysis)
Overall
In order to provide the requisite context for historically similar coaching changes we will look into various success metrics differing in granularity and scope: 
Team
Team Success Metric (still to be developed)
Factors in Team Winning Percentage and the Longevity of the New Coach
Offense
Points per Game
Total Yards per Game
Turnovers per Game
Sacks Allowed per Game
Penalties per Game
Average Penalty Yardage
*Variables to be included, but not limited to
Defense
Points Allowed per Game 
Total Yards Allowed per Game
Sacks per Game
Turnovers Forced per Game
Penalties per Game
Average Penalty Yardage
*Variables to be included, but not limited to
Business Questions
Phase 1: Can we group together and provide coach recommendations based on similarity relative to the current coach? 
Phase 2: Are certain head coaching changes more successful than others?
Proposed Techniques/Methodology
Our team’s goal is to cluster head coaches, as well as, offensive and defensive coordinators in the NFL from 2000-2016.  The clustering will occur on the features/variables listed above in the Phase 1 section. The algorithm for clustering will likely come from this list of possibilities (the decision on which one(s) [potential use of ensemble methods] to use will be based on performance:
K-means
Ward Clustering
Birch Clustering
Affinity Propagation
Spectral Clustering
Mini-Batch Clustering
HDBSCAN 
Agglomerative Clustering
HDBScan



Once these coaches have been clustered based on their scheme preferences, we will look at head coaching changes from 2003-2015.  In each instance of a coaching change we will examine the following:
What was the preference of the previous head coach?
Offense or defense
What is the preference of the new head coach?
Offense or defense
Are their preferences the same?
If they are, were the two coaches (previous and new) in the same or different clusters?  
How did the team’s performance change on the new coach’s preferred side of the ball?
Offense or defense
How did the overall team success change with the new head coach?
There will be 12 different types of coaching changes that we will ultimately examine.
Offensive to Offensive (Intra-Cluster)
Offensive to Offensive (Inter-Cluster)
Defensive to Defensive (Intra-Cluster)
Defensive to Defensive (Inter-Cluster)
Offensive to Defensive
Defensive to Offensive
Intra-team Offensive promotion (Intra-cluster)
Intra-team Offensive promotion (Inter-cluster)
Intra-team Defensive promotion (Intra-cluster)
Intra-team Defensive promotion (Inter-cluster)
Intra-team Offensive to Defensive
Intra-team Defensive to Offensive
Our hope is that different patterns will begin to emerge with each of these different coaching changes.  Executives will then be able to make more informed decisions when hiring a new Head Coach.  
Deliverables
Coaching recommendation engine based on similarity relative to current coach (Phase 1)
Strengths and weaknesses of different coaching changes (Phase 2)
User Interface to make suggestions for type of new coach (Phase 2)



Appendix


Base Offense – Type of offensive formation is the team in the majority of the time
Run:Pass Ratio – Number of run plays called compared to the number of pass plays called
YAC/Total Receiving Yards – The number of yards after catch divided by the 
Air Yards per Pass – The number of yards traveled from the line of scrimmage to the spot of the catch
Blocking Scheme – Whether the offensive line uses a man or zone blocking scheme
Average Time per Play – Total Time of Possession divided by the number of offensive plays run
Proportion of Plays in Shotgun Formation – The number of plays run out of a Shotgun formation divided by the number of total plays run on offense
Penalties per Game – The number of penalty flags thrown per game (could be on either or both sides of the ball)
Average Penalty Yardage – The total penalty yardage divided by the number of flags thrown
Base Defense  - Whether the defense runs a 4-3 or 3-4 alignment
Blitz Percentage  - Number of times 5 or more rushers are sent divided by the total number of defensive plays
Primary Coverage Scheme  - Whether the defensive backs employ a man or zone coverage scheme
Aggressiveness – The number of fumbles forced divided by the total number of tackles
Team Success Metric 
Points per Game – The number of points scored per game
Total Yards per Game – The number of passing and rushing yards per game
Turnovers per Game – The number of interceptions thrown and fumbles lost per game
Sacks Allowed per Game – The number of times the team’s quarterback is tackled at or behind the line of scrimmage
Points Allowed per Game – The number of points the other team scores per game
Total Yards Allowed per Game – The number of passing and rushing yards the other team gets per game
Sacks per Game – The number of times the other team’s quarterback is tackled at or behind the line of scrimmage
Turnovers Forced per Game – The number of interceptions forced and fumbles recovered per game
