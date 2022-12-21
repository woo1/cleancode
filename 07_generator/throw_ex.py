class CustomException(Exception):
    pass

def stream_data(db_handler):
    while True:
        try:
            yield db_handler.read_n_records(10)
        except CustomException as e:
            print(f"처리 가능한 에러, 계속 진행 {e}")
        except Exception as e:
            print(f"처리 불가능한 에러, 중단 {e}")
            db_handler.close()
            break
