from wtfrit_storage_schema import Database
import argparse

#set up the parser
parser = argparse.ArgumentParser()

parser.add_argument('database_path', default="my_database.db", help="the path to the database file")

parser.add_argument("--stamp-only", action="store_true", help="just stamp the current db version to the db")

#parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
	db = Database("sqlite:///" + args.database_path)
	if args.stamp_only:
		db.stamp()
	else:
		db.initialize()
