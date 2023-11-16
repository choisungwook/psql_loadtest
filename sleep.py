import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import text

def connect_to_db():
  engine = create_engine('postgresql://{id}:{pw}@{ip}:{port}/{database_name}')
  Session = sessionmaker(bind=engine)
  return Session()


def test_connection(_):
  session = connect_to_db()
  result = session.execute(text('SELECT pg_sleep(10)')).fetchone()
  session.close()
  return result

def run_load_test(num_connections):
  with ThreadPoolExecutor(max_workers=num_connections) as executor:
    results = list(executor.map(test_connection, range(num_connections)))
  return results

def main():
  parser = argparse.ArgumentParser(description='Run load test on PostgreSQL database')
  parser.add_argument('-n', '--num_connections', type=int, help='Number of connections to use in the load test')
  args = parser.parse_args()

  results = run_load_test(args.num_connections)
  print(f"Results: {results}")

if __name__ == "__main__":
  main()
