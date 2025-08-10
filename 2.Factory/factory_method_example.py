import abc # 추상 기본 클래스를 위한 모듈

# --- 1. Product 역할 ---
class Document(abc.ABC):
    @abc.abstractmethod
    def open(self):
        pass
    @abc.abstractmethod
    def read(self):
        pass    

# --- 2. CreateProduct 역할 ---
class PDFDocument(Document):
    def open(self):
        print(f"Opening PDF document...")
    def read(self):
        print(f"Reading content from PDF document...")

class WordDocument(Document):
    def open(self):
        print(f"Opening Word document...")
    def read(self):
        print(f"Reading content from Word document...")

# --- 3. Creator 역할 ---
class DocumentParser(abc.ABC):
    @abc.abstractmethod
    def create_document(self) -> Document: #팩토리 매서드 선언
        pass

    def parse_and_read(self):
        print(f"[{self.__class__.__name__}] Starting parsing process...")
        # 이 시점에는 어떤 문서가 올지 모름! 오직 Document 인터페이스에만 의존!
        doc = self.create_document()
        doc.open()
        doc.read()
        print(f"[{self.__class__.__name__}] Parsing finished.")
        return doc

# --- 4.ConcreateCreator 역할 ---
class PDFParser(DocumentParser):
    #추상 팩토리 매서드 구현
    def create_document(self) -> Document:
        print("PDF Parser: Creating PDF Document.")
        return PDFDocument()
    
class WordPaser(DocumentParser):
    #추상 팩토리 매서드 구현
    def create_document(self) -> Document:
        print("Word Parser: Creating Word Document.")
        return WordDocument()
    
# ---클래식 팩토리 매서드 사용 예시 ---
print("--- Classic Factory Method Usage ---")
pdf_parser: DocumentParser = PDFParser()
word_parser: DocumentParser = WordPaser()

# 클라이언트는 Creator의 일반 매서드만 호출하면, 객체 생성은 위임됨
pdf_doc = pdf_parser.parse_and_read()
print("-" * 10)
word_doc = word_parser.parse_and_read()
print("-" * 20)




def simple_document_factory(doc_type: str) -> Document | None:
    print(f"\\nSimple Factory: Attempting to create '{doc_type}' document")
    type_lower = doc_type.lower()
    if type_lower == "pdf":
        print("Simple Factory: Creating PDF Document.")
        return PDFDocument()
    elif type_lower == "word":
        print("SImple Factory: Creating Word Document.")
        return WordDocument()
    else:
        print(f"Simple Factory: Unsupported document type '${doc_type}'.")
        return None
print("--- Simple Factory Function Usage ---")
doc1 = simple_document_factory("pdf")
if doc1:
    doc1.open()
    doc1.read()