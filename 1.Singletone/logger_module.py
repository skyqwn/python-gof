_log_file = "module_app.log"
_log_entries = []

print(f"Logger 모듈({__name__}) 로딩됨")

def configure(log_file_name="module_app.log"):
    global _log_file
    _log_file = log_file_name
    print(f"로그 파일이 '{_log_file}'로 설정됨")

def log(message):
    entry = f"[MODULE LOG] {message}"
    print(f"'{message}' 기록 완료 (모듈 로거)")
    _log_entries.append(entry)

def get_logs():
    return _log_entries