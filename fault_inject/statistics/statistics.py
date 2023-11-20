import re
import sys
import chardet

class Statistics():
	'''
	Count the number of errors in file named argv [1]
		The file named argv [2] is displayed correctly
	'''
	def __init__(self):
		return

	def adapt_data(self, file):
		'''
		Adjust the data to remove unnecessary parts and ensure that its format is consistent with the correct data
		'''
		ite = ''
		iteline = file.readline()
		while(iteline.split(' ')[0] != 'end' and len(iteline) != 0):
			if iteline.split(' ')[0] == 'Breakpoint' or \
				iteline.split(' ')[0] == '[Inferior' or \
				iteline.split(' ')[0][0:8] == 'Program run time is' or\
				iteline.strip(' ')[0][4:6] == 'at' or\
				iteline.split(' ')[0][0:2] == '0x':
				iteline = file.readline()
				print(iteline)
				continue
			# if iteline != '\n':
			ite = ite + iteline
			iteline = file.readline()
		ite = ite.replace('\n', ' ')
		return ite
	
	def get_correct_ans(self, correct_file_name):
		cor_file = open(correct_file_name,'r', encoding='utf-8')
		cor_ans=''
		for cor_line in cor_file:
			if cor_line.split(' ')[0][0:8] == 'Program run time is':
				continue
			# print(cor_line.split(' ')[0][0:8])
			cor_ans += cor_line.rstrip()
			cor_ans += ' '

		return cor_ans
		#prin(cor_ans)

	def statistic_rates(self, file_name, correct_file_name):
		file = open(file_name, 'r', encoding='utf-8')
		# cor_file = open(correct_file_name,'r')
		round = 0
		seg_fault = 0
		find_err = 0
		correct = 0
		cor_ans = self.get_correct_ans(correct_file_name)
		cor_ans = cor_ans.replace(' ', '')
		print('cor_ans:\n', cor_ans)
		line = file.readline()
		while line:
			if line.split(' ')[0] == 'round':
				round += 1
				print("round:", round)
				
				ite = self.adapt_data(file)
				if len(re.findall(r'#(.*?)#', ite)) == 0:
					break
				ans = re.findall(r"#(.*?)#", ite)[0]
				ans = ans.replace(' ', '')
				print("ans",ans)
				print("len(ans):"+str(len(ans))," len(correct):"+str(len(cor_ans)))
				if re.findall(r'(Segmentation.*fault)', ans):
					seg_fault += 1
				if re.findall(r'(Aborted)', ans):
					find_err += 1
				elif ans == cor_ans or re.findall(r'(normally)', ans):
				#elif ans == cor_ans or len(ans) > len(cor_ans):
					print("correct", round)
					correct += 1
                
			line = file.readline()
		loujian = (seg_fault + find_err + correct) *100/ round
		print("Number of fault injections:", round)
		print("Control flow error detected:", seg_fault+find_err+correct)	
		print("detected error:", find_err)
		print("Segmentation fault:", seg_fault)	
		print("Running correctly:", correct)
		print("Others:", round-find_err-seg_fault-correct)
		print("Detection rate:", loujian,"%")

st = Statistics()
st.statistic_rates(sys.argv[1],sys.argv[2]) 	
