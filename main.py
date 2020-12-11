"""
Instagram Profile Picture Downloader (python)

Version : 1.0.0

Language : Python3

Dependenices : None

Standard Modules Required : json, urllib, sys

Author : Rishav Das
"""

try:
	# Importing the required modules and functions

	from json import loads
	from urllib.request import urlopen
	from sys import argv, platform
except Exception as e:
	# If there are any errors in the importing of the required modules, then we print the error on the console screen and exit the script

	print('[ Error : {} ]'.format(e))
	quit()

# Defining the ANSII color codes variables only if the operating system type is a linux based operating system that runs bash terminal ( or xTerm)
if 'linux' in platform:
	# If the operating system type is a linux based operating system, then we define the ANSII color codes

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	green_rev = '\033[07;92m'
	yellow_rev = '\033[07;93m'
	defcol = '\033[00m' # The default shell color
else:
	# If the operating system type is not a linux based operating system, then we declare the ANSII color code variables as blank

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	green_rev = ''
	yellow_rev = ''
	defcol = ''

# Defining the colored console messages for the beautification of the output
def print_success(message):
	""" The function to print the success message on the console with a colored output (green). The function requires the ANSII color code variables 'green_rev' and 'defcol' to be defined earlier, otherwise errors would arise. To use the function properly, call with a string message data passed as the only argument. """

	print(green_rev + '[ Success : {} ]'.format(message) + defcol)

def print_warning(message):
	""" The function to print the warning message on the console with a colored output (yellow). The function requires the ANSII color code variables 'yellow_rev' and 'defcol' to be defined earlier, otherwise errors would arise. To use the function properly, call with a string message data passed as the only argument. """

	print(yellow_rev + '[ Warning : {} ]'.format(message) + defcol)

def print_error(message):
	""" The function to print the error message on the console with a colored output (red) .The function requires the ANSII color code variables 'red_rev' and 'defcol' to be defined earlier, otherwise errors would arise. To use the function properly, call with a string message data passed as the only argument. """

	print(red_rev + '[ Error : {} ]'.format(message) + defcol)

def main():
	"""
The main function of the script
	"""

	try:
		# Getting the username from the user via arguments

		username = argv[1]
	except IndexError:
		# If the user did not mentioned the username via the arguments, then we ask for the username manually to the user

		username = input(blue + 'Enter the target username : ' + yellow);print(defcol, end = '')
	finally:
		# If we recieve the username from the user in any either way, then we proceed for the further statements

		try:
			# Sending the GET requests
			response = urlopen('https://instagram.com/{}?__a=1'.format(username))
			response = loads(response.read())
		except Exception as e:
			# If there are any errors in the sending of the GET requests, then we print the error message on the console screen

			print_error(e)
		else:
			# If there are no errors in sending the GET request to the server, then we proceed

			try:
				# Getting the profile picture HD version link and then downloading the image

				profilepicLink = response['graphql']['user']['profile_pic_url_hd']
			except KeyError:
				# If there is a key errors in fetching the profile picture of the fetched data, then it might be possible that the profile isnt available

				print_error('Cannot fetch the requested instagram profile')
			except Exception as e:
				# For any else error, we print the error message on the console screen

				print_error(e)
			else:
				# If there are no errors in the process, then we execute the code for fetching the profile picture

				try:
					# Sending the GET request to download the requested image from the servers of the instagram / facebook
					
					response = urlopen(profilepicLink)
				except Exception as e:
					# If there are any errors in the process of the downloading of the instagram user's profile picture, then we print the error message on the console screen

					print_error(e)
				else:
					# If there are no errors in fetching the requested profile picture for the instagram user, then we proceed to saving the image to the local filesystem with the user specified file name

					fileLocation = input(blue + "Enter the file location to save the {}'s profile picture : ".format(username) + yellow);print(defcol, end = '')
					try:
						# Saving the profile picture

						with open(fileLocation, 'wb') as image:
							image.write(response.read())
					except Exception as e:
						# If there are any errors in the process of the saving the fetched image to the local machine, then we print the error to the console screen

						print_error(e)
					else:
						# If there are no any errors in saving the fetched profile picture to the local filesystem with the user specified filename, then we can assume that the process has been executed without errors, and finally we can exit the script with an success message on the console screen

						print_success("Instagram user {}'s profile picture has been saved to {}".format(username, fileLocation))
					finally:
						# Exiting the script finally

						quit()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Exiting')
		quit()