from zxcvbn import zxcvbn
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def get_result_parameters(in_file):
	"""
	Input: (String) File path that contains the passwords
	return (2d) array of containing the parameters of passGAN for online throttles, offline slow and fast hashing
	and number of guesses required to break passwords
	"""

	fileName = in_file
	lineList = [line.rstrip('\n') for line in open(fileName)]

	score_list = []
	online_throttle10 = []
	online_throttle100 = []
	offline_fast_hash = []
	offline_slow_hash = []
	guesses = []
	guesses_log10 = []


	for ele in lineList:
		results = zxcvbn(ele, user_inputs=[" ", " "])
		score_list.append(results['score'])
		online_throttle10.append(results['crack_times_seconds']['online_no_throttling_10_per_second'])
		online_throttle100.append(results['crack_times_seconds']['online_throttling_100_per_hour'])
		offline_fast_hash.append(results['crack_times_seconds']['offline_fast_hashing_1e10_per_second'])
		offline_slow_hash.append(results['crack_times_seconds']['offline_slow_hashing_1e4_per_second'])
		guesses.append(results['guesses'])
		guesses_log10.append(results['guesses_log10'])
	score_list = np.asarray(score_list,dtype=float)
	online_throttle10 = np.asarray(online_throttle10,dtype=float)
	online_throttle100 = np.asarray(online_throttle100,dtype=float)
	offline_fast_hash = np.asarray(offline_fast_hash,dtype=float)
	offline_slow_hash = np.asarray(offline_slow_hash,dtype=float)
	guesses = np.asarray(guesses,dtype=float)
	guesses_log10 = np.asarray(guesses_log10,dtype=float)
	return np.vstack((score_list,online_throttle10,online_throttle100,offline_fast_hash,offline_slow_hash,guesses,guesses_log10))

file_name1 = 'orig_40k.txt'
file_name2 = 'modified_40k.txt'
regular_params_orig = get_result_parameters(file_name1)
regular_params_modified = get_result_parameters(file_name2)

Get the means of all the parameters of the dataset
scores_orig,score_modified = regular_params_orig[0,],regular_params_modified[0,]
throttle10_orig,thrott = regular_params[1,]
throttle100 = regular_params[2,]
fast_hash = regular_params[3,]
slow_hash = regular_params[4,]
guesses_orig,guesses_modified= regular_params_orig[5,], regular_params_modified[5,]
guesses_log10_orig,guesses_log10_modified = regular_params_orig[6,],regular_params_modified[6,]

avg_scores = np.mean(regular_params[0,])
avg_throttle10 = np.mean(regular_params[1,])
avg_throttle100 = np.mean(regular_params[2,])
avg_fast_hash = np.mean(regular_params[3,])
avg_slow_hash = np.mean(regular_params[4,])
avg_guesses = np.mean(regular_params[5,])
avg_guesses_log10 = np.mean(regular_params[6,])
print(avg_scores,avg_throttle10,avg_throttle100,avg_fast_hash,avg_slow_hash,avg_guesses,avg_guesses_log10)
Params for original. dataset
(1.5925, 5323675136.357611, 1916523049088.74, 5.323675136357612, 5323675.136357611, 53236751363.57612, 6.2561273091854455)
Params for modified dataset
(1.5561883116883117, 6809398.840911937, 2451383582.728298, 0.006809398840911938, 6809.398840911938, 68093988.40911938, 6.165661717562823)


plt.hist2d(scores_orig,score_modified)
plt.xlabel('Scores on Original Dataset')
plt.ylabel('Scores on Modified Dataset')
plt.title('Scores on Original and Modified Dataset')
plt.show()

plt.hist2d(guesses_log10_orig,guesses_log10_modified)
plt.xlabel('Guesses on Original Dataset')
plt.ylabel('Guesses on Modified Dataset')
plt.title('Guesses on Original and Modified Dataset')
plt.show()

N = 3
original_params= (1.5925, 5.323675136357612, 6.2561273091854455)
modified_params = (1.5561883116883117, 6.809398840911938, 6.165661717562823)
orig_errs= (0.4, 0.4, 0.4)
modified_errs = (0.4, 0.4, 0.4)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, original_params, width, yerr=orig_errs)
p2 = plt.bar(ind, modified_params, width,
             bottom=original_params, yerr=modified_errs)

plt.ylabel('Scores and Guesses')
plt.title('Average Scores and Guesses on Datasets')
plt.xticks(ind, ('Scores', 'Guesses', 'Log Guesses',))
# plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Original RockYou', 'Extended RockYou'))

plt.show()

N = 4
original_params= (5.323675136357611, 1.91652304908874, 5.323675136357612,5.323675136357611)
modified_params = (6.809398840911937, 2.451383582728298, 6.809398840911938, 6.809398840911938)
orig_errs= (0.4, 0.4, 0.4, 0.4)
modified_errs = (0.4, 0.4, 0.4, 0.4)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, original_params, width, yerr=orig_errs)
p2 = plt.bar(ind, modified_params, width,
             bottom=original_params, yerr=modified_errs)

plt.ylabel('Average Number of Varied Attacks')
plt.title('Average Attacks Per Time')
plt.xticks(ind, ('Throttle/Hr', 'Throttle/Sec', 'Fast Hash','Slow Hash'))
# plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Original RockYou', 'Extended RockYou'))

plt.show()





plt.hist2d(guesses_log10,guesses)
plt.show()

plt.plot(scores)
plt.title('zxcvbn scores of passwords')
plt.xlabel('Passwords')
plt.ylabel('Scores')
plt.show()

sorted_score_list = np.sort(scores)
probs = np.linspace(0, 1, len(sorted_score_list))
plt.step(sorted_score_list,probs)
plt.title('Cummulative Distribution frequency of Password Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency Distributions')
plt.show() 


# print(score_list)
# with open('scores.txt', 'w') as f:
#     for ele in score_list:
#         f.write("%s\n" % ele)