from zxcvbn import zxcvbn
score_list = []
password_array = [('JohnnySmitty','John','Smith'),('enemies','cat','mouse'),('NepalSuman96','suman','nepal'),('DeeWangy123','Daniel','Wang')]
for ele in password_array:
	results = zxcvbn(ele[0], user_inputs=[ele[1], ele[2]])
	score_list.append(results['score'])
print(score_list)