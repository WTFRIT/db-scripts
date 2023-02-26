from wtfrit_storage_schema import Database
import argparse


if __name__ == "__main__":
	db = Database()
	# db.initialize()
	db.stamp()