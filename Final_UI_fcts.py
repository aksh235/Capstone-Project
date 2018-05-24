import pandas as pd
import numpy as np
import sys

#Create function to fix the metadata file with coaching change binary variables
def team_off_def_clustering(team_name,coach_pref):
	#team_name is going to have something like 'ARI', 'PHI', 'NYJ'
	team_id_to_find = team_name + '_15'
	
	#read in all csv's
	off_final = pd.read_csv('off_final.csv')
	off_success = pd.read_csv('off_success_wTeamID_00_16.csv')
	def_final = pd.read_csv('def_final.csv')
	def_success = pd.read_csv('def_success_wTeamID_00_16.csv')
	changes_transID = pd.read_csv('meta_w_changes_trans_id.csv')

	#data cleaning
	changes_transID = changes_transID.drop('team_id', axis = 1)
	changes_transID['team_id'] = off_final['team_id']

	changes_transID.loc[changes_transID.def_align == '3-Apr', 'def_align1'] = '4-3'
	changes_transID.loc[changes_transID.def_align == '4-Mar', 'def_align1'] = '3-4'
	changes_transID.loc[changes_transID.def_align == '3/4/', 'def_align1'] = '3-4'
	changes_transID = changes_transID.drop(['def_align','record','def_align1'],axis=1)



	#Join coaches data with clusters (offensive)
	off_metadata_cluster = off_final.merge(changes_transID, on='team_id')
	off_metadata_cluster = off_metadata_cluster.drop(off_metadata_cluster.columns[1:7], axis=1)
	off_metadata_cluster = off_metadata_cluster.drop(['team'],axis=1)
	

	#Join coaches data with clusters (defensive)
	def_metadata_cluster = def_final.merge(changes_transID, on='team_id')
	def_metadata_cluster = def_metadata_cluster.drop(def_metadata_cluster.columns[1:5],axis=1)
	def_metadata_cluster = def_metadata_cluster.drop(['team'],axis=1)
	
	

	if coach_pref.lower() == 'offense':
		init_clusters_off = off_metadata_cluster[off_metadata_cluster['team_id'] == team_id_to_find][['clustering_byPassAtt','clustering_byPassComp','clustering_noPassYds']]
		return init_clusters_off
		#['clustering_byPassAtt'],init_clusters_off['clustering_byPassComp'],init_clusters_off['clustering_noPassYds']
	elif coach_pref.lower() == 'defense':
		init_clusters_def = def_metadata_cluster[def_metadata_cluster['team_id'] == team_id_to_find]['defClustering']
		return init_clusters_def
	else:
		print('coaching preference is in wrong format')
		
def teamID_to_organization(df_w_teamID):
	test = pd.DataFrame(df_w_teamID['team_id'].str.split('_',expand=True))
	test.columns = ['v','yr']
	lookup_tbl = pd.read_csv('team_lookup1.csv')
	names_org_tbl = test.merge(lookup_tbl, on='v')
	
	
	full_join_org_coach = pd.concat([df_w_teamID.reset_index(),pd.DataFrame(names_org_tbl['mascot1'])],axis=1, ignore_index=True)
	if full_join_org_coach.shape[1] == 11:
		full_join_org_coach1 = full_join_org_coach.iloc[:,2:]
		full_join_org_coach1.columns = ['team_id','cluster','year','head_coach','off_coord','def_coord','binary','trans_id','org']
	elif full_join_org_coach.shape[1] == 13:
		full_join_org_coach1 = full_join_org_coach.iloc[:,2:]
		full_join_org_coach1.columns = ['team_id','cluster1','cluster2','cluster3','year','head_coach','off_coord','def_coord','binary','trans_id','org']
	
	
	# full_join_org_coach.columns = ['team_id','cluster','year','head_coach','off_coord','def_coord','binary','trans_id','org']
	return full_join_org_coach1
	
	
	
	

def filter_succMet_byCluster(team_name,coach_pref, weights):

	#read in offense and defense sucess metrics by cluster jumps
	off_succ_met_byCJ = pd.read_csv('offensive_succMetrics_changes_wClusters.csv')
	def_succ_met_byCJ = pd.read_csv('defensetuples.csv')
	off_cluster_coaches = pd.read_csv('offensive_clusters_coachnames.csv')
	def_cluster_coaches = pd.read_csv('defensive_clusters_coachnames.csv')
	
	
	
	
	init_clusters = team_off_def_clustering(team_name,coach_pref)
	all_cluster_checks = pd.DataFrame()
	if coach_pref.lower() == 'offense':
		init_clusters_cols = init_clusters.transpose()
		init_clusters_cols.columns = ['off_clusters']
		unique_off_clusters = init_clusters_cols['off_clusters'].unique()
		for i in unique_off_clusters:
			cl1 = off_succ_met_byCJ[off_succ_met_byCJ['clustering1_byPassAtt_init'] == i]
			cl2 = off_succ_met_byCJ[off_succ_met_byCJ['clustering2_byPassComp_init'] == i]
			cl3 = off_succ_met_byCJ[off_succ_met_byCJ['clustering3_noPass_init'] == i]
			all_clusters_check1 = pd.concat([cl1,cl2,cl3], axis=0)
			all_cluster_checks = all_cluster_checks.append(all_clusters_check1)
		# return all_cluster_checks
		off_succ_mets = all_cluster_checks[['Pass_Yards_Per_Game_Rank', 'Points_Per_Game_Rank', 'Run_Yards_Per_Game_Rank', 'Sacks_Allowed_Per_Game_Rank', 'Turnovers_Per_Game_Rank']]

		first_val_set = np.random.randint(0,len(weights))
		# print(first_val_set)
		# print(weights)
		for i, val in enumerate(weights):
			if i == first_val_set:
				first_val = np.random.choice([0.2,0.5,0.8],1)[0]
				weights[i] = first_val
			else:
				weights[i] = 0
		# print(weights)
		for i, val in enumerate(weights):
			if val == 0:
				weights[i] = (1 - first_val) / 4
			else:
				weights[i] = val
		
		
		# print(weights)
		# sys.exit()
			
	
		
		
		for_client_scores = pd.Series(np.dot(off_succ_mets,weights))

		# print(for_client_scores)
		# print(all_cluster_checks)
		# sys.exit()
		# scored_succ_mets =  pd.concat([all_cluster_checks.reset_index(),for_client_scores],axis=1)
		# sorted_scored_succ_mets = scored_succ_mets.sort_values(0, ascending=False)
		# sorted_scored_succ_mets_top5 = sorted_scored_succ_mets.iloc[:5,:]
		# final_cluster_allmethods = pd.concat([sorted_scored_succ_mets_top5['clustering1_byPassAtt_final'],sorted_scored_succ_mets_top5['clustering2_byPassComp_final'],sorted_scored_succ_mets_top5['clustering3_noPass_final']], axis=0)
		
		
		viable_coach_df = off_cluster_coaches[(off_cluster_coaches['year'] == 2015) & (off_cluster_coaches['clustering_byPassAtt'] == np.random.choice(np.arange(2,5),1)[0])]
		# print(viable_coach_df)
		full_df = teamID_to_organization(viable_coach_df)
		
		return full_df[['off_coord','org']]

		
		# return viable_coach_df.columns	#['off_coord']
		
		sys.exit()
		
	elif coach_pref.lower() == 'defense':
		
		unique_def_clusters = init_clusters.unique()
		all_cluster_checks = all_cluster_checks.append(def_succ_met_byCJ[def_succ_met_byCJ['Custering1_init'].isin(unique_def_clusters)])
		
		def_succ_mets = all_cluster_checks[['Pass_Yards_Allowed_Per_Game_Rank', 'Points_Per_Game_Allowed_Rank', 'Run_Yards_Allowed_Per_Game_Rank', 'Sacks_Per_Game_Rank', 'Turnovers_Forced_Per_Game_Rank']]
		
		first_val_set = np.random.randint(0,len(weights))
		# print(first_val_set)
		# print(weights)
		for i, val in enumerate(weights):
			if i == first_val_set:
				first_val = np.random.choice([0.2,0.5,0.8],1)[0]
				weights[i] = first_val
			else:
				weights[i] = 0
		# print(weights)
		for i, val in enumerate(weights):
			if val == 0:
				weights[i] = (1 - first_val) / 4
			else:
				weights[i] = val
		# print(weights)
		# sys.exit()
		# for_client_scores = pd.Series(np.dot(def_succ_mets,weights))

		
		# scored_succ_mets =  pd.concat([all_cluster_checks.reset_index(),for_client_scores],axis=1)
		# sorted_scored_succ_mets = scored_succ_mets.sort_values(0, ascending=False)
		# sorted_scored_succ_mets_top3 = sorted_scored_succ_mets.iloc[:3,:]
		# if len(sorted_scored_succ_mets_top3['Clustering1_finall'].unique()) < 3:
			# viable_coach_df = def_cluster_coaches[(def_cluster_coaches['year'] == 2015) & (def_cluster_coaches['defClustering'] == sorted_scored_succ_mets_top3['Clustering1_finall'].mode()[0])]
			# full_df = teamID_to_organization(viable_coach_df)
			
			# return full_df[['def_coord','org']]
		# else:
			# final_cluster_preIndexing = sorted_scored_succ_mets_top3['Clustering1_finall'].reset_index()
			# final_cluster_noMode = final_cluster_preIndexing[final_cluster_preIndexing.index == 0]['Clustering1_finall']
			

		viable_coach_df = def_cluster_coaches[(def_cluster_coaches['year'] == 2015) & (def_cluster_coaches['defClustering'] == np.random.choice(np.arange(1,5),1)[0])]
		full_df = teamID_to_organization(viable_coach_df)
		
		return full_df[['def_coord','org']]
		
		

	else:
		print('coaching preference is in wrong format')
	

# def return_viable_coaches(coach_pref):
	# off_cluster_coaches = pd.read_csv('offensive_clusters_coachnames.csv')
	# def_cluster_coaches = pd.read_csv('defensive_clusters_coachnames.csv')
	# if coach_pref.lower() == 'offense':
		# off_cluster_coaches[off_cluster_coaches['year'] == 15 & off_cluster_coaches['clustering_byPassAtt'] == 
	# elif coach_pref.lower() == 'defense':
	
	# else:
		# print('coaching preference is in wrong format')

"""		
off_weights = ['Pass_Yards_Per_Game_Rank', 'Points_Per_Game_Rank', 'Run_Yards_Per_Game_Rank', 'Sacks_Allowed_Per_Game_Rank', 'Turnovers_Per_Game_Rank']
def_weights = ['Pass_Yards_Allowed_Per_Game_Rank', 'Points_Per_Game_Allowed_Rank', 'Run_Yards_Allowed_Per_Game_Rank', 'Sacks_Per_Game_Rank', 'Turnovers_Forced_Per_Game_Rank']
"""

test = filter_succMet_byCluster('PHI','offense',[0,0,0,0.9,0.1])
print(test)
print('**************************************')
test = filter_succMet_byCluster('BAL','offense',[0,0,0.9,0.1,0])
print(test)
print('**************************************')
test = filter_succMet_byCluster('NYJ','offense',[0.9,0.1,0,0,0])
print(test)
print('**************************************')
test = filter_succMet_byCluster('NYJ','defense',[0.5,0.5,0,0.0,0])
print(test)
print('**************************************')
test = filter_succMet_byCluster('NYJ','defense',[0,0.5,0,.5,0])
print(test)

# print(test1)




	
	
