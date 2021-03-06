#Refer to https://manifestoproject.wzb.eu/down/documentation/codebook_MPDataset_MPDS2015a.pdf for specific value meanings 
variables = [
	['country', 'Country ID'],
	['countryname', 'Country'],
	['oecdmember', 'OECD Member'],
	['eumember', 'EU Member'],
	['edate', 'Election Date'],
	['date', 'Year/Month E Date'],
	['party', 'Party ID'],
	['partyname', 'Party Name'],
	['partyabbrev', 'Party'],
	['parfam', 'Party Grouping'],
	['coderid', 'Coder Identification'],
	['manual', 'Coding Manual'],
	['coderyear', 'Coding Year'],
	['testresult', 'Coding Reliability [Krippendorffas],'],
	['testeditsim', 'Coding Realiability [Levenshtein],'],
	['pervote', 'Percentage Vote (%)'],
	['voteest', 'Voting Calculation'],
	['presvote', 'Presidential Vote (%)'],
	['absseat', 'Seats Won'],
	['totseats', 'Total Seats'],
	['progtype', 'Type of Program'],
	['datasetorigin', 'Dataset Publish Origin'],
	['corpusversion', 'Manifesto Corpus Version'],
	['total', 'Total Coded'],
	['peruncod', 'Missing Coded'],
	['per101', 'Foreign Relationships: Positive'],
	['per102', 'Foreeign Relationships: Negative'],
	['per103', 'Anti-Imperialism'],
	['per104', 'Military: Positive'],
	['per105', 'Military: Negative'],
	['per106', 'Peace'],
	['per107', 'Internationalism: Positive'],
	['per108', 'EU/EEC: Positive'],
	['per109', 'Internationalism: Negative'],
	['per110', 'EU/EEC: Negative'],
	['per201', 'Freedom/Human Rights'],
	['per202', 'Democracy'],
	['per203', 'Constitutionalism: Positive'],
	['per204', 'Constitutionalism: Negative'],
	['per301', 'Decentralization'],
	['per302', 'Centralisation'],
	['per303', 'Need Government/Admin Efficiency'],
	['per304', 'Stop Political Corruption'],
	['per305', 'For Political Authority'],
	['per401', 'Free Market Economy'],
	['per402', 'Supply Side Incentives: Positive'],
	['per403', 'Market Regulation'],
	['per404', 'Economic Planning'],
	['per405', 'Mixed Economy'],
	['per406', 'Protectionism: Positive'],
	['per407', 'Protectionism: Negative'],
	['per408', 'Economic Goals'],
	['per409', 'Demand Side Incentives: Positive'],
	['per410', 'Economic Growth: Positive'],
	['per411', 'Technology and Infrastructure: Postiive'],
	['per412', 'Controlled Economy'],
	['per413', 'Nationalisation'],
	['per414', 'Economic Orthodoxy'],
	['per415', 'Marxist Analysis'],
	['per416', 'Economic Growth: Negative'],
	['per501', 'Enviromental Protection'],
	['per502', 'Culture: Positive'],
	['per503', 'Equality: Positive'],
	['per504', 'Welfare State: Positive'],
	['per505', 'Welfare State: Negative'],
	['per506', 'State Education: Positive'],
	['per507', 'State Education: Negative'],
	['per601', 'National Way of Life: Positive'],
	['per602', 'National Way of Life: Negative'],
	['per603', 'Traditional Morality: Positive'],
	['per604', 'Traditional Morality: Negative'],
	['per605', 'Law and Order: Positive'],
	['per606', 'Civic Mindedness: Positive'],
	['per607', 'Multiculturalism: Positive'],
	['per608', 'Multiculturalism: Negative'],
	['per701', 'Labour Groups: Positive'],
	['per702', 'Labour Groups: Negative'],
	['per703', 'Agriculture and Farmers: Positive'],
	['per704', 'Middle Class and Professional Groups: Positive'],
	['per705', 'Underprivileged Minority Groups: Positive'],
	['per706', 'Non-economic Demographic Groups: Positive'],
	['per1011', 'Russia/USSR/CIS: Positive'],
	['per1012', 'Western States: Positive'],
	['per1013', 'Eastern European Countries: Positive'],
	['per1014', 'Baltic States: Positive'],
	['per1015', 'Nordic Council: Positive'],
	['per1016', 'SFR Yugoslavia: Positive'],
	['per1021', 'Russia/USSR/CIS: Negative'],
	['per1022', 'Western States: Negative'],
	['per1023', 'East European Countries: Negative'],
	['per1024', 'Baltic States: Negative'],
	['per1025', 'Nordic Council: Negative'],
	['per1026', 'SFR Yugoslavia: Negative'],
	['per1031', 'Russian Army: Negative'],
	['per1032', 'Independence: Positive'],
	['per1033', 'Rights of Nations: Positive'],
	['per2021', 'Transition to Democracy'],
	['per2022', 'Restrictive Citizenship: Positive'],
	['per2023', 'Lax Citizenship: Positive'],
	['per2031', 'Presidential Regime: Positive'],
	['per2032', 'Republic: Positive'],
	['per2033', 'Checks and Balances: Positive'],
	['per2041', 'Monarchy: Positive'],
	['per3011', 'Republicanism: Positive'],
	['per3051', 'Public Situation: Negative'],
	['per3052', 'Communist: Positive'],
	['per3053', 'Communist: Negative'],
	['per3054', 'Rehabilitation and Compensation: Positive'],
	['per3055', 'Political Coalitions: Positive'],
	['per4011', 'Privatisation: Positive'],
	['per4012', 'Control of Economy: Negative'],
	['per4013', 'Property-Restitution: Positive'],
	['per4014', 'Privatisation Vouchers: Positive'],
	['per4121', 'Social Ownership: Positive'],
	['per4122', 'Mixed Economy: Positive'],
	['per4123', 'Publicly-Owned Industry: Positive'],
	['per4124', 'Socialist Property: Positive'],
	['per4131', 'Property-Restitution: Negative'],
	['per4132', 'Privatisation: Negative'],
	['per5021', 'Private-Public Mix in Culture: Positive'],
	['per5031', 'Private-Public Mix in Social Justice: Positive'],
	['per5041', 'Private-Public Mix in Welfare: Positive'],
	['per5061', 'Private-Public Mix in Education: Positive'],
	['per6011', 'The Karabakh Issue: Positive'],
	['per6012', 'Rebuilding the USSR: Positive'],
	['per6013', 'National Security: Positive'],
	['per6014', 'Cyprus Issue Reference'],
	['per6061', 'General Crisis Reference'],
	['per6071', 'Cultural Autonomy: Positive'],
	['per6072', 'Multiculturalism pro-Roma: Positive'],
	['per6081', 'Multiculturalism pro-Roma: Negative'],
	['per7051', 'Minorities Inland: Positive'],
	['per7052', 'Minorities Abroad: Positive'],
	['per7061', 'War Participants: Positive'],
	['per7062', 'Refugees: Positive'],
	['per103_1', 'Anti-Imperialism: State Centred '],
	['per103_2', 'Anti-Imperialism: Foreign Finance'],
	['per201_1', 'Freedom'],
	['per201_2', 'Human Rights'],
	['per202_1', 'Democracy General: Positive'],
	['per202_2', 'Democracy General: Negative'],
	['per202_3', 'Representative Democracy: Positive'],
	['per202_4', 'Direct Democracy: Positive'],
	['per305_1', 'Political Authority: Party Competence'],
	['per305_2', 'Political Authority: Personal Competence'],
	['per305_3', 'Political Authority: Strong government'],
	['per305_4', 'Transition: Pre-Democratic Elites: Positive'],
	['per305_5', 'Transition: Pre-Democratic Elites: Negative'], 
	['per305_6', 'Transition: Rehabilitation and Compensation'],
	['per416_1', 'Anti-Growth Economy: Positive'], 
	['per416_2', 'Sustainability: Positive'],
	['per601_1', 'National Way of Life General: Positive'],
	['per601_2', 'National Way of Life: Immigration: Negative'],
	['per602_1', 'National Way of Life General: Negative'],
	['per602_2', 'National Way of Life: Immigration: Positive'],
	['per605_1', 'Law and Order: Positive'],
	['per605_2', 'Law and Order: Negative'],
	['per606_1', 'Civic Mindedness General: Positive'],
	['per606_2', 'Civic Mindedness: Bottom-Up Activism'],
	['per607_1', 'Multiculturalism General: Positive'],
	['per607_2', 'Multiculturalism: Immigrants Diversity'],
	['per607_3', 'Multiculturalism: Indigenous rights: Positive'],
	['per608_1', 'Multiculturalism General: Negative'],
	['per608_2', 'Multiculturalism: Immigrants Assimilation'],
	['per608_3', 'Multiculturalism: Indigenous rights: Negative'],
	['per703_1', 'Agriculture and Farmers: Positive'],
	['per703_2', 'Agriculture and Farmers: Negative'],
	['rile', 'Right/Left'],
	['planeco', 'Planned Economy'],
	['markeco', 'Market Economy'],
	['welfare', 'Welfare'],
	['intpeace', 'International Peace'],
	['datasetversion', 'Dataset Version'],
	['id_perm', 'ID_Perm']
]