import logger_module
import logger_module as logger2 
print(f"두 모듈 객체는 동일한가? {logger_module is logger2}") 

logger_module.log("Main에서 첫 번째 로그")
logger2.log("Main에서 두 번째 로그")

print(f"기록된 로그: {logger_module.get_logs()}")
