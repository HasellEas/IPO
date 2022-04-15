def all_eq(massive):
	lens = []
	minimal_words = []
	minimal_output = ''
	for tx in massive:
		lens.append(len(tx))
		tx_split = tx.split()
		minimal_len_inlit = []
		for text_split in tx_split:
			minimal_len_inlit.append(len(text_split))
		minimal_words.append(min(minimal_len_inlit))
		minimal_output+=str(tx_split[minimal_words.index(min(minimal_len_inlit))])+" "
	minimal_string = len(minimal_output)
	maximal_string = max(lens)
	rzc = maximal_string - minimal_string
	for n in range(rzc):
		minimal_output+="_"
	return minimal_output

print(all_eq(["сон разница пасажир ржака", "Юля привет сонный арест", "спиливание алгебра химия математика"]))