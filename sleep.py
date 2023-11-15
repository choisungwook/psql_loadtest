import argparse
import psycopg2
from concurrent.futures import ThreadPoolExecutor

def connect_to_db():
  conn = psycopg2.connect(
    host="127.0.0.1",
    database="test",
    user="root",
    password="password"
  )
  return conn

def idle_session(_):
  conn = connect_to_db()
  cur = conn.cursor()
  cur.execute("SELECT pg_sleep(10)")
  cur.close()
  conn.close()

def run_idle_sessions(num_sessions):
  with ThreadPoolExecutor(max_workers=num_sessions) as executor:
    executor.map(idle_session, range(num_sessions))

def main():
  parser = argparse.ArgumentParser(description='Run load test on PostgreSQL database')
  parser.add_argument('-n', '--num_sessions', type=int, help='Number of sessions to idle')
  args = parser.parse_args()

  run_idle_sessions(args.num_sessions)

if __name__ == "__main__":
  main()
