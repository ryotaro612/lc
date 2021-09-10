#!/usr/bin/env python3
import sys
import os
import argparse

def parse(args) -> argparse.Namespace:
	"""

	Parameters
	----------
	args: list[str]

	References
	----------
	https://docs.python.org/ja/3/library/argparse.html#sub-commands

	"""
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='command')
	src_parser = subparsers.add_parser('src')
	src_parser.add_argument('filepath')
	test_parser = subparsers.add_parser('test')
	test_parser.add_argument('filepath')
	return parser.parse_args(args)
	

def generate_src(target_file: str):
	if os.path.exists(target_file):	
		raise RuntimeError('file already exists.')
	cmake_path = f'{os.path.dirname(target_file)}/CMakeLists.txt'

	prefix = ''
	with open(cmake_path) as f:
		texts = f.readlines()
		if len(texts) > 0 and not texts[-1].endswith('\n'):
			prefix = '\n'
	with open(cmake_path, 'a') as f:
		_, file = os.path.split(target_file)
		name, _ = os.path.splitext(file)
		f.writelines([f'{prefix}add_library({name} {file})\n'])
	with open(target_file, 'w') as f:
		f.writelines(['#include<bits/stdc++.h>\n', 'using namespace std;\n'])

def generate_test(target_file: str):
	if os.path.exists(target_file):	
		raise RuntimeError('file already exists.')
	cmake_path = f'{os.path.dirname(target_file)}/CMakeLists.txt'

	prefix = ''
	with open(cmake_path) as f:
		text = f.read()
		if text.endswith('\n\n'):
			prefix = ''
		elif text.endswith('\n'):
			prefix = '\n'
		else:
			prefix = '\n\n'

	with open(cmake_path, 'a') as f:
		_, file = os.path.split(target_file)
		name, _ = os.path.splitext(file)
		f.writelines([
			f'{prefix}add_executable({name}_test {file})\n',
			f'target_link_libraries({name}_test {name} gtest_main)\n',
			f'gtest_discover_tests({name}_test)',
		])
	with open(target_file, 'w') as f:
		f.writelines([
			'#include <gtest/gtest.h>\n',
		])

if __name__ == '__main__':
	options = parse(sys.argv[1:])

	if options.command == 'src':
		generate_src(options.filepath)
	elif options.command == 'test':
		generate_test(options.filepath)