# abstract_factory_example.py
import abc
import random

# --- 1. Abstract Product 역할 ---
# 생성될 각 제품군(버튼, 텍스트박스)의 공통 인터페이스
class Button(abc.ABC):
    @abc.abstractmethod
    def paint(self):
        pass

class Textbox(abc.ABC):
    @abc.abstractmethod
    def display_text(self, text):
        pass

# --- 2. Concrete Product 역할 (Windows 제품군) ---
class WindowsButton(Button):
    def paint(self):
        print("Painting a Windows style button.")

class WindowsTextbox(Textbox):
    def display_text(self, text):
        print(f"Displaying text in a Windows style textbox: '{text}'")

# --- 2. Concrete Product 역할 (macOS 제품군) ---
class MacButton(Button):
    def paint(self):
        print("Painting a macOS style button.")

class MacTextbox(Textbox):
    def display_text(self, text):
        print(f"Displaying text in a macOS style textbox: '{text}'")

# --- 3. Abstract Factory 역할 ---
# 각 추상 제품을 생성하는 메서드를 선언하는 인터페이스
class WidgetFactory(abc.ABC):
    @abc.abstractmethod
    def create_button(self) -> Button:
        pass

    @abc.abstractmethod
    def create_textbox(self) -> Textbox:
        pass

# --- 4. Concrete Factory 역할 ---
# 특정 제품군의 객체를 생성하는 구체 팩토리
class WindowsFactory(WidgetFactory):
    def create_button(self) -> Button:
        print("Windows Factory: Creating a Windows Button.")
        return WindowsButton()
    def create_textbox(self) -> Textbox:
        print("Windows Factory: Creating a Windows Textbox.")
        return WindowsTextbox()

class MacFactory(WidgetFactory):
    def create_button(self) -> Button:
        print("Mac Factory: Creating a macOS Button.")
        return MacButton()
    def create_textbox(self) -> Textbox:
        print("Mac Factory: Creating a macOS Textbox.")
        return MacTextbox()

# --- 5. Client 역할 ---
# Abstract Factory와 Abstract Product 인터페이스만 사용하는 클라이언트
class Application:
    def __init__(self, factory: WidgetFactory):
        print(f"\\nInitializing Application with factory: {factory.__class__.__name__}")
        self._factory = factory
        self._button = None
        self._textbox = None

    def create_ui(self):
        print("Application: Creating UI elements using the provided factory...")
        self._button = self._factory.create_button()
        self._textbox = self._factory.create_textbox()
        print("Application: UI elements created successfully.")

    def run(self):
        if not self._button or not self._textbox:
            print("Error: UI elements have not been created yet!")
            return
        print("\\nApplication: Running main logic...")
        self._button.paint()
        self._textbox.display_text("Hello Abstract Factory Pattern!")
        print("Application: Run complete.")

# --- 클라이언트가 사용할 팩토리를 결정하는 로직 ---
def get_factory() -> WidgetFactory:
    """현재 환경에 맞는 위젯 팩토리를 반환 (시뮬레이션)."""
    os_name = random.choice(["windows", "mac"])
    print(f"\\nSimulating OS detection... Detected: {os_name}")
    if os_name == "windows":
        return WindowsFactory()
    elif os_name == "mac":
        return MacFactory()
    else:
        raise NotImplementedError(f"Widget factory for OS '{os_name}' is not implemented.")

# --- 메인 실행 코드 ---
if __name__ == "__main__":
    print("--- Abstract Factory Pattern Usage Example ---")
    try:
        current_factory = get_factory()
        app = Application(current_factory)
        app.create_ui()
        app.run()

        print("-" * 20)

        current_factory_2 = get_factory()
        app_2 = Application(current_factory_2)
        app_2.create_ui()
        app_2.run()
    except NotImplementedError as e:
        print(e)
    print("\\n--- Example Finished ---")

