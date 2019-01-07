import sys

from .export import export

NAME = 'djexp'
VERSION = '0.0.1'
DESCRIPTION = 'CLI application which exports Django models to json.'


def parse_args(argv):
	if len(argv) != 5:
		raise ValueError('too many arguments were specified')
	try:
		root_idx = argv.index('-r')
	except ValueError as _:
		raise ValueError('root directory is required')
	try:
		settings_idx = argv.index('-s')
	except ValueError as _:
		raise ValueError('settings module is required')
	return {
		'root': argv[root_idx + 1],
		'settings': argv[settings_idx + 1]
	}


def print_help():
	print("""Help:
	-h     print help
	-r     specify project root
	-s     specify an explicit name of settings module""")


def print_info():
	print('{}, version {}\n{}'.format(NAME, VERSION, DESCRIPTION))


def cli_exec():
	if len(sys.argv) == 1:
		print_info()
		print()
		print_help()
		return
	elif len(sys.argv) == 2:
		try:
			sys.argv.index('-h')
			print_help()
			return
		except ValueError as _:
			pass
	else:
		try:
			print('Exporting...')
			args = parse_args(sys.argv)
			export(args['root'], args['settings'])
			print('Done.')
		except ValueError as val_err:
			print('{}: {}, try \'-h\' for help'.format(NAME, val_err.args[0]))
		except Exception as exc:
			print('An error occurred while exporting: {}'.format(exc))
		return
	print('{}: invalid arguments were specified, try \'-h\' for help'.format(NAME))
