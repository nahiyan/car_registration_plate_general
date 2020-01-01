import os

def get_new_image_id():
	content_file = open('database/new_image_id.csv', 'r')

	contents = content_file.readline()
	content_file.close()

	if (len(contents.strip()) == 0):
		return 0
	else:
		new_image_id = int(contents)
		return new_image_id


def set_new_image_id(new_image_id):
	content_file = open('database/new_image_id.csv', 'w')
	content_file.write(str(new_image_id))
	content_file.close()

	return new_image_id


def get_last_processed_image_id():
	content_file = open('database/last_processed_image_id.csv', 'r')

	contents = content_file.readline()
	content_file.close()

	if (len(contents.strip()) == 0):
		return 0
	else:
		last_processed_image_id = int(contents)

		return last_processed_image_id


def set_last_processed_image_id(last_processed_image_id):
	content_file = open('database/last_processed_image_id.csv', 'w')
	content_file.write(str(last_processed_image_id))
	content_file.close()

	return last_processed_image_id

def file_exists(file_name):
    return os.path.isfile(file_name)
