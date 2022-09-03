#import regex module
import re

#import the mac addresses from a file, form of MAC address should be like 98D8639B7996
mac_addr_pool = '/path/to/your/file'

#define the regex pattern in splitting two characters into group, six groups in total
regex_pattern = r"([0-9a-fA-F]{1,2})([0-9a-fA-F]{1,2})([0-9a-fA-F]{1,2})([0-9a-fA-F]{1,2})([0-9a-fA-F]{1,2})([0-9a-fA-F]{1,2})"

#read content from file
with open(mac_addr_pool, 'r') as f:
	#use for loop to regex-searching in each line
	for line in f:
		re_result = re.search(regex_pattern, line)
		#concatenate groups extracted by regex with ':'
		mac_addr = re_result.group(1) \
		+ ':' + re_result.group(2) \
		+ ':' + re_result.group(3) \
		+ ':' + re_result.group(4) \
		+ ':' + re_result.group(5) \
		+ ':' + re_result.group(6)
		print(mac_addr)
