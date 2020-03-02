import shutil

def delete_backup():
	shutil.rmtree("C:/primer-entregable/backup")

def main():
	print("Eliminación realizada con éxito")
	delete_backup()

#!/usr/bin/env python3
main()
