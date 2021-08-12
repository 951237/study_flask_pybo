from pybo import db

# db.Model 상속 
# db는 __init__.py에서 생성한 SQLAlchemy객체
class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)  # 고유아이디 숫자 속성
    subject = db.Column(db.String(200), nullable = False)   # 글자 200자 
    content = db.Column(db.Text(), nullable = False)    # 텍스트 속성
    create_date = db.Column(db.DateTime(), nullable = False)    # 날짜 시간 속성

class Answer(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    question_id = db.Column(db.Interger, db.ForeignKey('question.id', ondelete = 'CASCADE'))    # foreignkey - 외부키 , ondelete - 삭제연동 cascade - 질문삭제시 답변도 함께 삭제
    question = db.Relationship('Question', backref=db.backref('answer_set'))    # 답변 모델에서 질문 모델을 참조하기 위해생성. relationship 참조, backref 역참조
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)