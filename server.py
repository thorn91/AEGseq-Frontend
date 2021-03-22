import eel
from os import stat
eel.init('web')


@eel.expose
def parse_input_file(filename):
	print(filename)
	print_input_file(filename)


def print_input_file(filename):
	with open('./samples/SRR062635.filt.fastq', 'r') as f:
		# For now, lets just let JS iterate through the file as an example
		eel.display_input_text(f"> {filename}\n")
		counter = 0
		
		for line in f.readlines():
			eel.display_input_text(line)
			counter += 1

			# Truncate until we decide what to display
			if counter > 90000:
				break;


if __name__ == "__main__":
	eel.start('main.html', mode='')