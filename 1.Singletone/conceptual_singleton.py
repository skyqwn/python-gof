class SingletonLogger:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Logger 인스턴스를 새로 생성합니다.")
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._log_file = "app.log"
            cls._instance._initialized = False
        else:
            print("이미 생성된 Logger 인스턴스를 반환합니다.")
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, '_initialized') or not self._initialized:
            print(f"Logger 인스턴스 초기화 중 (Log File: {self._log_file})")
            self.initialized = True
        else:
            print("Logger 인스턴스는 이미 초기화 되었습니다.")

    def log(self, message):
        try:
            with open(self._log_file, "a") as f:
                f.write(f"[LOG] {message}\\n")
            print(f"'{message}'를 로그파일({self._log_file}에 기록했습니다.)")
        except IOError as e:
            print(f"로그 파일 쓰기 오류: {e}")

print("--- Conceptual Singleton (using __new__) ---")
logger1 = SingletonLogger()
logger2 = SingletonLogger()

print(f"logger1 객체 ID: {id(logger1)}")
print(f"logger2 객체 ID: {id(logger2)}")
print(f"두 객체는 동일한가? {logger1 is logger2}")
