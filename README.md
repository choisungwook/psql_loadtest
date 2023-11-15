# 개요
* postgresl 커넥션 테스트

<br>

# postgres 도커 컨테이너 생성

```bash
# 생성
make up

# 삭제
make down
```

<br>

# 로드 테스트
* 파이썬 가상환경 활성화(파이썬 3.9 이상)

```bash
python -m venv venv
source ./venv/bin/activate

pip install -r requirements.txt
```

* 동시 접속 테스트 방법

```bash
# select 1쿼리를 동시 실행
python simple.py -n {동시 접속 개수}

# sleep함수 10초를 동시 실행
python sleep.py -n {동시 접속 개수}
```

<br>

# 테스트 결과

* max_connection 100개 일 때, 동시 접속 100번하면 에러 발생

![](imgs/connection_99.png)

* sleep을 실행하면 activate session발생

![](./imgs/idle_session.png)
