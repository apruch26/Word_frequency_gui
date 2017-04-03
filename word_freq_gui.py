# IMPORTING tkiner for gui, re for regular expression, string for stinrg operations 
import tkinter
import re
import string

# function to analyze the words in input_file and name the csv file for top 100 words
def analyze(word_freq_list, input_file, top_word_input, total_count, csv_file_input):
	
	#  stopwords: Words you don't want to analyze     
	stopwords = ['this','with','which','from','that','will','think']
	stopwords+= ['basis','also','would','what','they','some']
	stopwords+= ['just','have','much','when','making','crafts']
	stopwords+= ['art','home','the','make','for','and','because']
	stopwords+= ['melissa','about','like','smith','year','say']
	stopwords+= ['again', 'against', 'all', 'almost', 'alone', 'along']
	stopwords+= ['already', 'also', 'although', 'always', 'am', 'among']
	stopwords+= ['amongst', 'amoungst', 'amount', 'an', 'and', 'another']
	stopwords+= ['any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere']
	stopwords+= ['are', 'around', 'as', 'at', 'back', 'be', 'became']
	stopwords+= ['because', 'become', 'becomes', 'becoming', 'been']
	stopwords+= ['before', 'beforehand', 'behind', 'being', 'below']
	stopwords+= ['beside', 'besides', 'between', 'beyond', 'bill', 'both']
	stopwords+= ['bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant']
	stopwords+= ['co', 'computer', 'con', 'could', 'couldnt', 'cry', 'de']
	stopwords+= ['describe', 'detail', 'did', 'do', 'done', 'down', 'due']
	stopwords+= ['during', 'each', 'eg', 'eight', 'either', 'eleven', 'else']
	stopwords+= ['elsewhere', 'empty', 'enough', 'etc', 'even', 'ever']
	stopwords+= ['every', 'everyone', 'everything', 'everywhere', 'except']
	stopwords+= ['few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first']
	stopwords+= ['five', 'for', 'former', 'formerly', 'forty', 'found']
	stopwords+= ['four', 'from', 'front', 'full', 'further', 'get', 'give']
	stopwords+= ['go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her']
	stopwords+= ['here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers']
	stopwords+= ['herself', 'him', 'himself', 'his', 'how', 'however']
	stopwords+= ['hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed']
	stopwords+= ['interest', 'into', 'is', 'it', 'its', 'itself', 'keep']
	stopwords+= ['last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made']
	stopwords+= ['many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine']
	stopwords+= ['more', 'moreover', 'most', 'mostly', 'move', 'much']
	stopwords+= ['must', 'my', 'myself', 'name', 'namely', 'neither', 'never']
	stopwords+= ['nevertheless', 'next', 'nine', 'no', 'nobody', 'none']
	stopwords+= ['noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of']
	stopwords+= ['off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or']
	stopwords+= ['other', 'others', 'otherwise', 'our', 'ours', 'ourselves']
	stopwords+= ['out', 'over', 'own', 'part', 'per', 'perhaps', 'please']
	stopwords+= ['put', 'rather', 're', 's', 'same', 'see', 'seem', 'seemed']
	stopwords+= ['seeming', 'seems', 'serious', 'several', 'she', 'should']
	stopwords+= ['show', 'side', 'since', 'sincere', 'six', 'sixty', 'so']
	stopwords+= ['some', 'somehow', 'someone', 'something', 'sometime']
	stopwords+= ['sometimes', 'somewhere', 'still', 'such', 'system', 'take']
	stopwords+= ['ten', 'than', 'that', 'the', 'their', 'them', 'themselves']
	stopwords+= ['then', 'thence', 'there', 'thereafter', 'thereby']
	stopwords+= ['therefore', 'therein', 'thereupon', 'these', 'they']
	stopwords+= ['thick', 'thin', 'third', 'this', 'those', 'though', 'three']
	stopwords+= ['three', 'through', 'throughout', 'thru', 'thus', 'to']
	stopwords+= ['together', 'too', 'top', 'toward', 'towards', 'twelve']
	stopwords+= ['twenty', 'two', 'un', 'under', 'until', 'up', 'upon']
	stopwords+= ['us', 'very', 'via', 'was', 'we', 'well', 'were', 'what']
	stopwords+= ['whatever', 'when', 'whence', 'whenever', 'where']
	stopwords+= ['whereafter', 'whereas', 'whereby', 'wherein', 'whereupon']
	stopwords+= ['wherever', 'whether', 'which', 'while', 'whither', 'who']
	stopwords+= ['whoever', 'whole', 'whom', 'whose', 'why', 'will', 'wit']
	stopwords+= ['within', 'without', 'would', 'yet', 'you', 'your']
	stopwords+= ['yours', 'yourself', 'yourselves','really','okay']
	
	#--- creating empty variables ---##
	frequency = {}
	results = []
	word_freq_top = ""
	
	##--- get() retrieves user input  ---#
	f = input_file.get()
	csv_f = csv_file_input.get()
	top_word_num = top_word_input.get()

	##--- finding words in input file ---#
	# some of the following code was borrowed 
	# from Abder-Rahman Ali at
	# https://code.tutsplus.com/tutorials/counting-word-frequency-in-a-file-using-python--cms-25965
	document_text = open(f, 'r')
	text_string = document_text.read().lower()
	match_pattern = re.findall(r'\b[a-z]{3,20}\b', text_string)

	# Display total word count at bottom of GUI
	total_word = "Out of " + str(len(match_pattern)) + " total words."
 
 	# going through match_pattern and counting how many times each word is mentioned
	for word in match_pattern:
		if word not in stopwords:
			count = frequency.get(word,0)
			frequency[word] = count + 1

	# creating frequency_list dictionary using frequency 
	frequency_list = frequency.keys()	

	# goes through each word frequency list and saves the word and count in results
	for word in frequency_list:
		tuple = (word, frequency[word])
		results.append(tuple)

	# sorts results in descending order
	word_by_freq = sorted(results, key = lambda word: word[1], reverse = True)

	# writes the csv file 
	with open(csv_f, 'w') as output_file:
		output_file.write("Word,Frequency\n")
		for (word, freq) in word_by_freq[:100]:
			output_file.write(word + "," + str(freq) + "\n")

	# displays the top # of words the user wants to quickly analyze
	rank = 1
	for (word, freq) in word_by_freq[:int(top_word_num)]:
		word_freq_top += word + ": " + str(freq) + "\n"
		rank += 1

	# set() method to send the functions output to the gui	
	word_freq_list.set(word_freq_top)
	total_count.set(total_word)


	
#--- tkinter window ---#
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

word_freq_list = tkinter.StringVar()
total_count = tkinter.StringVar()
input_file = tkinter.StringVar()
top_word_input = tkinter.IntVar()
csv_file_input = tkinter.StringVar()


tkinter.Label(frame, text='File to analyze (file_name.txt):').pack()

text = tkinter.Entry(frame, textvar=input_file)
text.pack()

tkinter.Label(frame, text='Top number of words to quickly view:').pack()

top_word = tkinter.Entry(frame, textvar=top_word_input)
top_word.pack()

tkinter.Label(frame, text="File name for Top 100 words (file_name.csv):").pack()

csv_file = tkinter.Entry(frame, textvar=csv_file_input)
csv_file.pack()

label = tkinter.Label(frame, textvar=word_freq_list)
label.pack()

label_1 = tkinter.Label(frame, textvar=total_count)
label_1.pack()

button = tkinter.Button(frame, text='Analyze', command=lambda: analyze(word_freq_list, input_file, top_word_input, total_count, csv_file_input))
button.pack()

button2 = tkinter.Button(frame, text='Quit', command=lambda: window.destroy())
button2.pack()

window.mainloop()

