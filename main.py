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
	from sys import argv
except Exception as e:
	# If there are any errors in the importing of the required modules, then we print the error on the console screen and exit the script

	print('[ Error : {} ]'.format(e))
	quit()

def main():
	"""
The main function of the script
	"""

	try:
		# Getting the username from the user via arguments

		username = argv[1]
	except IndexError:
		# If the user did not mentioned the username via the arguments, then we ask for the username manually to the user

		username = input('Enter the target username : ')
	finally:
		# If we recieve the username from the user in any either way, then we proceed for the further statements

		try:
			# Sending the GET requests
			response = urlopen('https://instagram.com/{}?__a=1'.format(username))
			response = loads(response.read())

		except Exception as e:
			# If there are any errors in the sending of the GET requests, then we print the error message on the console screen

			print('[ Error : {} ]'.format(e))
		else:
			# If there are no errors in sending the GET request to the server, then we proceed

			try:
				# Getting the profile picture HD version link and then downloading the image

				profilepicLink = response['graphql']['user']['profile_pic_url_hd']
			except KeyError:
				# If there is a key errors in fetching the profile picture of the fetched data, then it might be possible that the profile isnt available

				print('[ Error : Cannot fetch the requested instagram profile ]')
			except Exception as e:
				# For any else error, we print the error message on the console screen

				print('[ Error : {} ]'.format(e))
			else:
				# If there are no errors in the process, then we execute the code for fetching the profile picture

				try:
					# Sending the GET request to download the requested image from the servers of the instagram / facebook
					
					response = urlopen(profilepicLink)
				except Exception as e:
					# If there are any errors in the process of the downloading of the instagram user's profile picture, then we print the error message on the console screen

					print('[ Error : {} ]'.format(e))
				else:
					# If there are no errors in fetching the requested profile picture for the instagram user, then we proceed to saving the image to the local filesystem with the user specified file name

					fileLocation = input("Enter the file location to save the {}'s profile picture : ".format(username))
					try:
						# Saving the profile picture

						with open(fileLocation, 'wb') as image:
							image.write(response.read())
					except Exception as e:
						# If there are any errors in the process of the saving the fetched image to the local machine, then we print the error to the console screen

						print('[ Error : {} ]'.format(e))
					else:
						# If there are no any errors in saving the fetched profile picture to the local filesystem with the user specified filename, then we can assume that the process has been executed without errors, and finally we can exit the script with an success message on the console screen

						print("[ Success : Instagram user {}'s profile picture has been saved to {} ]".format(username, fileLocation))
					finally:
						# Exiting the script finally

						quit()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()