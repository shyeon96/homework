class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author

class Other(BaseModel):
    TYPE = 'Other Model'
    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Novel, Other):
    extended_type = 'Extended type'
    def __init__(self, data_type, title, content, author):
        self.data_type = data_type
        self.title = title
        self.content = content
        self.author = author
   
    def display_info(self):
        self.PK = BaseModel.PK
        self.TYPE = super().TYPE
        self.extended_type = ExtendedModel.extended_type
        print(f'PK: {self.PK}',end='')
        print(f'TYPE: {self.TYPE}', end='')
        print(f'Extended Type : {self.extended_type}')
        print('데이터를 확장해서 저장합니다.')
        

# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
jung = ExtendedModel('학습서', '수학의 정석', '수학책', '홍성대')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
jung.display_info()
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)
