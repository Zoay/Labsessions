class CredentialsReader:

	@staticmethod
	def read(filename):
		import os
		credentials = {}
		twidentials = os.path.join(os.getcwd(), filename)
		with open(twidentials, 'r') as cf:
			lines = cf.readlines()
			#print(lines)
			for line in lines:
				key, value = line.strip('\n').split('=')
				credentials[key] = value
		return credentials

class ArgParser:
	@staticmethod
	def parse():
		import argparse
		parser = argparse.ArgumentParser(prog='Twibot', add_help=True)
		parser.add_argument('-k', '--keywords', action="store", dest="kw_file",
			metavar='keywords.txt',
			help="fichier contenant la liste de mots presents dans les tweets")
		parser.add_argument('-a', action='append', dest='args_list', default=[],
			metavar='arg1 -a arg2, -a arg3, ...',
			help="liste des mots cles presents dans les tweets ")
		parser.add_argument('-c', '--credentials', action="store", dest="credentials",
			metavar='credentials.txt',
			help="fichier contenant les credentials Twitter")
		parser.add_argument('--version', action='version', version='%(prog)s 1.5.0')


		return parser.parse_args()
"""if __name__ == '__main__':
	import os
	cred = ArgParser.parse()
	print (cred)
	#print cred['kw_file']
	print cred.kw_file"""
	