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

file_name = 'sample.txt'
regular_params = get_result_parameters(file_name)

# Get the means of all the parameters of the dataset
scores = regular_params[0,]
throttle10 = regular_params[1,]
throttle100 = regular_params[2,]
fast_hash = regular_params[3,]
slow_hash = regular_params[4,]
guesses = regular_params[5,]
guesses_log10 = regular_params[6,]

avg_scores = np.mean(regular_params[0,])
avg_throttle10 = np.mean(regular_params[1,])
avg_throttle100 = np.mean(regular_params[2,])
avg_fast_hash = np.mean(regular_params[3,])
avg_slow_hash = np.mean(regular_params[4,])
avg_guesses = np.mean(regular_params[5,])
avg_guesses_log10 = np.mean(regular_params[6,])
print(avg_scores,avg_throttle10,avg_throttle100,avg_fast_hash,avg_slow_hash,avg_guesses,avg_guesses_log10)

plt.hist2d(guesses_log10,guesses)
plt.show()

sorted_score_list = np.sort(scores)
probs = np.linspace(0, 1, len(sorted_score_list))
plt.step(sorted_score_list,probs)
plt.title('Cummulative Distribution frequency of Password Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency Distributions')
plt.show() 


# fig, axs = plt.subplots(2, 1, constrained_layout=True)
# axs[0].hist2d(guesses,throttle10)
# axs[0].set_title('Histogram')
# axs[0].set_xlabel('hist')
# axs[0].set_ylabel('hist')
# fig.suptitle('This is a somewhat long figure title', fontsize=16)

# axs[1].step(sorted_score_list,probs)
# axs[1].set_xlabel('Scores')
# axs[1].set_title('Cummulative Distribution frequency of Poassword Scores')
# axs[1].set_ylabel('Frequency Distributions')

# plt.show()
# fig, axes = plt.subplots(nrows=1, ncols=2)
# axes[0, 0].plot(score_list)
# axes[0, 1].plot(throttle_list)
# plt.show()



# print(score_list)
# with open('scores.txt', 'w') as f:
#     for ele in score_list:
#         f.write("%s\n" % ele)