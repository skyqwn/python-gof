import abc
from typing import List

# --- 1. Product 역할 ---
# 빌더 패턴을 통해 생성될 복잡한 객체
class Computer:
    def __init__(self):
        self.cpu: str | None = None
        self.ram: List[str] = []
        self.storage: str | None = None
        self.gpu: str | None = None
        self.cooler: str | None = None

    def display_specs(self):
        print("--- Computer Specifications ---")
        print(f"CPU: {self.cpu or 'N/A'}")
        print(f"RAM: {', '.join(self.ram) or 'N/A'}")
        print(f"Storage: {self.storage or 'N/A'}")
        print(f"GPU: {self.gpu or 'N/A'}")
        print(f"Cooler: {self.cooler or 'N/A'}")
        print("-----------------------------")

# --- 2. Builder 역할 ---
# 컴퓨터 부품 설정을 위한 추상 인터페이스
class ComputerBuilder(abc.ABC):
    @abc.abstractmethod
    def set_cpu(self, cpu: str) -> 'ComputerBuilder':
        pass
    @abc.abstractmethod
    def add_ram(self, ram_module: str) -> 'ComputerBuilder':
        pass
    @abc.abstractmethod
    def set_storage(self, storage: str) -> 'ComputerBuilder':
        pass
    @abc.abstractmethod
    def set_gpu(self, gpu: str) -> 'ComputerBuilder':
        pass
    @abc.abstractmethod
    def set_cooler(self, cooler: str) -> 'ComputerBuilder':
        pass
    @abc.abstractmethod
    def get_computer(self) -> Computer:
        pass

# --- 3. ConcreteBuilder 역할 ---
# 특정 사양의 컴퓨터를 조립하는 구체 빌더
class GamingPCBuilder(ComputerBuilder):
    def __init__(self):
        print("\\nInitializing Gaming PC Builder...")
        self._computer = Computer()

    def set_cpu(self, cpu: str) -> 'GamingPCBuilder':
        self._computer.cpu = f"High-end Gaming CPU: {cpu}"
        return self # 메서드 체이닝을 위해 self 반환
    def add_ram(self, ram_module: str) -> 'GamingPCBuilder':
        self._computer.ram.append(f"Gaming RAM: {ram_module}")
        return self
    def set_storage(self, storage: str) -> 'GamingPCBuilder':
        self._computer.storage = f"Fast NVMe SSD: {storage}"
        return self
    def set_gpu(self, gpu: str) -> 'GamingPCBuilder':
        self._computer.gpu = f"Powerful Gaming GPU: {gpu}"
        return self
    def set_cooler(self, cooler: str) -> 'GamingPCBuilder':
        self._computer.cooler = f"Liquid Cooler: {cooler}"
        return self
    def get_computer(self) -> Computer:
        return self._computer

class OfficePCBuilder(ComputerBuilder):
    def __init__(self):
        print("\\nInitializing Office PC Builder...")
        self._computer = Computer()
    # ... (OfficePCBuilder의 각 메서드 구현, 위 전체 코드 참조) ...
    def set_gpu(self, gpu: str) -> 'OfficePCBuilder':
        self._computer.gpu = "Integrated Graphics"
        return self
    def get_computer(self) -> Computer:
        return self._computer


# --- 4. Director 역할 (선택적) ---
# 조립 과정을 지시하는 디렉터
class ComputerAssembler:
    def __init__(self, builder: ComputerBuilder):
        self._builder = builder

    def build_minimal_viable_pc(self):
        (self._builder
            .set_cpu("Entry-level CPU")
            .add_ram("8GB DDR4")
            .set_storage("256GB SATA SSD"))

    def build_high_end_gaming_pc(self):
        (self._builder
            .set_cpu("Latest Gen i9/Ryzen 9")
            .add_ram("32GB DDR5 6000MHz")
            .add_ram("32GB DDR5 6000MHz")
            .set_storage("2TB NVMe Gen4 SSD")
            .set_gpu("Top-tier RTX/Radeon GPU")
            .set_cooler("360mm AIO Liquid Cooler"))

# --- 5. Client 사용 예시 ---
if __name__ == "__main__":
    # 방법 1: 클라이언트가 빌더를 직접 사용
    print("--- Builder Pattern Usage (Client directs Builder) ---")
    gaming_builder = GamingPCBuilder()
    gaming_pc = (gaming_builder
                 .set_cpu("AMD Ryzen 7 7800X3D")
                 .add_ram("16GB DDR5")
                 .set_storage("1TB NVMe PCIe 4.0 SSD")
                 .set_gpu("NVIDIA GeForce RTX 4080")
                 .get_computer())
    gaming_pc.display_specs()

    # 방법 2: 디렉터를 사용하여 조립 과정 캡슐화
    print("\\n--- Builder Pattern Usage (Director directs Builder) ---")
    builder_for_director = GamingPCBuilder()
    assembler = ComputerAssembler(builder_for_director)
    assembler.build_high_end_gaming_pc()
    director_built_gaming_pc = builder_for_director.get_computer()
    director_built_gaming_pc.display_specs()
